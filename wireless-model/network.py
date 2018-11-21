import copy
import devices
import generator

class CellularNetwork:
    def __init__(self):
        self.ue = []
        self.bs = []
        self.Generator = generator.Generator(self)
        self.constraintAreaMaxX = []
        self.constarintAreaMaxY = []
        self.radius = []



    def addOneBSTower(self, x_pos, y_pos):
        # for i in range(3):
        bs = devices.BS()
        bs.x = x_pos
        bs.y = y_pos
        self.bs.append(copy.deepcopy(bs))


    def connectUserToTheBestBS(self):
        for ue in self.ue:
            ue.connectToTheBestBS(self.bs)