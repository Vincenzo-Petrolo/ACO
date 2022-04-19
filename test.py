from secrets import randbelow

from numpy import number
from ant import Ant
from ant_colony import AntColonySystem
import path
import random

def main():
    number_of_nodes = 16
    p = path.Path(evaporation_rate=0.5)
    p.initRandomGraph(number_of_nodes=number_of_nodes,degree=2)
    p.setStartStop(0,random.randint(1,number_of_nodes-1))
    p.setStartingPheromones(1)
    p.setEdgesLength(1)
    p.showGraph()
    starting_ants = 50
    for i in range(0,starting_ants):
        acs = AntColonySystem(p,starting_ants)
        while(acs.finished() == False):
            acs.step()
        acs.updatePheromone()
        acs.showSolution()
        print(f"Run #{i}")

if __name__ == "__main__":
    main()