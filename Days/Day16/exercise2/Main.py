from Days.Day16.exercise2.Computer import Computer
from Days.Day16.exercise2.CPU import CPU
from Days.Day16.exercise2.Memory import Memory

memory = Memory()
cpu = CPU()

computer = Computer(cpu,memory)
computer.showCPU()

