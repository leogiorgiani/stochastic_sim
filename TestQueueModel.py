from utils.Distributions import Exponencial, Erlang
from utils.Random import Congrencial as crand
from BasicModels.System import System
from BasicModels.Atoms import Client

def simulate(n_attendants = 1, TMAX = 30, tec_g = Exponencial(4), ts_g = Erlang(2,3)):
    '''
            Simulates the queue model of 1 System with n attendents,
        Returns the stats from simulation.
        
        ** See System Documentation
    '''
    sv = System(n_attendants)

    while sv.real_time < TMAX:
        tec = tec_g.x()
        ts = ts_g.x()
        sv.update(tec)
        cl = Client(tec, ts, sv.real_time, sv.getMinimalAwaitTime())
        sv.client_arrival(cl)

    return sv.stats.resume(TMAX)

if __name__ == "__main__":
    print(simulate())