

from ant import Ant
from path import Path


class AntColonySystem(object):
    def __init__(self, path : Path, initial_ants : int) -> None:
        self._ants = []
        self._path = path
        self._end = False

        # create a number of initial ants
        for i in range(0,initial_ants):
            self._ants.append(Ant(path.getStartNode(),path.getStopNode()))
    
    def step(self):
        all_reached = True

        for ant in self._ants:
            if (ant.goalReached() == False):
                all_reached = False
        
        if (all_reached == True):
            self._end = True
            return
        
        self._end = False

        for ant in self._ants:
            if (ant.goalReached() == False):
                nextNodes = self._path.getNeighboors(ant.getCurrentNode())
                ant.nextNode(nextNodes)
                #print(ant)
    
    def finished(self):
        return self._end
    
    def updatePheromone(self):
        self._path.updatePheromone(self._ants)
    
    def showSolution(self):
        print("ACS found the following solutions")
        for ant in self._ants:
            print(ant)
        self._path.showGraph()