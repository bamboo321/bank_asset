import configparser
from selenium import webdriver

class Account:
    def __init__(self, inikey) -> None:
        self.balance = 0

        s = configparser.ConfigParser()
        s.read('../secret/config.ini')

        c = configparser.ConfigParser()
        c.read('../ini/config.ini')

        self.secret = s[inikey]
        self.config = c
        
        
    def login(self):
        pass

    def get_balance(self):
        pass