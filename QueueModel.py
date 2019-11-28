from utils.Distributions import Exponencial, Erlang
from utils.Random import Congrencial as crand
from BasicModels.System import System
from BasicModels.Atoms import Client

def simulate(n_caixas = 1, n_atendentes = 1, TMAX = 30, tec_g= Exponencial(4),
 tscaixa_g = Erlang(2,3), tsatend_g = Erlang(1.5, 4)):
    caixas = System(n_caixas)
    atendentes = System(n_atendentes)

    prev_tec_att = 0

    while caixas.real_time < TMAX :
        tec_caixa = tec_g.x()
        ts_caixa = tscaixa_g.x()
        caixas.update(tec_caixa)
        cl_c = Client(tec_caixa, ts_caixa, caixas.real_time, 
         caixas.getMinimalAwaitTime())
        caixas.client_arrival(cl_c)
        ts_atend = tsatend_g.x()
        atendentes.update(cl_c.end_time - prev_tec_att)
        prev_tec_att = cl_c.end_time
        cl_a = Client(cl_c.spent_time, ts_atend, atendentes.real_time,
         atendentes.getMinimalAwaitTime())
        atendentes.client_arrival(cl_a)
    
    return caixas.stats.resume(TMAX), atendentes.stats.resume(TMAX)


if __name__ == "__main__":
    print(simulate())