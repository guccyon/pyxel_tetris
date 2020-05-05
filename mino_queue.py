from mino import MinoType, Mino
from queue import SimpleQueue
import random

class MinoQueue:
    def __init__(self):
        self.queue = SimpleQueue()

    def get_next(self):
        if self.queue.empty():
            self.prepare_next_round()
            
        return Mino(self.queue.get())
    
    def prepare_next_round(self):
        types = list(MinoType)
        random.shuffle(types)
        for i in types:
            self.queue.put(i)
