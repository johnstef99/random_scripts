from selenium import webdriver
import os
from datetime import datetime
import time
import sys


def login():
    options = webdriver.ChromeOptions()
    # set browser executable file (even Windows's file .exe)
    options.binary_location = "/usr/bin/brave"
    # options.add_argument("headless") #uncomment this line if you want the browser to run in without a graphical interface
    # set chromedriver path (on windows you have to download the file)
    chromedriver_loc = "/usr/bin/chromedriver"
    driver = webdriver.Chrome(
        executable_path=chromedriver_loc, options=options)

    print('loading page')
    driver.get("http://cosmote.gr")

    print('clicking 15min promo')
    driver.find_element_by_xpath('//*[@id="cookiesConsent"]/div/a').click()
    driver.find_element_by_xpath(
        '/html/body/div[2]/div[1]/div/div[1]/div[2]/div[2]/a').click()

    email_field = driver.find_element_by_id("email")
    pass_field = driver.find_element_by_id("password")
    repass_field = driver.find_element_by_id("register_repeat-password")
    submit = driver.find_element_by_xpath('//*[@id="signup"]')

    print('filling form')
    email = str(datetime.now().timestamp()) + \
        "@freeinternethackfromjohnstef.gr"
    password = "0101010101"

    email_field.send_keys(email)
    pass_field.send_keys(password)
    repass_field.send_keys(password)

    print('submiting form')
    driver.set_page_load_timeout(5)
    driver.find_element_by_xpath('//*[@id="register_terms"]').click()
    submit.click()
    print('done')
    driver.close()


def changeMacAddress():
    os.system('sudo ip link set down wlp5s0 &&')
    os.system('sudo macchanger -r wlp5s0 &')
    os.system('sudo ip link set up wlp5s0')


def countdown(sec):
    for i in range(sec):
        sys.stdout.write(str(i)+' ')
        sys.stdout.flush()
        time.sleep(1)


while True:
    changeMacAddress()
    countdown(10)
    login()
    countdown(870)
