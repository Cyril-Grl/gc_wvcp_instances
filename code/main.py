"""Main module."""

from representation.solution import Solution
from representation.graph import load_graph


def main() -> None:
    """main function"""
    with open("../instance_list.txt", "r") as f:
        for instance in f.readlines():
            inst = instance[:-1:]
            print(inst)
            sol = Solution(load_graph(inst))
            sol.reduction()
            print()


if __name__ == "__main__":
    main()
