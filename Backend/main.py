#import functions/classes
from model import create_new_node
from pre_process import data_preprocess
from structure import Graph, Node

#import Relevant libraries
from flask import Flask, request, make_response, redirect
from fastapi import FastAPI, HTTPException
import os

graph = Graph()

# Define App:
app = Flask(__name__)

### Define Routes:
# Home-Page API:
@app.route('/')
def home():
    return "HOME"

@app.route("/user_input", methods = ['POST'])
def process_user_input():
    


@app.route("/graph_object", methods = ['GET'])
def process_graph_object(text: str):
    text_senteces = data_preprocess(text)
    for sentence in text_sentences:
        if (sentence == ""):
            raise HTTPException(status_code=404, detail="Sentence cannot be null.")
        create_new_node(sentence, graph)
    return graph.to_json()

@app.route('/post/initial_file', methods = ['POST'])
def init_file():

    audio_file = request.files['audio']

    # TODO: Add transcription code + Inital File Handling 

    return 'Received (POST) init_file request!'


@app.route('/post/graph/<string:graphID>')
def postGraph(graphID):
    
    # TODO: Generate Graph + Nodes
    return

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))