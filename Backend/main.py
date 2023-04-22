#import functions/classes
from model import create_new_node
from pre_process import data_preprocess
from structure import Graph, Node

#import Relevant libraries
from flask import Flask, request, make_response, redirect, url_for
from flask_cors import CORS
from fastapi import FastAPI, HTTPException
import requests
import os



graph = Graph()

# Define App:
app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

### Define Routes:
# Home-Page API:
@app.route('/')
def home():
    return "HOME"

@app.route("/user_input", methods = ['POST'])
def process_user_input():
    if request.method == "POST":
        user_text = request.json['text']


        # Generate the URL for the target endpoint
        response = requests.get(f"http://127.0.0.1/graph_object/{user_text}")

        # # Make an HTTP request to the target endpoint
        # response = requests.get(endpoint2_url)
    return response.content

@app.route("/graph_object/<string:text>", methods = ['GET'])
def process_graph_object(text):
    text_sentences = data_preprocess(text)
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