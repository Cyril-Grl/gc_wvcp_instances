"""
Class graph
"""
from typing import List, Tuple


class Graph:
    """Representation of a graph"""

    def __init__(
        self,
        name: str,
        nb_vertices: int,
        nb_edges: int,
        edges_list: List[Tuple[int, int]],
        weights: List[int],
    ):
        self.name: str = name
        self.nb_vertices: int = nb_vertices
        self.nb_edges: int = nb_edges
        self.weights = weights
        self.adjacency_matrix = [
            [False for _ in range(nb_vertices)] for _ in range(nb_vertices)
        ]
        self.edges_list: List[Tuple[int, int]] = edges_list
        self.neighborhood: List[List[int]] = [[] for _ in range(nb_vertices)]
        for vertex1, vertex2 in edges_list:
            if not self.adjacency_matrix[vertex1][vertex2]:
                self.adjacency_matrix[vertex1][vertex2] = True
                self.adjacency_matrix[vertex2][vertex1] = True
                self.neighborhood[vertex1].append(vertex2)
                self.neighborhood[vertex2].append(vertex1)
        self.degree: List[int] = [
            len(self.neighborhood[vertex]) for vertex in range(nb_vertices)
        ]

    def __repr__(self):
        return (
            f"File : {self.name}\n"
            f"Nb nodes : {self.nb_vertices}\n"
            f"Nb edges : {self.nb_edges}\n"
            f"Weights : {self.weights}\n"
        )


def load_graph(instance_name: str) -> Graph:
    """
    Load graph file

    :param instance_name: name of the graph
    :return: graph from the file
    """
    with open(f"../wvcp/{instance_name}.edgelist", "r") as file:
        edges_list: List[Tuple[int, int]] = []
        nb_edges: int = 0
        nb_vertices: int = 0
        for line in file.readlines():
            vertex1, vertex2 = sorted(list(map(int, line.split())))
            nb_edges += 1
            nb_vertices = max(nb_vertices, vertex1, vertex2)
            edges_list.append((vertex1, vertex2))
        nb_vertices += 1
    with open(f"../wvcp/{instance_name}.col.w", "r") as file:
        weights = list(map(int, file.readlines()))
    return Graph(instance_name, nb_vertices, nb_edges, edges_list, weights)


# max_clique
