from utils.Distributions import Exponencial, Erlang
from utils.Random import Congrencial as crand
from BasicModels.Server import Server
from BasicModels.Atoms import Client

def simulate(n_attendants = 1, TMAX = 60, tec_g = Exponencial(4), ts_g = Erlang(2,3)):
    '''
            Simulates the queue model of 1 Server with n attendents,
        Returns the stats from simulation.
        
        ** See Server Documentation
    '''
    sv = Server(n_attendants)

    while sv.real_time < TMAX:
        tec = tec_g.x()
        ts = ts_g.x()
        sv.update(tec)
        cl = Client(tec, ts, sv.real_time, sv.getMinimalAwaitTime())
        sv.client_arrival(cl)

    return sv.stats.resume(TMAX)

if __name__ == "__main__":
    print(simulate())