"""
cashed property, polymorphism, method override, Cashed property
"""
from functools import cached_property, lru_cache
import requests


#cashed property


class MyComputer:  # curl is Узнать свой ip можно у сайта curl icanhazip.com или "http://ifconfig.co"
    def __init__(self):
        self._external_ip = None

    @property
    def external_ip(self):
        if self._external_ip is None:
            result = requests.get("http://ifconfig.co", headers={"User-agent": "curl"})
            self._external_ip = result.text.strip()
        return self._external_ip
    """
    Для того чтобы реализовать эту функциог=нальность придумали @cashed_property 
    для этого нужно сделать import: from functools import cashed_property
    он только один раз запускает и достает результат после сохраняет его в кэш и при дальнейшей 
    выполнении программы достает результат оттуда
    """
    @cached_property
    def ip(self):
        ip = requests.get("http://ifconfig.co", headers={"User-agent": "curl"})
        return ip.text.strip()



p = MyComputer()
print(p.ip)
