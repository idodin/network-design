import itertools


class Edge(object):

    # Constructor For Object
    def __init__(self, vertex_1, vertex_2, cost, reliability):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
        self.cost = cost
        self.reliability = reliability

    # Representation (What gets returned when we do print(my_edge))
    def __repr__(self):
        return '\n<Endpoints: {},\n Cost: {},\n Reliability: {}>\n'.format(
            "[" + self.vertex_1 + ", " + self.vertex_2 + "]",
            self.cost,
            self.reliability)

    @staticmethod
    def get_cost(edge):
        return edge.cost

    @staticmethod
    def get_reliability(edge):
        return edge.reliability


class Graph(object):

    def __init__(self, cities, edges, adj=None):
        self.vertices = cities.copy()
        self.edges = edges.copy()
        self.adj = adj or self.construct_adj(edges)
        for c in cities:
            if c not in self.adj:
                raise Exception
        if not self.is_connected():
            raise Exception

    @staticmethod
    def construct_adj(edges):
        adj = dict()

        for e in edges:
            if e.vertex_1 not in adj:
                adj[e.vertex_1] = [e.vertex_2]
            else:
                adj[e.vertex_1].append(e.vertex_2)

            if e.vertex_2 not in adj:
                adj[e.vertex_2] = [e.vertex_1]
            else:
                adj[e.vertex_2].append(e.vertex_1)

        return adj

    def is_connected(self):
        visited = {vertex: False for vertex in self.vertices}

        stack = list()

        stack.append(self.vertices[0])

        while len(stack):
            me = stack[-1]
            stack.pop()

            if not visited[me]:
                visited[me] = True

            for neighbour in self.adj[me]:
                if not visited[neighbour]:
                    stack.append(neighbour)

        total_visited = [1 for (vertex, state) in visited.items() if state]

        return len(total_visited) == len(self.vertices)

    def compute_reliability(self):
        # All possible subsets of edges
        selections = itertools.product(range(2), repeat=len(self.edges))
        edge_subsets = [[e for (e, s) in zip(self.edges, sel) if s == 1] for sel in selections]

        # All possible subset of edges such that graph remains connected
        sub_graphs = list()
        for subset in edge_subsets:
            try:
                sub_graphs.append(Graph(self.vertices, subset))
            except Exception as e:
                continue

        total_rel = 0

        for graph in sub_graphs:
            sub_graph_rel = 1
            for e in graph.edges:
                sub_graph_rel *= e.reliability
            for e in [x for x in self.edges if x not in graph.edges]:
                sub_graph_rel *= (1 - e.reliability)
            total_rel += sub_graph_rel

        return total_rel

    def compute_max_reliability(self, cost_constraint):
        # All possible subsets of edges
        selections = itertools.product(range(2), repeat=len(self.edges))
        edge_subsets = [[e for (e, s) in zip(self.edges, sel) if s == 1] for sel in selections]

        # All possible subset of edges such that graph remains connected and satisfy constraint
        sub_graphs = list()
        for subset in edge_subsets:
            subset_cost = sum([e.cost for e in subset])
            if subset_cost <= cost_constraint:
                try:
                    sub_graphs.append(Graph(self.vertices, subset))
                except Exception as e:
                    continue

        max_rel = 0
        max_graph = None
        for graph in sub_graphs:
            curr_rel = graph.compute_reliability()
            if curr_rel > max_rel:
                max_rel = curr_rel
                max_graph = graph

        return max_graph

    def compute_cost(self):
        return sum([e.cost for e in self.edges])
