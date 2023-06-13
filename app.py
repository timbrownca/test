import os
from flask import Flask, request, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment

app = Flask(__name__, static_folder='build/static', template_folder='build')
CORS(app)


@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.template_folder, 'index.html')


@app.route("/manifest.json")
def manifest():
    return send_from_directory(app.template_folder, 'manifest.json')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.template_folder, 'favicon.ico')


# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
