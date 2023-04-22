# Import Relavent Libraries:
import json

# Node Class:
class Node:
    def __init__(self, id, payload, keyword, parents, children, depth, distance, embedding, x_coord, y_coord):
        self.id = id
        self.payload = payload
        self.keyword = keyword
        self.parents = parents
        self.children = children
        self.depth = depth
        self.distance = distance
        self.embedding = embedding
        self.x_coord = x_coord
        self.y_coord = y_coord

    # Getters:
    def get_id(self):
        return self.id
    
    def get_payload(self):
        return self.payload
    
    def get_keyword(self):
        return self.keyword
    
    def get_parents(self):
        return self.parents
    
    def get_children(self):
        return self.children
    
    def get_depth(self):
        return self.depth
    
    def get_distance(self):
        return self.distance
    
    def get_embedding(self):
        return self.embedding
    
    def get_x_coord(self):
        return self.x_coord
    
    def get_y_coord(self):
        return self.y_coord
    
    # Setters:
    def set_payload(self, payload):
        self.payload = payload
        
    def set_keyword(self, keyword):
        self.keyword = keyword
    
    def set_parents(self, parents):
        self.parents = parents
    
    def set_children(self, children):
        self.children = children
    
    def set_depth(self, depth):
        self.depth = depth
    
    def set_distance(self, distance):
        self.distance = distance
    
    def set_embedding(self, embedding):
        self.embedding = embedding
    
    def set_x_coord(self, x_coord):
        self.x_coord = x_coord
    
    def set_y_coord(self, y_coord):
        self.y_coord = y_coord
    
    # Helper methods:
    def add_parent(self, parent_node):
        self.parents.append(parent_node)
    
    def add_child(self, child_node):
        self.children.append(child_node)
    
    def remove_parent(self, parent_node):
        if parent_node in self.parents:
            self.parents.remove(parent_node)
    
    def remove_child(self, child_node):
        if child_node in self.children:
            self.children.remove(child_node)
    
    def is_leaf(self):
        return len(self.children) == 0
    
    def is_root(self):
        return len(self.parents) == 0

    # JSON converter:
    def to_dict(self):
        return {
            'id': self.id,
            'payload': self.payload,
            'keyword': self.keyword,
            'parents': self.parents,
            'children': self.children,
            'depth': self.depth,
            'distance': self.distance,
            'embedding': self.embedding,
            'x_coord': self.x_coord,
            'y_coord': self.y_coord
        }
    
    def to_json(self):
        return json.dumps(self.to_dict())

    # NOTE: Can add simmilarity Function

# Graph Class:
class Graph:
    def __init__(self, id):
        self.id = id
        self.node_dict = {}

    # Helper methods:
    def create_node(self, id, payload, keyword, parents, children, depth, distance, embedding, x_coord, y_coord):
        self.node_dict[id] = Node(id, payload, keyword, parents, children, depth, distance, embedding, x_coord, y_coord)

    def remove_node(self, node_id):
        self.node_dict.pop(node_id)

    def get_node(self, node_id):
        return self.node_dict[node_id]

    
    

# Testing:
x = Node("1AJX3s", "What is this shit I'm feeling", "Feeling Shit", ["1AXCc3"], ["6TrQaz", "Ll12Az"], 2, 12.3, [12, 34, 21.2, 2.23], 134, 34)
print(x.to_json())

y = Graph("x86-64")
y.create_node("1AJX3s", "What is this shit I'm feeling", "Feeling Shit", ["1AXCc3"], ["6TrQaz", "Ll12Az"], 2, 12.3, [12, 34, 21.2, 2.23], 134, 34)

print(">> ", y.get_node("1AJX3s").to_json())
y.get_node("1AJX3s").set_x_coord(69.69)
print(">> ", y.get_node("1AJX3s").to_json())