from itertools import chain, combinations
from graphs import Graph


def power_set(iterable):
    """
    Generates an iterable for the powerset of the input iterable
    Found at:
    https://stackoverflow.com/questions/41626379/python-power-set-of-a-list
    :param iterable: Iterable to generate a powerset from
    :return: Power set iterable
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def match_edges(edge, edge_list):
    for e in edge_list:
        endpoints = [e.vertex_1, e.vertex_2]
        if edge.vertex_1 in endpoints and edge.vertex_2 in endpoints:
            return True

    return False


def enhance_cost(complete, mst, cost_constraint):
    cost_left = cost_constraint - mst.compute_cost()
    if cost_left < 0:
        return None

    missing = [e for e in complete.edges if not match_edges(e, mst.edges)]

    possible_enhancements = filter(lambda x: cost_of_subset(x) < cost_left and len(x) > 0, list(power_set(missing)))
    max_rel = mst.compute_reliability()
    max_graph = mst
    for edge_list in possible_enhancements:
        enhanced_edges = mst.edges.copy()
        enhanced_edges.extend(list(edge_list))
        enhanced = Graph(complete.vertices, enhanced_edges)
        enhanced_rel = enhanced.compute_reliability()
        if enhanced_rel > max_rel:
            max_rel = enhanced_rel
            max_graph = enhanced

    return max_graph


def cost_of_subset(subset):
    return sum([e.cost for e in subset])