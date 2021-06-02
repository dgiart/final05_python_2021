import requests
import socket
import service.database_funcs

if __name__ == '__main__':
    print(help(requests))

    to_post = {'': 0}
    # data = {'data': 1000}
    req = requests.post('http://127.0.0.1:5000/rest/departments/', json=to_post)
    # resp = req.json()
    # print(resp)
    # req = requests.get('http://{}:8000'.format(socket.gethostbyname(socket.gethostname())))
    # res = req.content
    # print(res)
    # headers = req.headers
    # print(f'headers: {headers}')
    # for header in headers:
    #     print(header)

