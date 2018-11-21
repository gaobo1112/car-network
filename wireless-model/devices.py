import math

class NetworkDevice:
    def __init__(self):
        self.x = 0
        self.y = 0

#定义用户
class UE(NetworkDevice):
    def __init__(self):
        self.ID = 0
        self.connetedToBS = 0
        self.inside = True

    def distanceToBS(self, BS):
        return math.sqrt((self.x-BS.x)**2+(self.y-BS.y)**2)

    def isSeenFromBS(self,BS):
        a_y = BS.y - self.y
        distance_bs_ue = self.distanceToBS(BS)
        if distance_bs_ue == 0 or BS.turnedOn == False:
            return False
        return True

    def connectToNearestBS(self, BS_vector):
        closestDistance = self.distanceToBS(BS_vector[0])
        foundBS = -1
        for bs in BS_vector:
            currentDistance = self.distanceToBS(bs)
            if currentDistance < closestDistance:
                closestDistance = currentDistance
                foundBS = bs.ID
        self.connetedToBS = foundBS

# 定义基站
class BS(NetworkDevice):
    def __init__(self):
        self.ID = 0
        self.sendPower = 0
        self.x = 0
        self.y = 0
