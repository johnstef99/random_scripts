from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import os

def init():
    driver_loc = '/usr/local/bin/chromedriver'
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=driver_loc, options=options)
    driver.get('http://myinternet.cosmote.gr')
    return driver

def get_gb(driver):
    gb_element = driver.find_element_by_xpath(
        '//*[@id="wrapper"]/div[2]/div[1]/div/h3/span')
    gb_text = gb_element.get_attribute('innerHTML')
    while gb_text == '':
        gb_text = gb_element.get_attribute('innerHTML')
    return (gb_text)


def get_details(driver: webdriver.Chrome):
    details = driver.find_element_by_xpath(
        '//*[@id="statistics-prepaid"]/div/div')
    innerHTML = details.get_attribute('innerHTML')
    while not ('div' in innerHTML):
        innerHTML = details.get_attribute('innerHTML')
    john = BeautifulSoup(innerHTML, features='lxml')
    row = john.find_all("div", {"class": "row"})
    out = ''
    for i in row:
        out += (i.text.replace(
            'MB', 'MB -').replace('Διαθέσιμα για πλοήγηση στο Ιnternet έως', '')) + '\n'
    return out


os.system('figlet cosmote')
driver = init()
print('\nTotal: ' + get_gb(driver)+'GB')
print('==================')
print(get_details(driver))
driver.close()
