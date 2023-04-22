# Import Relavent Libraries:
import json
import random
import math
import numpy as np
import os
import openai
import nltk
import cohere
import re
nltk.download('punkt')

#define API Key and cohere client
API_KEY = "1g4kF4R2RpuNTB3ehW1tRWW4QMh3pbF8zgdJGSl8"
co = cohere.Client(API_KEY)

#Testing-Arjun
test_sentences= []
def data_preprocess(word_chunks: str):
  sentences = nltk.sent_tokenize(word_chunks)
  for sentence in sentences:
    test_sentences.append(sentence)
    # print(sentence)  

test_string = """
I need you to help me build a knowledge graph. I have some text from a presentation, and I want you to map that out from a basic idea (the root node) to more specific things about this idea. I also want you to assume the person who wrote this text isn't fully informed, so you must insert your own ideas into this as you please. Give me a graph representation in text form. Here is the text:

Okay, so I was thinking about this hackathon idea to help people keep their attention. You know how it's so hard to stay focused nowadays with all the distractions around us? Well, I was thinking about creating an app that uses gamification to keep people engaged. Like, maybe we could have different levels where users have to complete certain tasks or challenges to progress. And the tasks could be related to things like productivity or mindfulness. For example, completing a certain number of Pomodoros could move you up a level, or doing a guided meditation could give you bonus points. We could also incorporate social accountability, so users can compete with friends or colleagues and see each other's progress. I think it could be really helpful for people who struggle with staying on task, and it could be a fun way to make productivity more enjoyable. What do you think?
"""
data_preprocess(test_string)

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

    def get_nodes_dict_json(self):
        values = self.node_dict.values()
        json_nodes = []
        for val in values:
            json_nodes.append(val.to_json())
        return json_nodes

        

# def create_new_node():
#     for node in Graph 

def create_embedding(text):
  text[0] = text[0].replace("/n", "")
  return co.embed(text).embeddings

def calculate_similarity(node_a, node_b):
    if (node_a is None or node_b is None):
        return 0;
    return np.dot(node_a, node_b) / (np.linalg.norm(node_a) * np.linalg.norm(node_b))

def generate_keyword_from_sentence(sentence: str):
  prompt = """
    Extract a descriptive keyword that gives the core idea of this sentence: \n\n\
    Example Sentence: Black-on-black ware is a 20th- and 21st-century pottery tradition developed by the Puebloan Native American ceramic artists in Northern New Mexico.\n\
    Example keyword: Puebloan Pottery\n\,
    Sentence: 
    """ + sentence + ". Keyword: \n"

  response = co.generate(prompt, model = "xlarge", 
        max_tokens=10,
        temperature=0.2,
        frequency_penalty=0.8,
        presence_penalty=0.0,
        p = 0
).generations[0].text
  return response


#Testing-Arjun
print(generate_keyword_from_sentence("Harry Potter used a brilliant spell with his wand to defeat voldemort"))
print("similarity score: " + str(calculate_similarity(create_embedding(test_sentences[:1])[0], create_embedding(test_sentences[1:2])[0])))
create_embedding(test_sentences[:1])

# Testing:
x = Node("1AJX3s", "What is this shit I'm feeling", "Feeling Shit", ["1AXCc3"], ["6TrQaz", "Ll12Az"], 2, 12.3, [0.2]*1024, 134, 34)
# print(x.to_json())

y = Graph("x86-64")
y.create_node("1AJX3s", "What is this shit I'm feeling", "Feeling Shit", ["1AXCc3"], ["6TrQaz", "Ll12Az"], 2, 12.3, [0.2]*1024, 134, 34)

# print(">> ", y.get_node("1AJX3s").to_json())
y.get_node("1AJX3s").set_x_coord(69.69)
# print(">> ", y.get_node("1AJX3s").to_json())

print(y.get_nodes_dict_json())