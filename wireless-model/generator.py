import devices
import math

class Generator:
    def __init__(self, parent):
        self.parent = parent

    def createHexagonalBSdeployment(self, radius, numberOfBS = 36):
        for i in range(0, numberOfBS):
            bs = devices.BS()
            bs.ID = i
            a = (numberOfBS - 2) % 6
            b = (numberOfBS - 2) // 6 + 1
            if a == 0:
                bs.x = radius * b * 3 / 2
                bs.y = math.sqrt(3) * radius / 2
            elif a == 1:
                bs.x = 0
                bs.y = math.sqrt(3) * radius
            elif a == 2:
                bs.x = -radius * b * 3 / 2
                bs.y = math.sqrt(3) * radius / 2
            elif a == 3:
                bs.x = -radius * b * 3 / 2
                bs.y = -math.sqrt(3) * radius / 2
            elif a == 4:
                bs.x = 0
                bs.y = -math.sqrt(3) * radius
            else:
                bs.x = radius * b * 3 / 2
                bs.y = -math.sqrt(3) * radius /2
            self.parent.bs.apend(bs)



