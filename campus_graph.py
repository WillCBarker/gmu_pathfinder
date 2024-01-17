from node import Node
import heapq

class CampusGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node.name not in self.nodes:
            self.nodes[node.name] = node
    
    def get_node(self, node_name):
        try:
            node = self.nodes[node_name]
            return node
        except KeyError:
            return "Node not present in graph"
    
    def add_edge(self, source, destination, weight=1):
        print(source)
        self.nodes[source.name].add_neighbor((destination, weight))
        self.nodes[destination.name].add_neighbor((source, weight))

    def __repr__(self):
        return str(self.nodes)
    
    def dijkstra(self, start, destination):
        distances = {node_name: float('infinity') for node_name in self.nodes}
        distances[start.name] = 0
        priority_queue = [(0, start.name)]
        previous_nodes = {node_name: None for node_name in self.nodes}

        while priority_queue:
            current_distance, current_node_name = heapq.heappop(priority_queue)

            if current_node_name == destination.name:
                return self._build_path(start.name, destination.name, previous_nodes)

            current_node = self.nodes[current_node_name]

            for neighbor_node, edge_weight in current_node.get_neighbors():
                neighbor_name = neighbor_node.name
                distance = current_distance + edge_weight

                if distance < distances[neighbor_name]:
                    distances[neighbor_name] = distance
                    previous_nodes[neighbor_name] = current_node_name
                    heapq.heappush(priority_queue, (distance, neighbor_name))

        return []

    def _build_path(self, start, destination, previous_nodes):
        path = []
        current_node_name = destination

        while current_node_name is not None:
            path.insert(0, current_node_name)
            current_node_name = previous_nodes[current_node_name]

        if path[0] == start:
            return path
        else:
            return []  # No path found
