from flask import Flask, request, redirect, url_for
# jsonify, abort, make_response, request, send_file)

# import requests
# import json
# import time
# import sys
# import pandas as pd

# import dp_utils.pic_utils as pic
# import dp_utils.audio_utils as audio
import dp_utils.data_utils as data_utils
import dp_utils.model_utils as model
# import dp_utils.np_utils as np
# import dp_utils.predict_utils as predict
# import dp_utils.video_utils as video


app = Flask(__name__)


# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     '''
#         Receive a file or array with keyword: 'data'
#     '''
#     if request.method == 'POST':
#         file = request.files.get('file')
#         if file:
#             mimetype = file.content_type
#             print(f'mime:{mimetype}')
#             # filename = werkzeug.secure_filename(file.filename)
#             # file.save(os.path.join(UPLOAD_FOLDER, filename))
#
#             return redirect(url_for('/upload'))
#         else:
#             data = request.args.get('data')
#             print(f'get data:{data}')
#             return redirect(url_for('/upload'))


@app.route("/predict", methods=["GET", "POST"])
def predict():
    # Если запрос - GET, то вернуть приветственное сообщение
    if request.method == "GET":
        data = request.args.get('data')
        print(f'get data:{data}')
        return redirect(url_for('/predict'))

    # Если запрос - POST, то обработать файл с данными
    if request.method == "POST":
        file = request.files.get('file')
        if file:
            mimetype = file.content_type
            print(f'mime:{mimetype}')
            # filename = werkzeug.secure_filename(file.filename)
            # file.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect(url_for('/upload'))
        # Получить файл из запроса

        # Отправить файл на вход скрипту-обработчику
        data = data_utils.process_file(file)

        # Сделать предсказание с помощью модели
        res = model.predict(data)

        # Вернуть результат в виде JSON
        return res.to_json()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
