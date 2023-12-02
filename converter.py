import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

from google_cookies import reject_cookies
from sweet_cookies import save_cookie, load_cookie
from extracting_links import links


USERNAME = 'username@gmail.com'
PASSWD = '########'

# initialize driver 
driver = webdriver.Chrome()
url = 'https://www.google.com'
driver.get(url)
time.sleep(5)
reject_cookies(driver)
time.sleep(5)

driver.get('https://linkedin.com/login')

driver.implicitly_wait(10)
wait = WebDriverWait(driver, 20)

user_name = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="username"]')))
user_name.send_keys(USERNAME)

time.sleep(10)

password = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
password.send_keys(PASSWD)

time.sleep(10)

submit_btn = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
submit_btn.send_keys(Keys.ENTER)

time.sleep(5)

lsn_links = links()
# print(lsn_links)
print(len(lsn_links))



for link in lsn_links:
    driver.get(link)
    time.sleep(6)
    current_url = driver.current_url
    time.sleep(3)
    with open("urls.csv","a") as fi:
        fi.write(f'"{link}","{current_url}"\n')
    time.sleep(2)
    
print("Done extracting links")


