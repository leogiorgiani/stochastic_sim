from utils.statistics import ci
from QueueModel import simulate

'''
    TODO: Full stats from n simulations
'''

if __name__ == "__main__":
    StatsCaixas = []
    StatsAtententes = []
    for _ in range(1000):
        caix, att = simulate()
        StatsCaixas.append(caix); StatsAtententes.append(att)


    