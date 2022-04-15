from tracemalloc import start


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
        probabilities = {}
        for node in nextNodes:
            # compute the probability
            if (node not in self._path_taken):
                if (denominator != 0):
                    # denominator is 0 at first run
                    probabilities[node] = nextNodes[node]['pheromone']/nextNodes[node]['length']/denominator
                else:
                    probabilities[node] = 0
            else:
                # if node was not already taken
                probabilities[node] = 0

        node_with_highest_prob = 0
        highest_probability = 0

        for node in probabilities:
            if (probabilities[node] >= highest_probability):
                highest_probability = probabilities[node]
                node_with_highest_prob = node
        
        # at the end the next node to be chosen is found and I add to my path

        self._path_taken.append(node_with_highest_prob)
        if (node_with_highest_prob == self._stopNode):
            self._reached = True
            print("Reached my goal")

        print(f"New node is {node_with_highest_prob}")
        # update traveled distance
        self._tourLength += nextNodes[node_with_highest_prob]['length']

    def getPath(self):
        return self._path_taken

    def goalReached(self):
        return self._reached
    
    # return the amount of pheromone the ant has to deposit after
    #it completed a travel
    def getPheromone(self):
        if (self._reached == True):
            return 1/self._tourLength
        else:
            return 0
    
    def __str__(self) -> str:
        tmp_str = "Ant traveled nodes: " + str(self._path_taken()) + "\n"
        tmp_str += "Traveled distance: " + str(self._tourLength)
        tmp_str += "Reached: " + str(self.-_reached)

        return tmp_str
