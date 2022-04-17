from ant import Ant
from ant_colony import AntColonySystem
import path

def main():
    p = path.Path(evaporation_rate=0.2)
    p.initRandomGraph(number_of_nodes=24,degree=3)
    p.setStartStop(0,23)
    p.setStartingPheromones(1)
    p.setEdgesLength(1)

    for i in range(0,100):
        acs = AntColonySystem(p,100)
        while(acs.finished() == False):
            acs.step()
        acs.updatePheromone()
        acs.showSolution()
        print(f"Run #{i}")

if __name__ == "__main__":
    main()