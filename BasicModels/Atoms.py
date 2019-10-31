from collections import deque

class Attendant:
    '''
        Attendant class:
            Each attendant has it own queue, for 1 queue models the clients end_time must be appended
            to the shortest Attendant.queue. 
    '''
    isFree: bool
    last_end_time: float

    def __init__(self):
        self.queue = deque()
        self.isFree = True
        self.last_end_time = 0

    def append(self, end_time):
        '''
            Append the client end_time to its own attendant queue
        '''
        self.isFree = False
        self.queue.append(end_time)

    def getAwaitTime(self):
        '''
            Returns the Await Time in the attendant queue
        '''
        return self.queue[len(self.queue)-1] if len(self.queue) > 0 else 0

    def updateQueue(self, real_time):
        while len(self.queue) > 0 and self.queue[0] <= real_time:
            self.last_end_time = self.queue.popleft()
        
        if len(self.queue) == 0:
            isFree = True

    def __len__(self):
        return len(self.queue)

class Client:
    '''
        Client class:
            interarrival_time: Tempo entre clientes (TEC)
            service_time: Tempo de serviço (TS)
            start_time: Tempo do inicio do serviço
            end_time: Tempo do fim do serviço
    '''
    interarrival_time: float
    service_time: float
    start_time: float
    end_time: float
    spent_time: float
    queue_time: float

    def __init__(self, interarrival_time, service_time, arrive_time, queue_time):
        self.interarrival_time = interarrival_time
        self.service_time = service_time
        self.spent_time = service_time + queue_time
        self.start_time = arrive_time + queue_time
        self.end_time = self.start_time + service_time
        self.queue_time = queue_time