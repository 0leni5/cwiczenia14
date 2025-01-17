from zadanie1_methods import urlFun as uf
import requests as rq

def main():
    url = "https://www.if.pw.edu.pl/~meteo/warszawapw/tempt.jpg"
    filename = "test_temperatura.jpg"
    print(uf.getImage(url, filename))



if __name__ == "__main__":
    main()