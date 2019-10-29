from utils.Distributions import Exponencial, Erlang
from utils.Random import Congrencial as crand
from BasicModels.Server import Server
from BasicModels.Atoms import Client

def simulate(n_caixas = 1, n_atendentes = 1, TMAX = 60, tec_g= Exponencial(4), tscaixa_g = Erlang(2,3), tsatend_g = Erlang(1.5, 4)):
    caixas = Server(n_caixas)
    atendentes = Server(n_atendentes)

    while caixas.real_time < TMAX :
        tec_caixa = tec_g.x()
        ts_caixa = tscaixa_g.x()
        caixas.update(tec_caixa)
        t_fila_caixa = max(caixas.attendants[caixas.getMinimalServiceTime()].getAwaitTime() - caixas.real_time, 0)
        cl_c = Client(tec_caixa, ts_caixa, caixas.real_time, t_fila_caixa)
        caixas.client_arrival(cl_c)
        ts_atend = tsatend_g.x()
        atendentes.update(cl_c.spent_time)
        t_fila_atendente = max(atendentes.attendants[caixas.getMinimalServiceTime()].getAwaitTime() - atendentes.real_time, 0)
        cl_a = Client(cl_c.spent_time, ts_atend, atendentes.real_time, t_fila_atendente)
        atendentes.client_arrival(cl_a)


if __name__ == "__main__":
    simulate()