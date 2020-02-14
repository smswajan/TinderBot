from selenium import webdriver
from time import sleep


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(2)

        #we will log in through phone
        phone_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[1]/button')
        phone_btn.click()

        phone_in = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input')
        phone_in.send_keys('#your phone number')

        continue_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
        continue_btn.click()

        #getting verification code via sms
        vf_key = int(input('Verification Key: '))
        a = 0
        while a < 6:
            num = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[3]/input[{0}]'.a+1)
            num.send_keys('{}'.vf_key[a])
            a = a + 1

        continue_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
        continue_btn.click()


        #location settings
        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        #notification settings
        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(2)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = TinderBot()
bot.login()