graph = {'A': ['B', 'C', 'D'], 'B': ['E'], 'C': ['D', 'E'], 'D': [], 'E': []}
visited = set()

def dfs(visited, graph, root):
    if root not in visited:
        print(root, end=" ")
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited, graph, neighbour)


if __name__ == '__main__':
    print("Following is Depth First Search Traversal (root vertex is 'A')")
    dfs(visited, graph, 'A')
