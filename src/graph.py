"""A gragh data structure."""


class Graph(object):
    """Graph."""

    def __init__(self):
        """Create the dictionary that will be the graph."""
        self.g = {}

    def nodes(self):
        """Return a list of all the nodes in the graph."""
        nodes = []
        for key in self.g:
            nodes += [key]
        return nodes

    def edges(self):
        """Return a list of all the edges in the graph."""
        edges = []
        for key in self.g:
            for edge in self.g[key]:
                edges += [(key, edge)]
        return edges

    def add_node(self, n):
        """Add a node to the graph."""
        self.g.setdefault(n, [])

    def add_edge(self, n1, n2, weight=1):
        """Add an edge between two nodes."""
        try:
            self.g[n1] += [(n2, weight)]
        except KeyError:
                self.g[n1] = [(n2, weight)]

    def del_node(self, n):
        """Delete a node from the graph."""
        try:
            del self.g[n]
        except KeyError:
            raise KeyError('No node exists.')

    def del_edge(self, n1, n2):
        """Delete the edge between two nodes."""
        try:
            for i in self.g[n1]:
                if i[0] is n2:
                    self.g[n1].remove(i)
                    break
        except ValueError:
            raise ValueError('Edge does not exist.')

    def has_node(self, n):
        """Find a specific node in the graph."""
        return n in self.g

    def neighbors(self, n):
        """Return all the edges for n."""
        try:
            nbrs = []
            for i in self.g[n]:
                nbrs += [i[0]]
            return nbrs
        except KeyError:
            raise KeyError('No node exists.')

    def adjacent(self, n1, n2):
        """Return true if an edge exists between n1 and n2."""
        try:
            list1 = []
            list2 = []
            for i in self.g[n1]:
                list1 += [i[0]]
            for i in self.g[n2]:
                list2 += [i[0]]
            if n1 in list2 or n2 in list1:
                return True
            return False
        except KeyError:
            raise KeyError('No node exists.')

    def depth_first_traversal(self, start):
        """Return a list of nodes based on depth first traversal."""
        start = (start, 0)
        travel = [start]
        depth_list = []
        depth = set()
        while travel:
            edge = travel.pop()[0]
            if edge not in depth:
                travel.extend(self.g[edge][::-1])
                depth_list.append(edge)
                depth.add(edge)
        return depth_list

    def breadth_first_traversal(self, start):
        """Return a list of nodes based on breadth first traversal."""
        start = (start, 0)
        travel = [start]
        depth = []
        while travel:
            edge = travel.pop(0)[0]
            if edge not in depth:
                travel.extend(self.g[edge])
                depth.append(edge)
        return depth

    def distance_graph(self, start, stop):
        V = 4
        INF = 99999
        for i in range(V):
            for j in range(V):
                if(dist[i][j] == INF):
                    print "%7s" %("INF"),
                else:
                    print "%7d\t" %(dist[i][j]),
                if j == V-1:
                    print ""

    def floyd_warshall(self, n, , ):
        """Floyd Warshall formula."""
        V = 4

        dist = map(lambda i : map(lambda j : j , i) , graph)
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    dist[i][j] = min(dist[i][j], dist[i][k]+ dist[k][j]
)

if __name__ == '__main__':

        graph = {'A':{'A':0,'B':6,'C':INF,'D':6,'E':7},

                 'B':{'A':INF,'B':0,'C':5,'D':INF,'E':INF},

                 'C':{'A':INF,'B':INF,'C':0,'D':9,'E':3},

                 'D':{'A':INF,'B':INF,'C':9,'D':0,'E':7},

                 'E':{'A':INF,'B':4,'C':INF,'D':INF,'E':0}

                 }

    floydWarshall(graph)

    import timeit
    print('depth first time: ', timeit.timeit(stmt='g.depth_first_traversal(1)', setup='from test_graph import g_trav; g = g_trav()', number=10000))
    print('breadth first time: ', timeit.timeit(stmt='g.breadth_first_traversal(1)', setup='from test_graph import g_trav; g = g_trav()', number=10000))
