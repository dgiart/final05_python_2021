import requests


if __name__ == '__main__':
    to_post = {name: 'jon', birth: 1980, salary: 2000}
    req = requests.post('http://127.0.0.1:5000/employees', data=to_post)
    # req = requests.get('http://127.0.0.1:5000/employees')
    # res = req.content
    # print(res)
    # header = req.headers
    # print(header['content-type'])
