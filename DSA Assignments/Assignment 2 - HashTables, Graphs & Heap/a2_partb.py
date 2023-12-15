#    Main Author(s): Dev Soni
#    Main Reviewer(s): Sarah Haque

# uncomment the following lines of code if you wish to make use of the linked list or hash table
# in your solution as appropriate
from a1_partb import DoublyLinked
# from a2_parta import HashTable


class Graph:
    def __init__(self, number_of_verts):
        # Initialize the graph with a specified number of vertices.
        # Each vertex is represented by a DoublyLinked list.
        self.adj_list = [DoublyLinked() for _ in range(number_of_verts)]

    def add_vertex(self):
        # Add a new vertex to the graph.
        self.adj_list.append(DoublyLinked())

    def add_edge(self, from_idx, to_idx, weight=1):
        # Add an edge from one vertex to another with a given weight.
        # Returns False if indices are invalid or the edge already exists.
        if from_idx < 0 or to_idx < 0 or from_idx >= len(self.adj_list) or to_idx >= len(self.adj_list):
            return False
        if self.has_edge(from_idx, to_idx):
            return False
        self.adj_list[from_idx].push_back((to_idx, weight))
        return True

    def num_edges(self):
        # Return the total number of edges in the graph.
        return sum(len(lst) for lst in self.adj_list)

    def num_verts(self):
        # Return the total number of vertices in the graph.
        return len(self.adj_list)

    def has_edge(self, from_idx, to_idx):
        # Check if an edge exists between two vertices.
        if from_idx < 0 or to_idx < 0 or from_idx >= len(self.adj_list):
            return False
        current = self.adj_list[from_idx].get_front()
        while current:
            if current.get_data()[0] == to_idx:
                return True
            current = current.get_next()
        return False

    def edge_weight(self, from_idx, to_idx):
        # Return the weight of an edge between two vertices.
        if from_idx < 0 or to_idx < 0 or from_idx >= len(self.adj_list):
            return None
        current = self.adj_list[from_idx].get_front()
        while current:
            if current.get_data()[0] == to_idx:
                return current.get_data()[1]
            current = current.get_next()
        return None

    def get_connected(self, vert):
        # Return all vertices directly connected to a given vertex.
        if vert < 0 or vert >= len(self.adj_list):
            return []
        connected = []
        current = self.adj_list[vert].get_front()
        while current:
            connected.append(current.get_data())
            current = current.get_next()
        return connected
class LabelGraph:
    def __init__(self, vertex_list):
        # Initialize the LabelGraph with a list of vertex names.
        self.vertices = {vertex: DoublyLinked() for vertex in vertex_list}

    def add_vertex(self, vertex_name):
        # Add a vertex with the specified name to the graph.
        if vertex_name not in self.vertices:
            self.vertices[vertex_name] = DoublyLinked()

    def add_edge(self, from_vertex, to_vertex, weight=1):
        # Add an edge between two vertices with a specified weight.
        # Returns False if vertex names are invalid or the edge already exists.
        if from_vertex not in self.vertices or to_vertex not in self.vertices:
            return False
        if self.has_edge(from_vertex, to_vertex):
            return False
        self.vertices[from_vertex].push_back((to_vertex, weight))
        return True

    def num_edges(self):
        # Return the total number of edges in the graph.
        return sum(len(lst) for lst in self.vertices.values())

    def num_verts(self):
        # Return the total number of vertices in the graph.
        return len(self.vertices)

    def get_verts(self):
        # Return a list of all vertex names in the graph.
        return list(self.vertices.keys())

    def has_edge(self, from_vertex, to_vertex):
        # Check if an edge exists between two vertices identified by their names.
        if from_vertex not in self.vertices:
            return False
        current = self.vertices[from_vertex].get_front()
        while current:
            if current.get_data()[0] == to_vertex:
                return True
            current = current.get_next()
        return False

    def edge_weight(self, from_vertex, to_vertex):
        # Return the weight of an edge between two vertices identified by their names.
        if from_vertex not in self.vertices or to_vertex not in self.vertices:
            return None
        current = self.vertices[from_vertex].get_front()
        while current:
            if current.get_data()[0] == to_vertex:
                return current.get_data()[1]
            current = current.get_next()
        return None

    def get_connected(self, from_vertex):
        # Return all vertices directly connected to a given vertex, along with the weights of the connecting edges.
        # The method uses the vertex name to identify the vertex.
        if from_vertex not in self.vertices:
            return []
        connected = []
        current = self.vertices[from_vertex].get_front()
        while current:
            connected.append(current.get_data())  # Each item is a tuple of (vertex name, weight)
            current = current.get_next()
        return connected
