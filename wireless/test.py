from network import CellularNetwork

network = CellularNetwork()
network.Generator.createHexagonalBSdeployment(1666,numberOfBS=36)


network.Generator.insertURrandomly(300)
network.connectUserToTheBestBS()

network.getSINR()
