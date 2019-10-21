from utils.Distributions import Erlang, Exponencial
from Models.Atoms import Attendant

'''
    TODO:   - clients arrival
            - clients disparture
            - stats processing
            - generalized model
'''

class Server:
    attendants: list
    real_time: float

    def __init__(self, n_attendants):
        self.attendants = [Attendant() for _ in range(n_attendants)]

    def client_arrival(self, client):
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

    def update_server(self):
        for a in self.attendants:
            a.updateQueue(self.real_time)
