from utils.Distributions import Erlang, Exponencial
from BasicModels.Atoms import Server, Client
from dataclasses import dataclass

@dataclass
class Stats:
    n_clients = 0
    total_service_time = 0 
    total_spent_time = 0
    total_queue_time = 0
    total_free_server_avgtime = 0
    total_clients_inqueue = 0

    def resume(self, time):
        '''
            Returns stats:
                Average service time,
                Average spent time,
                Average queue time,
                Probability of finding a free attendent,
                Probability of await in queue.
        '''
        return  self.total_service_time/self.n_clients, self.total_spent_time/self.n_clients,\
                self.total_queue_time/self.n_clients, self.total_free_server_avgtime/time,\
                self.total_clients_inqueue / self.n_clients

class System:
    '''
            In This Class the simulation of one queue is made by looking into the lowest end time on queue,
        and represents this model:

                            Server
            Queue         +->  [] (1)
            | | | | | | | +->  [] (2)
                        ...
                          +->  [] (n)

    '''
    servers: list
    real_time: float
    stats: Stats

    def __init__(self, n_servers):
        self.servers = [Server() for _ in range(n_servers)]
        self.real_time = 0
        self.stats = Stats()

    def client_arrival(self, client: Client):
        '''
                Append the client in the queue with minimal service time (getMinimalServiceTime()), and update
            the stats of the server.
        '''
        # Stats Processing
        self.stats.n_clients += 1
        self.stats.total_service_time += client.service_time
        self.stats.total_spent_time += client.spent_time
        self.stats.total_queue_time += client.queue_time
        self.stats.total_clients_inqueue += 0 if self.hasFreeServer() else 1

        # Client arrival
        self.servers[self.getMinimalServiceTime()].append(client.end_time)

    def getMinimalServiceTime(self):
        '''
            Returns the index of the attentend with minimal service time
        '''
        min = self.servers[0]
        idx = 0
        for i, a in enumerate(self.servers):
            if min.getAwaitTime() > a.getAwaitTime():
                min = a
                idx = i
        
        return idx

    def getMinimalAwaitTime(self):
        '''
            Returns the minimal await time in the server 
        '''
        return max(self.servers[self.getMinimalServiceTime()].getAwaitTime() - self.real_time, 0)

    def update(self, time_inc):
        '''
            Update the server time using a time increment (TEC) and update the queues status.
        '''
        self.real_time += time_inc
        for a in self.servers:
            a.updateQueue(self.real_time)
        self.stats.total_free_server_avgtime += self.getFreeTime()

    def getQueuesSize(self):
        '''
            Returns the sum of the sizes of each server queue
        '''
        count = 0
        for a in self.servers:
            count += len(a)

        return count

    def hasFreeServer(self) -> bool:
        '''
            Returns True if some server is idle, otherwise returns False
        '''
        for a in self.servers:
            if a.isFree:
                return True

        return False

    def getFreeTime(self):
        '''
            Returns the number of free server and the average free time of them.
        '''
        t_free_att = 0
        free_time = 0
        for a in self.servers:
            if(a.isFree):
                t_free_att += 1
                free_time += self.real_time - a.last_end_time

        return free_time/t_free_att if t_free_att != 0 else 0
