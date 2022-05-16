import configparser
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By

import inquiry


class JPBANK(inquiry.Account):
    inikey = 'jpbank'

    def __init__(self) -> None:
        super().__init__(__class__.inikey)
        self.driver = webdriver.Remote(
            command_executor=self.config['SELENIUM']['RemoteAddress'],
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.driver.implicitly_wait(5)
        
        
    def login(self):
        self.driver.get('https://direct.jp-bank.japanpost.jp/direct_login.html?link_id=ycDctLgn')

        # IDとパスワードの入力
        id1 = self.driver.find_element(By.NAME, 'okyakusamaBangou1')
        id2 = self.driver.find_element(By.NAME, 'okyakusamaBangou2')
        id3 = self.driver.find_element(By.NAME, 'okyakusamaBangou3')

        id1.send_keys(self.secret['User'][:4])
        id2.send_keys(self.secret['User'][4:8])
        id3.send_keys(self.secret['User'][8:])
        
        # 次へボタン
        self.driver.find_element(By.NAME, 'U010103').click()
        
        passwd = self.driver.find_element(By.NAME, 'loginPassword')
        passwd.send_keys(self.secret['Password'])
        
        # ログインボタン
        self.driver.find_element(By.NAME, 'U010302').click()

        # ダイレクトトップボタン
        self.driver.find_element(By.XPATH, '//*[@id="strMain"]/p[6]/a').click()
        
        
    def get_balance(self):
        balance = self.driver.find_element(By.XPATH, '//*[@id="strMain"]/div[3]/div/div[2]/p/span')
        self.balance = int(balance.text.replace(',', ''))
        return self.balance
    


# if __name__ == '__main__':
#     try:
#         jpbank = JPBANK()
#         jpbank.login()
#     finally:
#         jpbank.driver.quit()