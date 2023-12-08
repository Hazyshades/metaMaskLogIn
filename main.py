from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

profile_path = r"C:\Users\leo\AppData\Local\Google\Chrome\User Data"


def login():
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument(f'user-data-dir={profile_path}')
    chrome_options.add_argument('--profile-directory=Profile 1')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", chrome_options=chrome_options)
    time.sleep(5)
    driver.get(
        'https://www.app.rage.trade/vaults/0xa237af5e'
    )
    time.sleep(4)

    driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div/header/div[2]/button[2]/div').click()
    driver.find_element(By.XPATH, '//*[@id="radix-:R1jlj6:"]/div[3]/div/button[1]').click()
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    # print("Second window title = " + driver.title)
    time.sleep(1)
    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    password.send_keys('test')  # set your password
    time.sleep(3)
    password.send_keys(Keys.ENTER)
    time.sleep(3)
    # check if button "Got It" exist
    gotIt = driver.find_element(By.XPATH, '//*[@id="popover-content"]/div/div/section/div[3]/button')

    if gotIt != '':
        gotIt.click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[2]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
    time.sleep(15)


if __name__ == '__main__':
    login()
