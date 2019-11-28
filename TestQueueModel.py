from utils.Distributions import Exponencial, Erlang
from utils.Random import Congrencial as crand
from BasicModels.System import System
from BasicModels.Atoms import Client

def simulate(n_attendants = 2, TMAX = 30, tec_g = Exponencial(4), ts_g = Erlang(2,3)):
    '''
            Simulates the queue model of 1 System with n attendents,
        Returns the stats from simulation.
        
        ** See System Documentation
    '''
    print("tec,ts,treal,tinit,tfim,tfila,tsist,tCLivre,n_Fila")
    sv = System(n_attendants)

    while sv.real_time < TMAX:
        tec = tec_g.x()
        ts = ts_g.x()
        sv.update(tec)
        cl = Client(tec, ts, sv.real_time, sv.getMinimalAwaitTime())
        sv.client_arrival(cl)
        print("{:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {}".format(
            tec, ts, sv.real_time, cl.start_time, cl.end_time, 
            cl.queue_time, cl.spent_time, sv.getFreeTime(), sv.getQueuesSize()
        ))


    return sv.stats.resume(TMAX)

if __name__ == "__main__":
    print(simulate())