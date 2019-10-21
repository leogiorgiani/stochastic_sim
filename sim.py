from utils.Distributions import Exponencial, Erlang
from utils.Random import Congrencial as crand
from collections import deque

'''
    TODO:
        1. create a method for executing one entrance in the queue, and then be able to enqueue 
        two or more queues.
        2. create a method that receives the number of queues used in series and how many queues 
        is used in parallel.
        3. be able to perform statistical analysis for each queue, and the whole system
'''

def simulate(Gtec = Exponencial(4), Gts = Erlang(2, 3), TMAX = 60):
    #tempos
    treal = 0
    tinit = 0
    tfim = 0
    tsist = 0
    
    #contadores
    cTServ = 0 # Soma dos TS
    cTSist = 0 # Soma dos TS + tempo na fila
    cTEspera = 0 # Soma dos Tempos na fila
    cTFuncLivre = 0 # Soma Tempo da Fila Vazia
    cClientesFila = 0 # Soma do numero de clientes na fila
    tClientes = 0 #Total de Clientes

    queue = deque()
    
    while treal < TMAX:
        tClientes += 1 #Cada iteração é um cliente entrando 
        
        tec = Gtec.x()#Gera valores de uma distribuição
        ts = Gts.x()    


        cTServ += ts #Soma tempo serviços

        treal += tec    #Tempo real += Tempo Entre Chegadas
        
        if treal < tfim: #Tem alguem na fila
            tinit = tfim
            tfila = tinit - treal
            tCLivre = 0
            cClientesFila +=1
        else:
            tinit = treal
            tfila = 0
            tCLivre = treal - tfim

        cTFuncLivre += tCLivre
        cTEspera += tfila

        tfim = tinit + ts # Tempo final = Tempo inicio + Tempo Sistema

        queue.append(tfim)

        # definição tempo no sistema
        tsist = tfila + ts
        cTSist += tsist

        if len(queue) > 0 and queue[0] < treal:
            queue.popleft()
    

        # print("{:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {}".format(tec,ts,treal,tinit,tfim,tfila,tsist,tCLivre,len(queue)))
        prev_ts = ts

    
    return cTServ/tClientes, cTSist/tClientes, cTEspera/tClientes, cTFuncLivre/TMAX, cClientesFila/tClientes

if __name__ == "__main__":
    MAX = 200
    Medias = []
    for i in range(MAX):
        pass
        