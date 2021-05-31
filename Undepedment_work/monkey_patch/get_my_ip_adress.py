import requests


class GetMyIpAdress:

    def __init__(self, name):
        self.name = name

    def my_ip(self):
        ip_req = requests.request(method='get', url='http://icanhazip.com')
        ip = ip_req.text

        return ip


if __name__ == '__main__':
    my_ip = GetMyIpAdress(name='Azura')
    print(my_ip.my_ip())
