from dataclasses import dataclass
from random import Congrencial as crand

@dataclass
class Coordinates:
    x: float
    y: float

    def __add__(self, other):
        return Coordinates(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

def thinkdir(random = crand.random()):
    rand = random()
    if rand < 0.45: #to north 45%
        return Coordinates(0,1)
    if rand < 0.55: #to south 10%
        return Coordinates(-1,0)
    if rand < 0.65: #to west 10%
        return Coordinates(0,-1)
    return Coordinates(1,0) #to east 35%

def bebado(tempomax ,n = 10000, final_pos = Coordinates(3,4), init_pos = Coordinates(0, 0), random=crand.random):    
    arrived = 0
    for _ in range(n):
        current_pos = init_pos
        tempo = 0
        while current_pos != final_pos and tempo < tempomax:
            if random() < 0.3: # 30% chances of stop and thinking where to go
                tempo += 1
                
            dir = thinkdir(random)
            current_pos += dir
            tempo += 5
        
        if current_pos == final_pos:
            arrived += 1

    return arrived/n

if __name__ == "__main__":
    # crand.seed(2000)
    print(bebado(60))
    print(bebado(120))
    print(bebado(180))