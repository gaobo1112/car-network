import numpy as np
from wireless_network import CellularNetwork

class Env:
    def __init__(self):
        self.state_size = np.zeros((36,200))
        self.action_size = np.zeros((36,200))



    def reset(self):
        #初始化状态
        network = CellularNetwork()
        network.createHexagonalBSdeployment(1666)
        network.insertURrandomly(200)
        us_vector = network.connectUserToTheBestBS()
        for ue in us_vector:
            self.state_size
        

    
    def step(self,action):
        # 通过当前状态得到下一状态
        pass
