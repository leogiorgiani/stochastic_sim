from Distributions import Exponencial, Erlang, samplenumbers
from collections import deque
from Random import Congrencial as crand

if __name__ == "__main__":
    Gtec = Exponencial(4)
    Gts = Erlang(2, 3)

    crand.seed(1000)

    treal = 0
    tinit = 0
    tfim = 0
    tsist = 0

    TMAX = 60

    queue = deque()
    
    #variaveis para analise estatistica
    tms = 0
    tds = 0
    tmef = 0
    pfunclivre = 0
    pfila = 0  
    clientes = 0

    print("TEC,TS,Treal,Tinicio,Tfim,Tf,Tsistema,Tcaixalivre, N pessoas")
    while treal < TMAX:
        tec = Gtec.x()
        ts = Gts.x()

        treal += tec

        
        # definição tempo de inicio e tempo de fila
        if tinit < tfim:
            tinit += prev_ts
            tf = tinit - treal
            tcaixalivre = 0
        else:
            tinit = treal
            tf = 0
            tcaixalivre = tfim - treal

        # definição tfim
        tfim = tinit + ts

        queue.append(tfim)

        # definição tempo no sistema
        tsist = tfim - treal

        if len(queue) > 0 and queue[0] < treal:
            queue.popleft()
        
        nf = len(queue)

        print("{:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {}".format(tec,ts,treal,tinit,tfim,tf,tsist,tcaixalivre,nf))
        prev_ts = ts

        # estudos estatisticos
        clientes +=1
        tms += ts
        tds += tsist
        tmef += tf
        pfunclivre += tcaixalivre
        if nf > 0:
            pfila += 1


    print(",,,,,,,,,Tempo médio de Serviço:, {}", (tms/clientes))
    print(",,,,,,,,,Tempo médio despendido no sistema:, {}", (tds/clientes))
    print(",,,,,,,,,Tempo médio de espera na fila:, {}", (tmef/clientes))
    print(",,,,,,,,,Probabilidade do funcionario estar livre:, {}", (pfunclivre/TMAX))
    print(",,,,,,,,,Probabilidade de esperar na fila:, {}", (pfila/clientes)) 