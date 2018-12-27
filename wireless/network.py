import copy
from wireless import devices
from wireless import generator
import numpy as np
import random

class CellularNetwork:
    def __init__(self):
        self.ue = []
        self.bs = []
        self.Generator = generator.Generator(self)
        self.constraintAreaMaxX = []
        self.constraintAreaMaxY = []
        self.radius = []
        self.bandwidth = 10.e6
        self.powerofbs = 20




    def addOneBSTower(self, x_pos, y_pos):
        # for i in range(3):
        bs = devices.BS()
        bs.x = x_pos
        bs.y = y_pos
        self.bs.append(copy.deepcopy(bs))


    def connectUserToTheBestBS(self):
        for ue in self.ue:
            ue.connectToTheBestBS(self.bs)

    def reset(self):
        b = []
        for ue in self.ue:
            for bs in self.bs:
                a = ue.distanceToBS(bs)
                b.append(a)
        return np.array(b)

    def render(self):
        pass

    def step(self,action):
        self.ue[0].connetedToBS = (action-1)//16
        self.ue[1].connetedToBS = ((action-1)//4)%4
        self.ue[2].connetedToBS = (action - 1)%4
        reward = 0
        observation_ = []
        done = False
        for ue in self.ue:
            a = -(ue.distanceToBS(self.bs[ue.connetedToBS])/self.bandwidth)
            reward += a
            ue.x += random.uniform(-50,50)
            if ue.x >self.constraintAreaMaxX or ue.x < 0:
                done = True
            ue.y += random.uniform(-50,50)
            if ue.y >self.constraintAreaMaxY or ue.y < 0:
                done = True
            for bs in self.bs:
                distance = ue.distanceToBS(bs)
                observation_.append(distance)
        return np.array(observation_), reward, done



# Environment: consider the wireless vehicular network, where a 2-tier wireless network is included.
# For a cell, a macro and several road side base stations are deployed in the environment.
# Vehicle with UE can move around the environment.
# Due to the mobility of UE, it needs to associate with the BSs while the association
# controller needs to consider its transmission demand as well as the possible handoffs.
#
#
#
# State: for each UE, position, speed(direction), transmission demand(down-link),
#
# Action: 0-1 vector for BS association, and the corresponding bandwidth allocation
#
# Reward: time to complete transmission task.
# However, for UE has no transmission task or just little task in terms of transmission volume,
# how do we handle this scenario? Or just long-term transmission rate?
# We can define the long-term task transmission rate to represent the reward.
