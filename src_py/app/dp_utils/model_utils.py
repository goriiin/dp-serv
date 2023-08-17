import pickle
import os

PATH_TO_MODELS = input("enter path to models: ")

for root, dirs, files in os.walk(PATH_TO_MODELS):
    for filename in files:
        print(filename)

filename = input("choose a model")

model = PATH_TO_MODELS + filename

def load_model():
    loaded_model = pickle.load(open(model, 'rb'))
    return loaded_model