from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    distances = {vertex: float('inf') for vertex in graph}
    edgeCount = {vertex: float('inf') for vertex in graph}
    parents = {vertex: None for vertex in graph}
    
    distances[source] = 0
    edgeCount[source] = 0
    
    queue = deque([source])
    
    while queue:
        current = queue.popleft()
        for neigh, weight in graph[current]:
            newDistance = distances[current] + weight
            if newDistance < distances[neigh] or (newDistance == distances[neigh] and edgeCount[current] + 1 < edgeCount[neigh]):
                distances[neigh] = newDistance
                edgeCount[neigh] = edgeCount[current] + 1
                parents[neigh] = current
                queue.append(neigh)
    
    shortest_paths = {vertex: (distances[vertex], edgeCount[vertex]) for vertex in graph}
    return shortest_paths


        
    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    queue = deque([source])
    parents = {source: None}

    while queue:
        current = queue.popleft()
        for neigh in graph[current]:
            if neigh not in parents:
                parents[neigh] = current
                queue.append(neigh)
    
    return parents

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    path = []
    
    while parents[destination] is not None:
        path.append(parents[destination])
        destination = parents[destination]

    return ''.join(path[::-1])

print(get_sample_graph())