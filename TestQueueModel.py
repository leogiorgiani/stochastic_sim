from utils.Distributions import Exponencial, Erlang
from utils.Random import Congrencial as crand
from BasicModels.Server import Server
from BasicModels.Atoms import Client

def simulate(n_attendants = 1, TMAX = 60, tec_g = Exponencial(4), ts_g = Erlang(2,3)):
    '''
        Simula o modelo de fila de n caixas
        Retorna:    Tempo médio de serviço,
                    Tempo médio despendido no sistema,
                    Tempo médio de espera na fila,
                    Probabilidade de se encontrar um funcionario livre
                    Probabilidade de um cliente esperar na fila
    '''
    sv = Server(n_attendants)

    while sv.real_time < TMAX:
        tec = tec_g.x()
        ts = ts_g.x()
        sv.update(tec)
        t_fila = max(sv.attendants[sv.getMinimalServiceTime()].getAwaitTime() - sv.real_time, 0)
        cl = Client(tec, ts, sv.real_time, t_fila)
        sv.client_arrival(cl)

    return sv.stats.resume(TMAX)

if __name__ == "__main__":
    crand.seed(1000)
    print(simulate())