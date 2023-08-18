from flask import Flask, request, redirect, url_for
# jsonify, abort, make_response, request, send_file)

# import requests
# import json
# import time
# import sys
# import pandas as pd

import dp_utils.pic
import dp_utils.audio
import dp_utils.data_utils
import dp_utils.model_utils
import dp_utils.np
import dp_utils.predict_utils
import dp_utils.video


app = Flask(__name__)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    '''
        Receive a file or array with keyword: 'data'
    '''
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            mimetype = file.content_type
            print(f'mime:{mimetype}')
            # filename = werkzeug.secure_filename(file.filename)
            # file.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect(url_for('/upload'))
        else:
            data = request.args.get('data')
            print(f'get data:{data}')
            return redirect(url_for('/upload'))


@app.route('/upload')
def upload():
    return dp_utils.pic.upload_pic()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
