import sys
import os
import re
import magic
from flask import Flask, request, redirect, url_for

import dp_utils.data_utils as data_utils
from dp_utils.model_utils import read_model, active_learning


app = Flask(__name__)


@app.route("/predict", methods=["GET", "POST"])
def predict():
    '''
        Receive a file or array with keyword: 'data'
    '''
    # Get array with GET method
    if request.method == "GET":
        data = request.args.getlist('data')
        print(f'get data:{data}')
    # Get file with POST method
    elif request.method == "POST":
        file = request.files.get('file')
        if file:
            filename = data_utils.secure_filename(file.filename)
            file.save(os.path.join('files/', filename))
            data = filename

    data = data_utils.process_file(data)

    # res = model.predict(data) # uncomment when use real model
    res = 'result'

    if config['active_learning']:
        active_learning(model, data)

    return f'result:{res}\nconfig:{config}, type: {type(config)}\n type of model: {type(model)}\nrequest.args:{request.args}'


if __name__ == "__main__":
    model, config = read_model()
    app.run(host='127.0.0.1', port=8080)
    '''
        run "tests/test_receive.py" when app.py is working to test file sharing
        result: miyagi.mp3 and testfile.txt in "files/"
    '''
