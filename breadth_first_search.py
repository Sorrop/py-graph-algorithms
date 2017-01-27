class breadth_first_search:
    '''
    Callable class that is instantiated on a graph.
    Performs the classic breadth first traversal.
    '''

    def __init__(self, G):
        '''
        Constructor of the class
               [state]: mapping from vertices to a state that can
                        be 'unexplored', 'exploring' and 'explored'.
               [has_cycle]: boolean to indicate if the algorithm
                            discovered that the graph has a cycle
                [queue]: a list that we manipulate as a queue that holds the
                         unexplored neighbors of each node
               [breadth_traversal]: a list that that holds the edges
                        of the resulting breadth first traversal (DFS tree)
        '''
        self.state = {vertex: 'unexplored' for vertex in G.vertices()}
        self.has_cycle = False
        self.queue = []
        self.breadth_traversal = []

    def __call__(self, G, start):
        '''
        Put the start vertex' unexplored neighbors into the [queue]
        and the corresponding edges into the [breadth_traversal list].
        As long as the queue is not empty, pop the first neighbor and
        do as above.
        '''
        self.queue.append(start)
        self.state[start] = 'exploring'
        while self.queue:
            vertex = self.queue.pop(0)
            self.state[vertex] = 'explored'
            for edge in G.incident_edges(vertex):
                neighbor = edge.opposite(vertex)
                if self.state[neighbor] == 'unexplored':
                    self.breadth_traversal.append(edge)
                    self.queue.append(neighbor)
                    self.state[neighbor] = 'exploring'
                else:
                    if self.state[neighbor] == 'exploring':
                        self.has_cycle = True
