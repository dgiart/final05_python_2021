import requests


if __name__ == '__main__':

    req = requests.get('http://127.0.0.1:5000/')
    res = req.content
    print(res)