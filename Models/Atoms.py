from collections import deque

class Attendant:
    '''
        Attendant class:
            Each attendant has it own queue, for 1 queue models the clients end_time must be appended
            to the shortest Attendant.queue. 
    '''
    def __init__(self):
        self.queue = deque()

    def append(self, end_time):
        '''
            Append the client end_time to its own attendant queue
        '''
        self.queue.append(end_time)

    def getAwaitTime(self):
        '''
            Returns the Await Time in the attendant queue
        '''
        return self.queue[len(self.queue)-1] if len(self.queue) > 0 else 0

    def updateQueue(self, real_time):
        if len(self) > 0:
            while self.queue[0] <= real_time:
                self.queue.popleft()

    def __len__(self):
        return len(self.queue)

class Client:
    '''
        Client class:
            ??
    '''
    interarrival_time: float #TEC
    service_time: float #TS
    arrive_time: float #TReal
    start_time: float
    end_time: float

    def __init__(self, interarrival_time, service_time, arrive_time, queue_time):
        self.interarrival_time = interarrival_time
        self.service_time = service_time
        self.arrive_time = arrive_time
        self.start_time = arrive_time + queue_time
        self.end_time = start_time + service_time