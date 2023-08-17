from flask import Flask
                   #jsonify, abort, make_response, request, send_file)

# import requests
# import json
# import time
# import sys
# import pandas as pd

import dp_utils.pic


app = Flask(__name__)


@app.route('/')
def audio():
    return dp_utils.pic.upload_pic()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)