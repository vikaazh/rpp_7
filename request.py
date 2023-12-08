import requests
import time


def req(url):
    for i in range(2405, 3486):
        forma = {
            'email': str(f'{"test"}{i}@{"gmail.com"}'),
            'password': i,
        }
        response = requests.post(url, data=forma)

        if response.status_code == 429:
            time.sleep(60)
        if response.status_code == 200:
            return forma


if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/login'
    req(url)
