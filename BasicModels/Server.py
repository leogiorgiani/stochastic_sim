from utils.Distributions import Erlang, Exponencial
from BasicModels.Atoms import Attendant, Client
from dataclasses import dataclass

@dataclass
class Stats:
    n_clients = 0
    total_service_time = 0 
    total_spent_time = 0
    total_queue_time = 0
    total_free_attendents_avgtime = 0
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
                self.total_queue_time/self.n_clients, self.total_free_attendents_avgtime/time,\
                self.total_clients_inqueue / self.n_clients

class Server:
    '''
            In This Class the simulation of one queue is made by looking into the lowest end time on queue,
        and represents this model:

                            Attendents
            Queue         +->  [] (1)
            | | | | | | | +->  [] (2)
                        ...
                          +->  [] (n)

    '''
    attendants: list
    real_time: float
    stats: Stats

    def __init__(self, n_attendants):
        self.attendants = [Attendant() for _ in range(n_attendants)]
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
        self.stats.total_clients_inqueue += 0 if self.hasFreeAttendant() else 1

        # Client arrival
        self.attendants[self.getMinimalServiceTime()].append(client.end_time)

    def getMinimalServiceTime(self):
        '''
            Returns the index of the attentend with minimal service time
        '''
        min = self.attendants[0]
        idx = 0
        for i, a in enumerate(self.attendants):
            if min.getAwaitTime() > a.getAwaitTime():
                min = a
                idx = i
        
        return idx

    def getMinimalAwaitTime(self):
        return max(self.attendants[self.getMinimalServiceTime()].getAwaitTime() - self.real_time, 0)

    def update(self, time_inc):
        self.real_time += time_inc
        for a in self.attendants:
            a.updateQueue(self.real_time)
        self.stats.total_free_attendents_avgtime += self.getFreeTime()

    def getQueuesSize(self):
        count = 0
        for a in self.attendants:
            count += len(a)

        return count

    def hasFreeAttendant(self) -> bool:
        for a in self.attendants:
            if a.isFree:
                return True

        return False

    def getFreeTime(self):
        '''
            Returns the number of free attendents and the average free time of them.
        '''
        t_free_att = 0
        free_time = 0
        for a in self.attendants:
            if(a.isFree):
                t_free_att += 1
                free_time += self.real_time - a.last_end_time

        return free_time/t_free_att if t_free_att != 0 else 0
