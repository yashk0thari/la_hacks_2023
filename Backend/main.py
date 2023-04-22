from flask import Flask, request, make_response, redirect
import model
import os

# Define App:
app = Flask(__name__)

### Define Routes:
# Home-Page API:
@app.route('/')
def home():
    return "HOME"

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