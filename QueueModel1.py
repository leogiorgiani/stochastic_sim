from utils.Distributions import Exponencial, Erlang
from utils.Random import Congrencial as crand
from BasicModels.Server import Server
from BasicModels.Atoms import Client

def simulate(n_attendants = 2, TMAX = 60, tec_g = Exponencial(4), ts_g = Erlang(2,3)):
    '''
        Simula o modelo de fila de n caixas
        Retorna:    Tempo médio de serviço,
                    Tempo médio despendido no sistema,
                    Tempo médio de espera na fila,
                    Probabilidade de se encontrar um funcionario livre
                    Probabilidade de um cliente esperar na fila
    '''
    sv = Server(n_attendants)

    Tts = 0
    Tspenttime = 0
    Tqueuetime = 0
    nClientes = 0
    Tt_FuncL = 0
    Tcfila = 0
    while sv.real_time < TMAX:
        nClientes += 1
        tec = tec_g.x()
        ts = ts_g.x()
        Tts+=ts
        sv.update(tec)
        t_fila = max(sv.attendants[sv.getMinimalServiceTime()].getAwaitTime() - sv.real_time, 0)
        Tcfila += 1 if t_fila > 0 else 0
        Tqueuetime += t_fila
        cl = Client(tec, ts, sv.real_time, t_fila)
        Tspenttime += cl.spent_time
        n, t_FuncL = sv.getFreeTime()
        Tt_FuncL+=t_FuncL

        sv.client_arrival(cl)

    return Tts/nClientes, Tspenttime/nClientes, Tqueuetime/nClientes, Tt_FuncL/TMAX, Tcfila/nClientes

if __name__ == "__main__":
    crand.seed(1000)
    print(simulate())