import time
import bank.jpbank
import bank.mufj


if __name__ == '__main__':
    try:
        jpbank = bank.jpbank.JPBANK()
        jpbank.login()
        balance = jpbank.get_balance()
        print('jpbank balance = ', jpbank.balance)

    finally:
        jpbank.driver.quit()

    try:
        mufj = bank.mufj.MUFJ()
        mufj.login()
        # time.sleep(3)
        balance = mufj.get_balance()
        print('mufj balance = ', mufj.balance)
        
    finally:
        mufj.driver.quit()