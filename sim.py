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
