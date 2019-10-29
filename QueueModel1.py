from utils.Distributions import Exponencial, Erlang
from utils.Random import Congrencial as crand
from BasicModels.Server import Server
from BasicModels.Atoms import Client

'''
    TODO: Get Stats
'''

def simulate(n_attendants = 1, TMAX = 60, tec_g = Exponencial(4), ts_g = Erlang(2,3)):
    '''
        Simula o modelo de fila de n caixas
    '''
    sv = Server(n_attendants)
    while sv.real_time < TMAX:
        tec = tec_g.x()
        ts = ts_g.x()
        sv.update(tec)
        t_fila = max(sv.attendants[sv.getMinimalServiceTime()].getAwaitTime() - sv.real_time, 0)
        cl = Client(tec, ts, sv.real_time, t_fila)
        n, t_FuncL = sv.getFreeTime()
        sv.client_arrival(cl)
        print("{:.5f}, {:.5f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {}".\
            format(tec, ts, sv.real_time, cl.start_time, cl.end_time, t_fila, cl.spent_time, n, sv.getQueuesSize()))

if __name__ == "__main__":
    crand.seed()
    print("tec,ts,treal,tinit,tfim,tfila,tsist,tCLivre,n_Fila")
    simulate()