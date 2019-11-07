from progress.bar import Bar

from utils.statistics import ci
from QueueModel import simulate
from utils.Random import Congrencial as crand

'''
    TODO: Full stats from n simulations
'''

if __name__ == "__main__":
    sAvgSt1 = []; sAvgSt2 = []
    sAvgSpt1 = []; sAvgSpt2 = []
    sAvgQt1 = []; sAvgQt2 = []
    sPFA1 = []; sPFA2 = []
    sPAQ1 = []; sPAQ2 = []

    for i in Bar('Simulando', suffix='%(percent)d%%').iter(range(5000)):
        crand.seed(100+i*100)
        
        (avgSt1, avgSpt1, avgQt1, pFA1, pAQ1),\
         (avgSt2, avgSpt2, avgQt2, pFA2, pAQ2) = simulate()
        
        sAvgSt1.append(avgSt1); sAvgSpt1.append(avgSpt1); sAvgQt1.append(avgQt1); sPFA1.append(pFA1); sPAQ1.append(pAQ1)
        sAvgSt2.append(avgSt2); sAvgSpt2.append(avgSpt2); sAvgQt2.append(avgQt2); sPFA2.append(pFA2); sPAQ2.append(pAQ2)

    print(ci(sAvgQt1))
    
    