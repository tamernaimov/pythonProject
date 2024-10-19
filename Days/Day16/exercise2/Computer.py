from Days.Day16.exercise2.CPU import CPU
from Days.Day16.exercise2.Memory import Memory

class Computer():
    def __init__(self,cpu,memory):
        self.cpu = cpu
        self.memory = memory

    def showCPU(self):
        self.cpu.showstats()

    def showMemory(self):
        self.memory.showstats()