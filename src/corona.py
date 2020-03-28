import requests
import re

class Covid19:

    def __init__(self):
        self.__endpoint = "https://www.worldometers.info"

    def getdata(self, country=None):
        if country is None:
            self.country = "/coronavirus/"
        else:
            self.country = "/coronavirus/country/" + country + "/"

        r =requests.get(self.__endpoint  + self.country)
        return self.getMid(r.text)

    def getMid(self, str):
        self.str = str
        result = {}
        case = re.findall(r'<span style="color:#aaa">(.*?) </span>', self.str)
        result['cases'] = case[0]
        dr = re.findall(r'<span>(.*?)</span>', self.str)
        result['deaths'] = dr[0]
        result['recovered'] = dr[1]
        return result
