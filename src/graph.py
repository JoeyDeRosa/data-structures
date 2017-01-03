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

    def add_edge(self, n1, n2):
        """Add an edge between two nodes."""
        try:
            self.g[n1] += [n2]
        except KeyError:
                self.g[n1] = [n2]

    def del_node(self, n):
        """Delete a node from the graph."""
        try:
            del self.g[n]
        except KeyError:
            raise KeyError('No node exists.')

    def del_edge(self, n1, n2):
        """Delete the edge between two nodes."""
        try:
            self.g[n1].remove(n2)
        except ValueError:
            raise ValueError('Edge does not exist.')

    def has_node(self, n):
        """Find a specific node in the graph."""
        return n in self.g

    def neighbors(self, n):
        """Return all the edges for n."""
        try:
            return self.g[n]
        except KeyError:
            raise KeyError('No node exists.')

    def adjacent(self, n1, n2):
        """Return true if an edge exists between n1 and n2."""
        try:
            if n1 in self.g[n2] or n2 in self.g[n1]:
                return True
            return False
        except KeyError:
            raise KeyError('No node exists.')

    def depth_first_traversal(self, start):
        depth = set()
        travel = [start]
        return_list = []
        while travel:
            edge = travel.pop()
            if edge not in depth:
                depth.add(edge)
                travel.extend(self.g[edge][::-1])
                return_list.append(edge)
        return return_list

    def breadth_first_traversal(self, start):
        """Return a list of nodes based on breadth first traversal."""
        depth = []
        travel = [start]
        while travel:
            edge = travel[0]
            travel.remove(edge)
            if edge not in depth:
                depth.append(edge)
                travel.extend(self.g[edge])
        return depth
