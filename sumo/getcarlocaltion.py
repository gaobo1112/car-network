import os
import sys
import optparse
import random

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary
import traci

def run():
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        vehicle_list = traci.vehicle.getIDList()
        for vehicle in vehicle_list:
            speed = traci.vehicle.getSpeed(vehicle)
            print(vehicle, speed)
    traci.close()

if __name__ == "__main__":

    sumoBinary = checkBinary('sumo-gui')
    traci.start([sumoBinary, "-c", "/home/gaobo/sumo-src-1.0.1/sumo-1.0.1/tools/2018-12-24-13-59-21/osm.sumocfg"])
    run()