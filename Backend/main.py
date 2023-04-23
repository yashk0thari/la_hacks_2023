#import functions/classes
from model import create_new_node
from pre_process import data_preprocess
from structure import Graph, Node
from werkzeug.utils import secure_filename
from whisp import run_whisper

#import Relevant libraries
from flask import Flask, request, flash, redirect, url_for, jsonify
from fastapi import FastAPI, HTTPException
import requests
import os

graph = Graph()

# Define App:
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = '/Users/valley/Desktop/External_Finder/Hackathons/la_hacks_2023/Backend/uploads'  # Choose the folder where you want to save the uploaded files.
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Set the maximum allowed file size to 16 MB.
app.config['SECRET_KEY'] = 'your_secret_key'  # Set your secret key for flash messages.

ALLOWED_EXTENSIONS = {'txt', 'wav'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

### Define Routes:
# Home-Page API:
@app.route('/')
def home():
    return "HOME"

@app.route("/user_input", methods = ['POST'])
def process_user_input():
    # if request.method == 'POST':
    #     if 'file' not in request.files:
    #         flash('No file part')
    #         return redirect(request.url)
    #     file = request.files['file']
    #     if file.filename == '':
    #         flash('No selected file')
    #         return redirect(request.url)
    #     if file and allowed_file(file.filename):
    #         filename = secure_filename(file.filename)
    #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #         flash('File uploaded successfully.')
    #         return redirect(url_for('upload_file'))
    # return '''
    # <!doctype html>
    # <title>Upload File</title>
    # <h1>Upload File</h1>
    # <form method=post enctype=multipart/form-data>
    #   <input type=file name=file>
    #   <input type=submit value=Upload>
    # </form>
    # '''
    if request.method == 'POST':
        if 'fileName' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files['fileName']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            if (".wav" in filename):
                text = run_whisper("/Users/valley/Desktop/External_Finder/Hackathons/la_hacks_2023/Backend/uploads/" + filename)

                payload = {"text": text}

                response = requests.get(f"http://127.0.0.1:8080/graph_object/", params = payload)
            if (".txt" in filename):
                with open("/Users/valley/Desktop/External_Finder/Hackathons/la_hacks_2023/Backend/uploads/" + filename) as f:
                    text = ""
                    for i in f.readlines():
                        text += i + ". "

                    payload = {"text": text}
                    response = requests.get(f"http://127.0.0.1:8080/graph_object/", params = payload)

            return jsonify({"success": "File uploaded successfully."}), 200
    return '''
    <!doctype html>
    <title>Upload File</title>
    <h1>Upload File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route("/graph_object/", methods = ['GET'])
def process_graph_object():
    text = request.args.get("text")
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