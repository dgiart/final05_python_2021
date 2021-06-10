import  requests


if __name__ == '__main__':
    url1 = 'http://127.0.0.1:5000/'
    url2 = 'http://iert.kharkov.ua'
    req = requests.get(url1)
    resp = req.text
    # json = req.json()
    print(f'resp: {resp}')
    # print(f'json: {json}')