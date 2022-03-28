class Graph:
    def __init__(self, vertices):
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.V = vertices

    def is_safe(self, v, pos, path):
        if self.graph[path[pos - 1]][v] == 0:
            return False

        for vertex in path:
            if vertex == v:
                return False

        return True

    # A recursive utility function to solve Hamiltonian cycle problem
     
    def ham_cycle_until(self, path, pos):

            # base case: if all vertices are included in the path
            if pos == self.V:
                # Last vertex must be adjacent to the first vertex in path to make a cycle
                if self.graph[path[pos - 1]][path[0]] == 1:
                    return True
                else:
                    return False

            for v in range(1, self.V):

                if self.is_safe(v, pos, path) is True:

                    path[pos] = v

                    if self.ham_cycle_until(path, pos + 1) is True:
                        return True

                # Remove current vertex if it doesn't lead to a solution
                    path[pos] = -1

            return False

    def ham_cycle(self):
        path = [-1] * self.V

        path[0] = 0

        if self.ham_cycle_until(path, 1) is False:
            print("Solution does not exist\n")
            return False

        self.print_solution(path)
        return True

    def print_solution(self, path):
        print("Solution Exists: Following is one Hamiltonian Cycle")
        for vertex in path:
            print(vertex, end=" ")
        print(path[0], "\n")


''' Let us create the following graph
    (0)--(1)--(2)
    | / \\ |
    | / \\ |
    | /     \\ |
    (3)-------(4) '''
g1 = Graph(5)
g1.graph = [[0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
            [0, 1, 0, 0, 1, ], [1, 1, 0, 0, 1],
            [0, 1, 1, 1, 0], ]
g1.ham_cycle()

''' Let us create the following graph
    (0)--(1)--(2)
    | / \\ |
    | / \\ |
    | /     \\ |
    (3)     (4) '''
g2 = Graph(5)
g2.graph = [[0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
            [0, 1, 0, 0, 1, ], [1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0], ]

# Print the solution
g2.ham_cycle()
