from flask import Flask, jsonify, abort, make_response, request, send_file
import requests
import json
import time
import sys
import pandas as pd


import sys
sys.path.append("utils/pic.py")

from utils import pic


app = Flask(__name__)


@app.route('/image')
upload_file()





if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)