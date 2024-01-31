import configparser
from configparser import ConfigParser

config=configparser.ConfigParser()
config.read(".\\Configurations\\config.ini")
# config.

class Readconfig:
    @staticmethod
    def getApplicattionUrl():
        url=config.get('common info','baseurl')
        return url

    @staticmethod
    def getUsername():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getpassword():
        password=config.get('common info','password')
        return password
