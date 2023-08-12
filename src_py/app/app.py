from flask import Flask, request, jsonify

import requests


session = requests.Session()
response = session.get("http://localhost:8080/")


app = Flask(__name__)

# @app.route("/", methods=["POST"])
# def post():
#     pass
#
#
# @app.route("/", methods=["GET"])
# def get():
#     pass


print(response)
if __name__ == '__main__':
    app.run()

