import graph
from depth_first_search import depth_first_search
from breadth_first_search import breadth_first_search

edges = [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 6),
         (2, 7), (3, 8), (3, 9), (4, 10), (4, 11)]
G, _ = graph.create_graph(edges)

start_vertex = G.get_vertex(0)
breadth = breadth_first_search(G)
breadth(G, start_vertex)

depth = depth_first_search(G)
depth(G, start_vertex)

print('Undirected Case.')
print(edges)
print('                             ')
print('==============================')
print('Breadth First traversal of G')
for edge in breadth.breadth_traversal:
    print((edge.endPoints()[0].element(), edge.endPoints()[1].element()))
print('==============================')
print('Depth First traversal of G')
for edge in depth.depth_traversal:
    print((edge.endPoints()[0].element(), edge.endPoints()[1].element()))

print('                             ')
print('==============================')
print('==============================')
print('                             ')

edges = [('a', 'b'), ('c', 'a'), ('c', 'b'),
         ('d', 'c'), ('d', 'e'), ('b', 'e')]

G, _ = graph.create_graph(edges, True)
start_vertex = G.get_vertex('a')
breadth = breadth_first_search(G)
breadth(G, start_vertex)

depth = depth_first_search(G)
depth(G, start_vertex)
print('Directed Case.')
print(edges)
print('                             ')
print('==============================')
print('Breadth First traversal of G')
for edge in breadth.breadth_traversal:
    print((edge.endPoints()[0].element(), edge.endPoints()[1].element()))
print('==============================')
print('Depth First traversal of G')
for edge in depth.depth_traversal:
    print((edge.endPoints()[0].element(), edge.endPoints()[1].element()))
