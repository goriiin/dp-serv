import requests

if __name__ == '__main__':
    url = 'http://127.0.0.1:8080/predict'
    r = requests.get(url, params={'data': [1, 2, 3], 'arr': [1, 2, 3]})
    print(r.text)

    files = {'file': open('test_files/testfile.txt', 'rb')}
    r = requests.post(url, files=files)
    print(r.text)

    files = {'file': open('test_files/miyagi.mp3', 'rb')}
    r = requests.post(url, files=files)
    print(r.text)
