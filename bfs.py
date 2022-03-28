import collections

graph = {'a' : ['b', 'c'],
         'b' : ['a', 'd'],
         'c' : ['a', 'd'],
         'd' : ['b', 'c', 'e'],
         'e' : ['d']
         }  #In this dictionary key use as a node and values as the edges.

def bfs(g, root):
    queue = collections.deque([root])
    visited = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)

        for item in g[node]:
            if item not in visited:
                queue.append(item)

    print(visited)


bfs(graph, 'e')
