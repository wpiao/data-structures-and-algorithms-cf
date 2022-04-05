from stack_and_queue.queue import Queue


class Graph:

    def __init__(self):
        # key will be the node, value adj node with a value of the edge
        self.adjacency_list = {}
        self.nodes = []

    def add_node(self, value):
        # Arguments: value
        # Returns: The added node
        # Add a node to the graph or add to adj list
        v = Vertex(value)
        self.nodes.append(v)
        self.adjacency_list[v] = {
            'nodes': [],
            'edges': [] 
        }
        return v

    def add_edge(self, v1, v2, w=1):
        # Arguments: 2 nodes to be connected by the edge, weight (optional)
        # Returns: nothing
        # Adds a new edge between two nodes in the graph
        # If specified, assign a weight to the edge
        # Both nodes should already be in the Graph
        e = Edge(v1, v2, w)
        try:
            self.adjacency_list[v1]['nodes'].append([v2, w])
            self.adjacency_list[v1]['edges'].append(e)
        except Exception:
            print(f'{v1} is not in the graph. Add {v1} to the graph before adding an edge with it.')
        try:
            self.adjacency_list[v2]['nodes'].append([v1, w])
            self.adjacency_list[v2]['edges'].append(e)
        except Exception:
            print(f'{v2} is not in the graph. Add {v2} to the graph before adding an edge with it.')
        

    def get_node(self):
        # Arguments: none
        # Returns all nodes in graph as a collection (set, list, or similar)
        return self.nodes

    def get_neighbor(self, v):
        # Arguments: node
        # Returns a collection of edges connected to the given node
        # Include the weight of connection in returned collection
        try:
            return self.adjacency_list[v]['edges']
        except Exception:
            print(f'Node {v} is not in the graph.')

    def size(self):
        # Arguments: none
        # Returns the total number of nodes in the graph
        return len(self.nodes)

    def breadth_first_search(self, vertex):
        # Arguments: vertex/node
        # Returns a list of vertex in the order they were visited
        nodes_list = []
        q = Queue()
        visited = set()

        q.enqueue(vertex)
        visited.add(vertex)

        while not q.is_empty():
            front = q.dequeue()
            neighbor = self.get_neighbor(front)
            nodes_list.append(front)

            for edge in neighbor:
                if edge.v1 == front:
                    if edge.v2 not in visited:
                        q.enqueue(edge.v2)
                        visited.add(edge.v2)
                else:
                    if edge.v1 not in visited:
                        q.enqueue(edge.v1)
                        visited.add(edge.v1)
        return nodes_list




class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, v1, v2, weight=1):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight
