import math
from devices import UE,BS
import random

class CellularNetwork:
    def __init__(self):
        self.ue = []
        self.bs = []
        self.constraintAreaMaxX = []
        self.constraintAreaMaxY = []


    def createHexagonalBSdeployment(self, radius, numberOfBS = 36):
        d_x = math.sqrt(3) / 2 * radius
        d_y = radius / 2
        H_hex = 2 * radius
        W_hex = radius * math.sqrt(3)
        self.constraintAreaMaxX = 6.5 * W_hex
        self.constraintAreaMaxY = 3 * H_hex + 3.5 * radius
        for i in range(0, numberOfBS):
            bs = BS()
            bs.ID = i
            bs.turnedOn = True

        numberOfRows = 3
        numberOfColumns = 4
        multiplier = 12

        for row_number in range(0, numberOfRows):
            for column_number  in range(0, numberOfColumns):
                for sector_nb in range(0, 3):
                    self.parent.bs[multiplier*row_number + 3*column_number + sector_nb].x = (3*(column_number+1)-1) * d_x
                    self.parent.bs[multiplier*row_number + 3*column_number + sector_nb].y = (1 + row_number) * H_hex - d_y + row_number * radius
                    self.parent.bs[multiplier*row_number + 3*column_number + sector_nb].angle = sector_nb * 120
                    if column_number % 2 == 1:
                        self.parent.bs[multiplier*row_number + 3*column_number + sector_nb].x = (3*(column_number+1)-1) * d_x
                        self.parent.bs[multiplier*row_number + 3*column_number + sector_nb].y += d_y
                        self.parent.bs[multiplier*row_number + 3*column_number + sector_nb].angle += 60



    def insertURrandomly(self, numberOfDevices):
        number = 0
        for i in range(0, numberOfDevices):
            ue = UE()
            ue.ID = number
            ue.x = random.uniform(0,self.parent.constraintAreaMaxX)
            ue.y = random.uniform(0,self.parent.constraintAreaMaxY)
            number = number + 1
            self.parent.ue.append(ue)

    def connectUserToTheBestBS(self):
        for ue in self.ue:
            ue.connectToTheBestBS(self.bs)
            return ue.connetedToBS