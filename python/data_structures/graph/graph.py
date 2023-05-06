class Graph:
    """
    Non-Linear data structure. Collection of Vertices (Nodes) connected by Edges

    """

    def __init__(self):
        self.adjacency_list = {}


    def add_node(self, value):
        """
        add vertex
        Arguments: value
        Add a vertx to the graph
        :return: added vertex/node
        """
        new_vertex = Vertex(value)
        self.adjacency_list[new_vertex] = []
        return new_vertex


    def add_edge(self, vertex1, vertex2, weight=1):
        """
        add edge
        Arguments: 2 vertex to be connected by the edge, weight (optional)
        Returns: nothing
        Adds a new edge between two vertex in the graph
        If specified, assign a weight to the edge
        Both vertex should already be in the Graph
        :return:
        """
        if vertex1 not in self.adjacency_list:
            self.add_node(vertex1)
        if vertex2 not in self.adjacency_list:
            self.add_node(vertex2)

        self.adjacency_list[vertex1].append(Edge(vertex2, weight))
        self.adjacency_list[vertex2].append(Edge(vertex1, weight))


    def get_nodes(self):
        """
        Arguments: none
        Returns all of the nodes in the graph as a collection (set, list, or similar)
        Empty collection returned if there are no nodes
        :return: All nodes in graph as list
        """
        return list(self.adjacency_list.keys())


    def get_neighbors(self, vertex):
        """
        Arguments: node
        Returns a collection of edges connected to the given node
        Include the weight of the connection in the returned collection
        Empty collection returned if there are no nodes
        :return: Collection of edges connected to node
        """
        if vertex in self.adjacency_list:
            return self.adjacency_list[vertex]
        else:
            return None


    def size(self):
        """
        Arguments: none
        Returns the total number of nodes in the graph
        0 if there are none
        :return: Integer representing the size of graph
        """
        return len(self.adjacency_list)


class Vertex:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight

    def __str__(self):
        return self.weight
