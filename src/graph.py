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

    def edges(self, start=None):
        """Return a list of all the edges in the graph."""
        edges = []
        for key in self.g:
            for edge in self.g[key]:
                edges += [(key, edge)]
        return edges

    def add_node(self, n):
        """Add a node to the graph."""
        if n in self.nodes():
            raise ValueError('Node already in graph.')
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
        """looking for the distance."""
        v = 4
        INF = 99999
        for i in range(v):
            for j in range(v):
                if(stop[i][j] == INF):
                    print "%7s" %("INF"),
                else:
                    print "%7d\t" %(stop[i][j]),
                if j == v-1:
                    print ""

graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]]

    def warshall(self, start, finish):
        """Floyd Warshall formula."""
        v = 4
        dist = map(lambda i: map(lambda j: j, i), self)
        for k in range(v):
                for i in range(v):
                    for j in range(v):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    def dijkstra(self, start, finish):
        """Dijkstra shortest path algorithm."""
        if self._path(start, finish):
            visited = {start: 0}
            path = {}
            nodes = set(self.breadth_first_traversal(start))
            while nodes:
                min_node = None
                for node in nodes:
                    if node in visited:
                        if min_node is None:
                            min_node = node
                        elif visited[node] < visited[min_node]:
                            min_node = node
                    if min_node is None:
                        break
                nodes.remove(min_node)
                curr_distance = visited[min_node]
                for edge in self._edges_for_node(min_node):
                    distance = curr_distance + edge[1][1]
                    # print(distance, ' = ', curr_distance, ' + ', edge[1][1])
                    if edge[1][0] not in visited or distance < visited[edge[1][0]]:
                        visited[edge[1][0]] = distance
                        path[edge[1][0]] = min_node
            return self._return_path(path, start, finish)
        raise ValueError('No such path.')

    def _path(self, n1, n2):
        """If there a path from n1 to n2 return True."""
        path = self.breadth_first_traversal(n1)
        if n2 in path:
            return True
        return False

    def _edges_for_node(self, n1):
        edges = []
        for edge in self.edges():
            if edge[0] is n1:
                edges += [edge]
        return edges

    def _return_path(self, path, start, finish):
        """Turn the path list into a compleate path."""
        node = finish
        full_path = []
        while node is not start:
            full_path += [node]
            node = path[node]
        return [start] + full_path[::-1]


if __name__ == '__main__':

    import timeit

print('depth first time: ', timeit.timeit(stmt='g.depth_first_traversal(1)', setup='from test_graph import g_trav; g = g_trav()', number=10000))
print('breadth first time: ', timeit.timeit(stmt='g.breadth_first_traversal(1)', setup='from test_graph import g_trav; g = g_trav()', number=10000))
