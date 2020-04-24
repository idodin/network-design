class Edge(object):

    # Constructor For Object
    def __init__(self, vertex_1, vertex_2, cost, reliability):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
        self.cost = cost
        self.reliability = reliability

    # Representation (What gets returned when we do print(my_edge))
    def __repr__(self):
        return 'endpoints: {}, cost: {}, reliability: {} \n'.format(self.vertex_1 + "<->" + self.vertex_2,
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
        self.vertices = cities
        self.edges = edges
        self.adj = adj or self.construct_adj(edges)

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