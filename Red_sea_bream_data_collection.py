import imp
from lib2to3.pgen2 import driver
from selenium import webdriver
import pandas as pd
import time

path = 'C:\\Users\\La vie est belle\\Desktop\\ML_practice\\Implementation-of-machine-learning-algorithm-through-real-life-examples\\chromedriver.exe'
driver = webdriver.Chrome(path)

url = 'https://www.susansijang.co.kr/nsis/miw/ko/info/miw3110'
driver.get(url)
time.sleep(10)

charm = []
for i in range(5):
    date = driver.find_element_by_xpath('//*[@id="searchDe"]')
    date.clear()
    date.send_keys('2020.07.2'+str(i))

    bt = driver.find_element_by_xpath('//*[@id="searchBtn"]')
    bt.click()
    time.sleep(1)

    opt = driver.find_element_by_xpath('//*[@id="kdfshNm"]/option[@value="참돔"]')
    opt.click()

    bt = driver.find_element_by_xpath('//*[@id="searchBtn"]')
    bt.click()
    time.sleep(1)

    df = pd.read_html(driver.page_source)[1]
    charm.append(df)

driver.quit()