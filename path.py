from platform import node
from random import randint, random
import networkx as nx
import matplotlib.pyplot as plt


class Path(object):
    def __init__(self,evaporation_rate = 0) -> None:
        # create an empty graph
        self._graph = nx.Graph()
        self._evaporationRate = evaporation_rate
        self._photogram_count = 0
    
    def initRandomGraph(self,number_of_nodes,degree):
        # create a random graph
        self._graph = nx.random_regular_graph(d=degree, n=number_of_nodes)
        self._layout = nx.shell_layout(self._graph)
    
    def setStartingPheromones(self, value):
        for n in self._graph:
            for e in self._graph[n]:
                self._graph[n][e]['pheromone'] = value
        
        pass

    def setRandomEdgesLength(self,min,max):
        for n in self._graph:
            for e in self._graph[n]:
                self._graph[n][e]['length'] = randint(min,max)
    
    def setEdgesLength(self, length):
        for n in self._graph:
            for e in self._graph[n]:
                self._graph[n][e]['length'] = length
        

    #return the pheromone for the edge between nodeA and nodeB
    def getPheromone(self,nodeA,nodeB):
        return self._graph[nodeA][nodeB]['pheromone']    

    def _setStartNode(self):
        self._startnode = randint(0,self._graph.number_of_nodes()-1)
    
    def _setArrivalNode(self):
        self._stopnode = randint(0,self._graph.number_of_nodes())-1
        while (self._stopnode == self._startnode):
            # avoid selecting the same node both for starting and stopping
            self._stopnode = randint(0,self._graph.number_of_nodes()-1)
    
    def setStartStop(self,startNode = None, stopNode = None):
        if (startNode is None):
            self._setStartNode()
        else:
            self._startnode = startNode
        if (stopNode is None):
            self._setArrivalNode()
        else:
            self._stopnode = stopNode
        print(f"Start node: {self._startnode}, Stop node: {self._stopnode}")
    
    def showGraph(self):
        # draw the rest of the graph
        nx.draw_networkx_nodes(self._graph,self._layout,node_size=2000/len(self._graph.nodes),node_color='#1f78b4')
        # draw the starting node
        nx.draw_networkx_nodes(self._graph,self._layout,node_size=3000/len(self._graph.nodes),nodelist=[self._startnode],node_color="#1BC700")
        # draw the ending node
        nx.draw_networkx_nodes(self._graph,self._layout,node_size=3000/len(self._graph.nodes),nodelist=[self._stopnode],node_color='tab:orange')
        # draw the edges
        for edge in self._graph.edges:
            edge_width = 1+ int(self._graph[edge[0]][edge[1]]['pheromone'])
            nx.draw_networkx_edges(self._graph, self._layout,edgelist = [edge], alpha=1, width=edge_width)
        # draw labels for nodes
        labels = {}
        for node in self._graph:
            labels[node] = str(node)
        
        nx.draw_networkx_labels(self._graph,self._layout,labels)
        # draw labels for edges
        #nx.draw_networkx_edge_labels(self._graph,layout,font_size = 5)

        # plt.show()
        plt.savefig(f"photogram/pic{self._photogram_count}.png",dpi=500)
        self._photogram_count += 1
    
    def getStartNode(self):
        return self._startnode
    
    def getStopNode(self):
        return self._stopnode

    # returns a dictionary with neighboor nodes
    def getNeighboors(self, node):
        return self._graph.adj[node]
    
    def updatePheromone(self,ants):
        for edge in self._graph.edges:
            # calculate the sum of pheromones for all ants
            sum_of_pheromones = 0
            for ant in ants:
                sum_of_pheromones += ant.edgePassed(edge[0],edge[1])
            self._graph[edge[0]][edge[1]]['pheromone'] = self._graph[edge[0]][edge[1]]['pheromone']*(1-self._evaporationRate) + sum_of_pheromones

    def __str__(self) -> str:
        tmp_str = "The graph is made of the following nodes\n"
        for node in self._graph:
            tmp_str += str(self._graph[node])

        return tmp_str