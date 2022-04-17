from ant import Ant
from ant_colony import AntColonySystem
import path

def main():
    p = path.Path(evaporation_rate=0.2)
    p.initRandomGraph()
    p.setStartStop()
    p.setStartingPheromones(1)
    p.setRandomEdgesLength(1,5)

    acs = AntColonySystem(p,10)
    while(acs.finished() == False):
        acs.step()
        # acs.showSolution()
    acs.updatePheromone()

    acs = AntColonySystem(p, 10)

    while(acs.finished() == False):
        acs.step()
    acs.updatePheromone()

    acs = AntColonySystem(p, 10)

    while(acs.finished() == False):
        acs.step()
    acs.updatePheromone()

    acs.showSolution()

if __name__ == "__main__":
    main()