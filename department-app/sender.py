import requests
import socket

if __name__ == '__main__':

    to_post = {'y': 100}
    # data = {'data': 1000}
    req = requests.post('http://127.0.0.1:5000', data=to_post) #, json=to_post)
    # req = requests.get('http://{}:8000'.format(socket.gethostbyname(socket.gethostname())))
    # res = req.content
    # print(res)
    # headers = req.headers
    # print(f'headers: {headers}')
    # for header in headers:
    #     print(header)

