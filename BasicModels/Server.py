from utils.Distributions import Erlang, Exponencial
from BasicModels.Atoms import Attendant, Client

class Server:
    attendants: list
    real_time: float

    def __init__(self, n_attendants):
        self.attendants = [Attendant() for _ in range(n_attendants)]
        self.real_time = 0

    def client_arrival(self, client: Client):
        '''
            
        '''
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

    def update(self, time_inc):
        self.real_time += time_inc
        for a in self.attendants:
            a.updateQueue(self.real_time)

    def getQueuesSize(self):
        count = 0
        for a in self.attendants:
            count += len(a)

        return count

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

        return (t_free_att, free_time/t_free_att) if t_free_att != 0 else (0, 0)
