import path
import random


class Ant(object):
    def __init__(self, startNode, stopNode) -> None:
        # list of nodes
        self._path_taken = []
        self._startNode = startNode
        self._stopNode = stopNode
        self._reached = False
        self._tourLength = 0
        self._path_taken.append(self._startNode)

    def getCurrentNode(self):
        # return the last element of the list
        return self._path_taken[len(self._path_taken)-1]

    # receives a dictionary with the nodes and their attributes
    def nextNode(self, nextNodes):
        if (self._reached == True):
            # don't do anything if already arrived
            return
        
        denominator = 0
        for node in nextNodes:
            denominator += nextNodes[node]['pheromone']/nextNodes[node]['length']
        # for each node create a probability and choose the highest value
        probabilities = []
        nodes = []
        for node in nextNodes:
            nodes.append(node)
            # compute the probability
            if (node in self._path_taken):
                probabilities.append(0)
            else:
                probabilities.append(nextNodes[node]['pheromone']/nextNodes[node]['length']/denominator)
        
        all_zero = True
        for probability in probabilities:
            if (probability != 0):
                all_zero = False
        if (all_zero == True):
            #assign random probabilities to perform a random choice
            for i in range(0,len(probabilities)):
                probabilities[i] = random.random()

        
        node_with_highest_prob = random.choices(nodes,probabilities,k=1)
        
        #print(f"Nodes: {nodes}\nProbabilities: {probabilities}\nChoosen : {node_with_highest_prob[0]}")
        
        self._path_taken.append(node_with_highest_prob[0])

        if (node_with_highest_prob[0] == self._stopNode):
            self._reached = True

        # update traveled distance
        self._tourLength += nextNodes[node_with_highest_prob[0]]['length']

    def getPath(self):
        return self._path_taken

    def goalReached(self):
        return self._reached
    
    # return the amount of pheromone the ant has to deposit after
    #it completed a travel
    def getPheromone(self):
        if (self._reached == True):
            return 2/self._tourLength
        else:
            return 0
    
    def edgePassed(self,nodeA,nodeB):
        for i in range(0,len(self._path_taken)-1):
            if (self._path_taken[i] == nodeA and self._path_taken[i+1] == nodeB):
                # if the edge correspond then return the pheromone of the ant
                # print(f"Pheromone: {self.getPheromone()}")
                return self.getPheromone()
        
        return 0

    
    def __str__(self) -> str:
        tmp_str = "\n===================================================\n"
        tmp_str += "Ant traveled nodes: " + str(self._path_taken) + "\n"
        tmp_str += "Traveled distance: " + str(self._tourLength) + "\n"
        tmp_str += "Reached: " + str(self._reached)
        tmp_str += "\n===================================================\n"
        return tmp_str