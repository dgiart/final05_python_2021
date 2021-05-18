import requests
import socket

if __name__ == '__main__':
    to_post = {'x': 100}
    req = requests.post('http://127.0.0.1:5000', data='', json=to_post)
    # req = requests.get('http://{}:8000'.format(socket.gethostbyname(socket.gethostname())))
    # res = req.content
    # print(res)
    # headers = req.headers
    # print(f'headers: {headers}')
    # for header in headers:
    #     print(header)

