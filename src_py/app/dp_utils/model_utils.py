import pickle
import os
from . import yaml_utils as ya


def _choose_current_file(paths: list, ch_files: list):
    """
        paths: list of (PATH_TO_CONFIGS, PATH_TO_MODELS)
        chfile: list of (cur_conf, cur_model)
    """
    result = []
    for i in range(len(paths)):
        ch_file = ch_files[i]
        path = os.path.abspath(paths[i])
        print(path)
        if ch_file is None:
            names = []
            for root, dirs, files in os.walk(path):
                for filename in files:
                    names.append(filename)
            names.sort(reverse=True)
            current_file = path + '/' + names[0]
        else:
            # cur_conf либо None, либо название файла
            current_file = path + '/' + ch_file
        result.append(current_file)
    return result


def _load_model(model):
    return pickle.load(open(model, 'rb'))


def read_model(cur_conf=None, cur_model=None):
    """
        !! USE ONLY FROM app.py !!
        cur_conf: None or filename of selected config
        cur_model: None or filename of selected model.
    """
    PATH_TO_CONFIGS = 'config/'
    PATH_TO_MODELS = 'models/'

    config_path, model_path = _choose_current_file([PATH_TO_CONFIGS, PATH_TO_MODELS],
                                                   [cur_conf, cur_model])
    model = _load_model(model_path)
    config = ya.load_config(config_path)
    print('model and config loaded')
    return [model, config]


def active_learning():
    pass


def predict():
    pass
