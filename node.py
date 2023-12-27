class Node:
    def __init__(self, name, node_type, parent_building = set()):
        self.name = name
        self.node_type = node_type
        self.parent_building = parent_building
        self.neighbors = []
    
    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
    
    def get_neighbors(self):
        return self.neighbors