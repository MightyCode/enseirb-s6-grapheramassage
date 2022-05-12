import commerce

def christophides(start: dict, graph: list, points: list, wastes_count: int) -> list:
    """
        @return Graph
    """
    def compute_minimum_spanning_tree(graph: list) -> list:
        result : list = []
        for i in range(len(graph)):
            result[i] = []

        neighbors : list = graph[0]

        while len(neighbors) > 0:
            min_distance = -1
            vSrc = 0
            vDst = 0
            for n in neighbors:
                for v in range(len(result)):
                    if n in graph[v]:
                        d = commerce.dist(points[v], points[n])
                        if min_distance == -1 or min_distance > d:
                            min_distance = d
                            vSrc = v
                            vDst = n
            result[v] = result[v] + [n]
            neighbors[n] = graph[n]

        return result
    
    spanning_tree = compute_minimum_spanning_tree(graph)

    odd_graph = compute_odd_degree_graph(spanning_tree)

    minimal_coupling_graph = compute_minimal_coupling_graph(odd_graph)

    union = union_graph(spanning_tree, minimal_coupling_graph)

    cycle = eulerian_cycle(union)

    return remove_multiple_vertices(cycle)



"""
    @return Graph
"""
def compute_odd_degree_graph(graph: list) -> list:
    result : list = []

    odd: list = []

    for i in range(len(graph)):
        if len(graph[i]) % 2 == 1:
            odd.append(i)

    for i in range(len(graph)):
        result.append([])

        if i in odd:
            for j in odd:
                if i != j:
                    result[i].append(j)

    return result

"""
    @return Graph
"""
def compute_minimal_coupling_graph(graph: list) -> list:
    result : list = []
    return result

"""
    @return Graph
"""
def union_graph(graph1: list, graph2: list) -> list:
    result : list = []
    return result

"""
    @parap Graph

    @return Cycle such as : [ 1, 2, 3, 1, 4, 5, 1 ]
"""
def eulerian_cycle(graph) -> list:
    result : list = []
    return result

"""
    @param Cycle such as : [ 1, 2, 3, 1, 4, 5, 1 ]

    @return Cycle such as : [ 1, 2, 3, 4, 5, 1 ]
"""
def remove_multiple_vertices(cycle: list) -> list:
    result : list = []
    for i in range(0, len(cycle)-1):
        if cycle[i] not in result:
            result = result + [cycle[i]]
    return result + [cycle[0]]


if __name__ == "__main__":
    # Test odd 
    print(compute_odd_degree_graph([[2], [2], [0, 1, 3, 4], [2], [2]]))
    print(remove_multiple_vertices([ 1, 2, 3, 1, 4, 5, 1 ]))
