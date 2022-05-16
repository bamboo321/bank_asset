import configparser
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import inquiry


class MUFJ(inquiry.Account):
    inikey = 'mufj'

    def __init__(self) -> None:
        super().__init__(__class__.inikey)

        self.driver = webdriver.Remote(
            command_executor=self.config['SELENIUM']['RemoteAddress'],
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.driver.implicitly_wait(5)
        

    def login(self):
        self.driver.get('https://entry11.bk.mufg.jp/ibg/dfw/APLIN/loginib/login?_TRANID=AA000_001&link_id=kojin_top_direct_login_kizon')
        
        # IDとパスワードの入力
        id = self.driver.find_element(By.NAME, 'KEIYAKU_NO')
        passwd = self.driver.find_element(By.NAME, 'PASSWORD')
        
        id.send_keys(self.secret['User'])
        passwd.send_keys(self.secret['Password'])

        # ログインボタン
        self.driver.find_element(By.XPATH, '/html/body/div[1]/main/form/section/div/div/div[1]/div[3]/div/button').click()

    
    def get_balance(self):
        time.sleep(3)
        balance = self.driver.find_element(By.XPATH, '/html/body/div/main/form/section/div/div[1]/div/div[2]/section[1]/a/div[1]/div[3]/span[1]')
        self.balance = int(balance.text.replace(',', ''))
        return self.balance