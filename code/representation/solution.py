"""
Representation of a Solution for graph coloring problem
"""

from typing import List

from representation.graph import Graph


class Solution:
    """Representation of a solution"""

    def __init__(self, graph: Graph):
        self.graph: Graph = graph
        self.free_vertices: List[int] = []
        self.reduced_vertices: List[int] = []
        self.list_free_vertices: List[int] = []

    def reduction(self) -> None:
        """
        Apply the reduction algorithm to delete useless vertices

        :return: None
        """
        self.compute_reduction()
        print(f"{len(self.reduced_vertices)} vertices deleted")
        self.list_free_vertices = sorted([
            v for v in range(self.graph.nb_vertices) if v not in self.reduced_vertices
        ], key=lambda v: (self.graph.weights[v], self.graph.degree[v]))
        print("second reduction")
        reduc_n2 = []
        reduc_v2 = []
        for vertex in self.list_free_vertices:
            if vertex in reduc_v2:
                continue
            neighbors = [
                self.graph.neighborhood[n]
                for n in self.graph.neighborhood[vertex]
                if n not in self.reduced_vertices
            ]
            if neighbors:
                inter = set(neighbors[0]).intersection(*neighbors)
                inter.remove(vertex)
                inter = inter.difference(self.reduced_vertices)
                if inter:
                    for v in inter:
                        if self.graph.weights[v] > self.graph.weights[vertex] or (
                            self.graph.weights[v] == self.graph.weights[vertex]
                            and vertex < v
                        ):
                            reduc_n2.append(f"{vertex} {v}")
                            reduc_v2.append(v)
                            self.reduced_vertices.append(vertex)
                            break
        print(f"{len(reduc_n2)} vertices deleted")
        with open(f"reduction_n2/{self.graph.name}.txt", "w") as f:
            for line in reduc_n2:
                f.write(f"{line}\n")

    def compute_reduction(self) -> None:
        """
        Search for less important vertices in the graph (with few neighbors and low weight)

        :return: None
        """
        print("first reduction")
        cliques: List[List[int]] = []
        # load cliques
        with open(f"../cliques/{self.graph.name}.txt", "r") as file:
            for line in file.readlines():
                cliques.append(
                    sorted(  # sort the vertices in the clique per weight
                        list(map(int, line.split())),
                        key=lambda v: self.graph.weights[v],
                        reverse=True,
                    )
                )
        if not cliques:
            return
        # sort the cliques per total weight
        cliques = sorted(
            cliques,
            key=lambda clique: sum([self.graph.weights[v] for v in clique]),
        )
        # Size largest clique
        size_clique_max = max([len(clique) for clique in cliques])
        # print(f"{len(cliques)},{size_clique_max},", end="")
        for vertex in range(self.graph.nb_vertices):
            vertex_degree: int = self.graph.degree[vertex]
            # if its degree is lower than the size of the largest clique
            if vertex_degree < size_clique_max:
                # if its weight is lower than the weight of any
                # vertex of all cliques in the column of its degree
                if self.graph.weights[vertex] < max(
                    [
                        self.graph.weights[clique[vertex_degree]]
                        for clique in cliques
                        if len(clique) > vertex_degree
                    ]
                ):
                    # the vertex can be deleted
                    self.reduced_vertices.append(vertex)
        self.reduced_vertices.sort(
            key=lambda v: (
                self.graph.weights[v],
                self.graph.degree[v],
            ),
            reverse=True,
        )
        with open(f"reduction_cliques/{self.graph.name}.txt", "w") as f:
            for vertex in self.reduced_vertices:
                f.write(f"{vertex}\n")
