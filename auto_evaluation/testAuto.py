from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
class Browser():
    def __init__(self,options,browser):
        self.options=options
        self.browser=browser

    def login(self):
        time.sleep(5)
        login_url = 'http://stu.1000phone.net//student.php/public/login'
        browser=self.browser
        browser.get(login_url)
        account = browser.find_element_by_name('Account')
        account.send_keys('')   # 输入账户,   input('账户:')
        password = browser.find_element_by_xpath("//input[@name='PassWord']")
        password.send_keys('666666')  # 输入密码,   input('密码:')

        submit = browser.find_element_by_xpath("//button[@type='submit']")
        submit.click()  # 点击提交按钮

    def enter_evaluation_page(self):
        time.sleep(5)
        browser=self.browser
        memeber_evalu=browser.find_element_by_xpath("//ul[@class='submenu']/li[9]")
        memeber_evalu.click()
        time.sleep(5)
        evaluate_object=browser.find_element_by_xpath("//table[@id='sample-table-2']/tbody//td[3]")
        evaluate_object=evaluate_object.text
        print('{:-^30}'.format('Start Evaluation'))
        print('{:-^30}'.format(evaluate_object))
        time.sleep(5)
        begin_evaluate=browser.find_element_by_xpath("//a[@class='btn btn-xs btn-success']")
        begin_evaluate.click()


    def evaluate(self):
        time.sleep(5)
        browser = self.browser
        first_choice = browser.find_elements_by_xpath("//tbody[@id='topic']/tr//td[3]/label[1]")
        try:
            for i in first_choice:
                i.click()
            text_evaluate = browser.find_elements_by_xpath("//textarea")
            for i in text_evaluate:
                i.send_keys('喵')
            submitbutton = browser.find_element_by_xpath('//button')
            submitbutton.click()
        except Exception:
            pass


if __name__ == '__main__':

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    # 附上这行代码90%可能会有ElementNotVisibleException,反之则不会

    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sanbox')
    #谷歌浏览器版本:72.0.3626.119
    try:
        browser = webdriver.Chrome(options=chrome_options,
                               executable_path='C:/Program Files (x86)/Google/Chrome/Application/chromedriver')
        browser.maximize_window()
        mybrowser=Browser(chrome_options,browser)

        mybrowser.login()
        mybrowser.enter_evaluation_page()
        # mybrowser.evaluate()
        browser.quit()
        print('{:-^30}'.format('Finish Evaluation'))
    except Exception as e:
        print('对不起,元素不可见')
        print(e)

