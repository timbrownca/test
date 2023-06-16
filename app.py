import os
import json
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


@app.route('/chat_history', methods=['POST'])
def get_chat_history():
    # if "user" not in session:
    #     return redirect(url_for('login'))
    
    # user = session["user"]
    # get all chat sessions for the user, sorted by date, grouped by today, this week, this month, older
    chat_history = [
        {"session_id": 12345, "config": {}, "history":[], "label": "chat session 1"},
        {"session_id": 23456, "config": {}, "history":[], "label": "chat session 2"}
        ]
    print(f"Fetched the following chat history:\n{json.dumps(chat_history)}")
    return { "status": "success", "history": chat_history }


# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
