from progress.bar import Bar

from utils.statistics import ci
from QueueModel import simulate
from utils.Random import Congrencial as crand

if __name__ == "__main__":
    n_atendentes = [(3,6), (4,5), (5,4), (6,3)]

    for c,a in n_atendentes:
        sAvgSt1 = []; sAvgSt2 = []
        sAvgSpt1 = []; sAvgSpt2 = []
        sAvgQt1 = []; sAvgQt2 = []
        sPFA1 = []; sPFA2 = []
        sPAQ1 = []; sPAQ2 = []
    
        for i in Bar('Simulando para {} caixas e {} atendentes de lanche'.format(c, a)).iter(range(5000)):
            crand.seed()
            
            (avgSt1, avgSpt1, avgQt1, pFA1, pAQ1),\
            (avgSt2, avgSpt2, avgQt2, pFA2, pAQ2) = simulate(c,a,30)
            
            sAvgSt1.append(avgSt1); sAvgSpt1.append(avgSpt1); sAvgQt1.append(avgQt1); sPFA1.append(pFA1); sPAQ1.append(pAQ1)
            sAvgSt2.append(avgSt2); sAvgSpt2.append(avgSpt2); sAvgQt2.append(avgQt2); sPFA2.append(pFA2); sPAQ2.append(pAQ2)

        print("Resultados para {} caixas e {} atendentes de lanche".format(c,a))

        print("""Fila 1: \n
            \tTempo médio de serviço: {}\n
            \tTempo médio gasto no sistema: {}\n
            \tTempo médio de fila: {}\n
            \tProbabilidade de atendente livre: {}\n
            \tProbabilidade de esperar na fila  {}\n
            """.format(ci(sAvgSt1), ci(sAvgSpt1), ci(sAvgQt1), ci(sPFA1), ci(sPAQ1)))
    
        print("""Fila 2: \n
            \tTempo médio de serviço: {}\n
            \tTempo médio gasto no sistema: {}\n
            \tTempo médio de fila: {}\n
            \tProbabilidade de atendente livre: {}\n
            \tProbabilidade de esperar na fila  {}\n
            """.format(ci(sAvgSt2), ci(sAvgSpt2), ci(sAvgQt2), ci(sPFA2), ci(sPAQ2)))

        
    