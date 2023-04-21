import sys

from collections import defaultdict


def is_two_colorable(edge_list: list[list[str]]) -> bool:
    """Determines if the given graph is two-colorable.

    The graph is specified as a list of edges, where each edge is a list
    of two vertices.  The result will be True if the given graph is two
    colorable, and False otherwise.

    Args:
        edge_list: the graph to analyze, given as a list of edges

    Returns:
        True if the given graph is two-colorable, False otherwise
    """
    adj_list = defaultdict(list)
    clr_list = defaultdict(int)

    for edge in edge_list:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])
        clr_list[edge[0]]
        clr_list[edge[1]]

    vertices = list(clr_list.keys())
    for vertex in vertices:
        if clr_list[vertex] == 0:
            is_tc = df_search(vertex, adj_list, clr_list)
            if not is_tc:
                return False

    return True


def df_search(start: str, adj_list: dict,
              clr_list: dict, color: int = 1) -> tuple[bool, dict]:
    """Determines if the given component of the graph is two-colorable via a
    recursive depth-first search. Also mutates/updates the color table.

    Args:
        start: the name of the starting vertex
        adj_list: adjacency hash table for the vertices
        clr_list: color hash table for the vertices
        color: color to be assigned to the starting vertex (1 or 2)

    Returns:
        True if the given component is two-colorable, False otherwise.
    """
    clr_list[start] = color
    is_tc = True
    for vertex in adj_list[start]:
        if clr_list[vertex] == 0:
            if color == 1:
                is_v_tc = df_search(vertex, adj_list, clr_list, 2)
            elif color == 2:
                is_v_tc = df_search(vertex, adj_list, clr_list, 1)
            is_tc = is_tc and is_v_tc
        elif clr_list[vertex] == color:
            return False

    return is_tc


def main(argv: list[str]) -> None:
    if len(argv) != 2:
        print('usage: python3 two_colorable.py <filename>', file=sys.stderr)
        sys.exit(1)

    with open(argv[1]) as file:
        edge_list = [line.split() for line in file]

    print(is_two_colorable(edge_list))


if __name__ == '__main__':
    main(sys.argv)
