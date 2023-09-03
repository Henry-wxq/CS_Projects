import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def checking_button():
    try:
        wait = WebDriverWait(driver, 2, 0.2)
        wait.until(EC.text_to_be_present_in_element((By.XPATH,
                                                    '//*[@id="app"]/div[2]/div[2]/div[2]/div[2]/div[4]/div[2]/div[1]'),
                                                    '立即购票'))
        driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/div[2]/div[4]/div[2]/div[1]').click()
    except TimeoutException:
        print('Refresh Timeout')
        driver.refresh()
        checking_button()


if __name__ == '__main__':
    # 0.0 Get User Info
    phone_num = input('请输入你的手机号码: ')
    password = input('请输入你的B站密码(不会储存): ')
    target_url = input('请输入B站目标抢票网站: ')

    # 1.1 Prevent the auto close of Chrome (defaulted close)
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)

    # 1.2 Stop automatic prohibition
    option.add_experimental_option('excludeSwitches', ['enable-automation'])

    # 1.3 Mask the save password prompt box
    prefs = {'credentials_enable_service': False, 'profile.password _manager _enabled': False}
    option.add_experimental_option('prefs', prefs)

    # 1.4 Anti-reptile feature processing
    option.add_argument('--disable-blink-features=AutomationControlled')

    # 2.1 Open the Google Chrome
    driver = webdriver.Chrome(options=option)

    # 2.2 Open the Specific Website
    driver.get('https://passport.bilibili.com/login')
    time.sleep(0.5)

    # 3.0 Auto Login
    # 3.1 Locate the username element and input username
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/input'). \
        send_keys(phone_num)
    time.sleep(0.5)

    # 3.2 Locate the key element and input key
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[1]/div[3]/input'). \
        send_keys(password)
    time.sleep(0.5)

    # 4.1 Click to Login
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]').click()
    time.sleep(10)

    # 6. Reserve
    driver.get(target_url)
    checking_button()
