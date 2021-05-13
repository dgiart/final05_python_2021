import requests


if __name__ == '__main__':
    to_post = {'id': '', 'name': 'research', 'num': 10}
    req = requests.post('http://127.0.0.1:5000/', data=to_post)
    # res = req.content
    # header = req.headers
    # print(header['content-type'])