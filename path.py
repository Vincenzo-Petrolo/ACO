from random import randint, random
import networkx as nx
import matplotlib.pyplot as plt


class Path(object):
    def __init__(self) -> None:
        # create an empty graph
        self._graph = nx.Graph()
    
    def initRandomGraph(self):
        # create a random graph
        self._graph = nx.barabasi_albert_graph(randint(10,20),randint(1,5))
    
    def setStartingPheromones(self, value):
        for n in self._graph:
            for e in self._graph[n]:
                self._graph[n][e]['pheromone'] = value
        
        pass

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
    
    def setStartStop(self):
        self._setStartNode()
        self._setArrivalNode()
        print(f"Start node: {self._startnode}, Stop node: {self._stopnode}")
    
    def showGraph(self):
        # get a unique layout
        layout = nx.circular_layout(self._graph)
        # draw the rest of the graph
        nx.draw_networkx_nodes(self._graph,layout,node_size=200,node_color='#1f78b4')
        # draw the starting node
        nx.draw_networkx_nodes(self._graph,layout,node_size=300,nodelist=[self._startnode],node_color="#1BC700")
        # draw the ending node
        nx.draw_networkx_nodes(self._graph,layout,node_size=300,nodelist=[self._stopnode],node_color='tab:orange')
        # draw the edges
        nx.draw_networkx_edges(self._graph, layout, alpha=1, width=1)
        plt.show()