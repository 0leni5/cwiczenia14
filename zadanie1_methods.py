import urllib as url
import requests as rq

class urlFun:
    def __init__(self):
        pass

    def getImage(self, url, filename):
        response = rq.get(url)
        print(rq.headers)
        print(rq.content[:500])

        if response.status_code == 200:
            content = response.text
        else:
            return False

        with open(os.path.join('data', filename), 'wb') as file:
            file.write(response.content)

        return True
