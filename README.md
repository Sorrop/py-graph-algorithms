# py-graph-algorithms

<h3><b>Various graph algorithms implemented in python</b></h3>

This is a repo loaded with various classic algorithms on graphs implememented in python (reinventing the wheel for practice).


<h2>graph.py</h2>

Contains the class <code>Graph()</code> that represent a graph object with support for directed or undirected ones. There you can find nested classes <code>graph.Node()</code> and <code>graph.Edge()</code> that represent a graph's vertex and edge. These classes are made hashable in order to implement adjacency relations between vertices using adjacency map. Each instantiated graph object has a private dictionary <code>self._outgoing</code> with keys being vertices. For each vertex u the value of <code>self._outgoing[u]</code> is another (singular) dict with key the adjacent vertex v and value the corresponding edge between u and v.

This data structure to represent adjacency is heavily based on the one that is presented in the book *Data Structures and Algorithms in Python* by M.T.Goodrich, R.Tamassia and M.H.Goldwasser. It is extended with other methods like one for retrieving an iterator on graph's vertices and others for deleting a vertex/edge. There is also a helper method  <code>graph.create_graph()</code> that can be used to instantiate a graph object from a simple list of tuples represenation of the edges of graph.

Example usage<br>
<code>E=[('a','b'),('b','c'),('c','a')]</code><br>
<code>G, weight_mapping = graph.create_graph(E)</code>
<br>

This method takes also as input a keyword argument [is_directed] which defaults to False to indicate if the graph is directed or not. The output is the graph object and a mapping of each edge to corresponding edge weight. If no weights are given then the mapping values default to 1.


<h2>breadth_first_traversal.py and depth_first_traversal.py</h2>

Callable classes that implement classic breadth-first and depth-first search correspondigly. Both work for directed or undirected graphs and in the latter case the depth-first callable can compute the topological ordering of the vertices (or else return an indication that there is a cycle). The depth-first callable also computes the timestamps of the algorithms arrival and departure in each vertex which can be used to determine if the graph has certain characteristic (for example if it has an odd length cycle).

<h2>kruskal.py</h2>

Classic algorithm of kruskal that computes a minimum spanning tree for a given undirected weighted graph. The algorithm proceeds with sorting the edges by weight and building the tree on the fly as it scans the sorted edges. If it connects an edge that breaks the tree, it removes it and continues until the number of vertices of tree becomes equal with the input graph's one.

<h2>bellman_ford.py</h2>

Classic dynamic programming approach to finding the shortest paths from a given vertex to any other vertex of a directed graph. The function returns a distance mapping of each vertex to its distance (length of the shortest path) from the start vertex and a predecessor mapping of each vertex to each predecessor on the shortest path tree. If the algorithm it detects a negative cycle then it returns None for both outputs.

<h2>dag_shortest_paths.py</h2>

This works only on directed acyclic graphs and computes the shortest paths from a start_vertex by obtainingthe graph's topological ordering of the vertices. It then proceeds by only relaxing the outgoing edges of each vertex one by one in the topological order. This way the shortest paths are computed in linear time O(n+m).

<h2>dijkstra.py</h2>

Another classic algorithm that computes the shortest paths in directed graphs with non-negative edge weights by proceeding in a breadth-first style and finalizing distances in non-decreasing order. To accomodate this non-decreasing order the algorithm makes use of a priority queue that is implemented in <code>priorityQueue.py</code>. This is a wrapper class of the <code>collections.heapq</code> data structure that is equipped with an <code>entry_finder</code> mapping of each item in the heap and a <code>counter</code> that is used to break ties in the item ordering.

<h2>traversal_tests.py</h2>

Example runs of breadth and depth-first traversals.
