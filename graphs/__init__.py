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

    def find_mst(self, f, reversal=False):
        self.edges = sorted(self.edges, key=f, reverse=reversal)
        dsu = DSU(self.vertices)

        selected_vertices = self.vertices.copy()
        selected_edges = []
        for e in self.edges:
            color_1 = dsu.find(e.vertex_1)
            color_2 = dsu.find(e.vertex_2)

            if color_1 != color_2:
                selected_edges.append(e)
                dsu.union(color_1, color_2)

        return Graph(selected_vertices, selected_edges)


class DSU(object):

    def __init__(self, nodes):
        self.parent = {n: n for n in nodes}
        self.rank = {n: 0 for n in nodes}

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def union(self, x, y):
        x_rep = self.find(x)
        y_rep = self.find(y)

        if self.rank[x_rep] < self.rank[y_rep]:
            self.parent[x_rep] = y_rep
        elif self.rank[x_rep] > self.rank[y_rep]:
            self.parent[y_rep] = x_rep
        else:
            self.parent[y_rep] = x_rep
            self.rank[x_rep] += 1
