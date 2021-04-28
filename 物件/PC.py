#object is instance of the class

class PC:
    def __init__(self):
        self.mb = None
        self.ps = None
        self.kb = None
        self.sc = None
        self.mem = None
        self.power = False
        self.pcie = None
        
    def open(self):
        self.power = True
class Motherboard:
    def __init__(self,name):
        self.name = name
        self.cpu = None
class Keyboard:
    def __init__(self,keys):
        self.keys = keys
class powersupport:
    def __init__(self,w):
        self.w = w
class Screen:
    def __init__(self,size):
        self.size = size
class Memory:
    def __init__(self,G):
        self.G = G
class PCIE:
    def __init__(self,names,GB):
        self.names = names
        self.GB = GB
class CPU:
    def __init__(self,brand):
        self.brand = brand
        self.hz = None
class HZ:
    def __init__(self,ghz):
        self.ghz =ghz
        self.st = None
class Socket:
    def __init__(self,socket):
        self.socket = socket

asus = PC()
asus.mb = Motherboard("華碩")
asus.kb = Keyboard(108)
asus.ps = powersupport(750)
asus.sc = Screen(17)
asus.mem = Memory(16)
asus.pcie = PCIE("1080ti", 4)
asus.mb.cpu = CPU("amd")
asus.mb.cpu.hz = HZ(4.3)
asus.mb.cpu.hz.st =Socket(1151)




