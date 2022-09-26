import selenium
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import re
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import datetime
# 不要运行，切记
server = Service(r"C:\Users\gzbxcpjy\Documents\coldbt\chromedriver.exe")
driver = selenium.webdriver.Chrome(service = server)
driver.get("https://supplier.ecoa.pg.com/")

# 账号密码
def login():
    driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("hbao")
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("qazwsx0.1")
    driver.find_element(By.XPATH, '//input[@name="x_submit"]').click()
# 护舒宝f
def h():
    a = input("愣着干什么？打字啊！！！！")
    b = int(a)
    if 0 < b < 5000:
        values_obs = "3"
    elif 5001 < b < 10000:
        values_obs = "6"
    elif 10001 < b < 15000:
        values_obs = "9"
    obs = driver.find_elements(By.XPATH, '//input[@name="C_STATS"]')
    yesterday = (datetime.datetime.now() + datetime.timedelta(days=0)).date().strftime('%m-%d-%Y')
    for i in obs:
        i.clear()
        i.send_keys(values_obs)
    obs_oos = driver.find_elements(By.XPATH, '//input[@name="C_OBSOOS"]')
    for i in obs_oos:
        i.send_keys('0')
    select = driver.find_elements(By.XPATH, '//select[@class="S4" and @name="C_MEAN"]')
    for i in select:
        Select(i).select_by_index(1)
    std = driver.find_elements(By.XPATH, '//input[@name="C_STDDEV"]')
    for i in std[0: 3]:
        i.send_keys('{:.2f}'.format(random.uniform(0.4, 0.7)))
    mean = driver.find_elements(By.XPATH, '//input[@name="C_MEAN"]')
    values_obs = re.findall('Target: </b>(.*?)<br', driver.page_source)
    for i, j in zip(mean[0:3], values_obs[0:3]):
        i.send_keys(j)
    select = driver.find_elements(By.XPATH, '//select[@class="S1" and @name="a_prod_line"]')
    for i in select:
        Select(i).select_by_index(1)
    driver.find_element(By.XPATH, '//input[@class="M1" and @name="a_mfglotqty"]').send_keys(a)
    driver.find_element(By.XPATH, '//input[@class="M1" and @name="produced_date"]').send_keys(yesterday)
    driver.find_element(By.XPATH, '//input[@tabindex="1"]').send_keys('GZBX22')


def b():
    a = input("愣着干什么？打字啊！！！！")
    b = int(a)
    if 0 < b < 5000:
        values = str(3)
    elif 5001 < b < 10000:
        values = str(6)
    elif 10001 < b < 15000:
        values = str(9)
    obs = driver.find_elements(By.XPATH, '//input[@name="C_STATS"]')
    yesterday = (datetime.datetime.now() + datetime.timedelta(days=0)).date().strftime('%m-%d-%Y')
    for i in obs:
        i.clear()
        i.send_keys(values)
    obsoos = driver.find_elements(By.XPATH, '//input[@name="C_OBSOOS"]')
    for i in obsoos:
        i.send_keys('0')
    select_list = driver.find_elements(By.XPATH, '//select[@class="S4" and @name="C_MEAN"]')
    for i in select_list:
        Select(i).select_by_index(1)
    std = driver.find_elements(By.XPATH, '//input[@name="C_STDDEV"]')
    for i in std[0: 3]:
        i.send_keys('{:.2f}'.format(random.uniform(0.4, 0.7)))
    mean = driver.find_elements(By.XPATH, '//input[@name="C_MEAN"]')
    values = re.findall('Target: </b>(.*?)<br', driver.page_source)
    for i, j in zip(mean[0:3], values[0:3]):
        i.send_keys(j)
    select = driver.find_elements(By.XPATH, '//select[@class="S1" and @name="a_prod_line"]')
    for i in select:
        Select(i).select_by_index(1)
    driver.find_element(By.XPATH, '//input[@class="M1" and @name="a_mfglotqty"]').send_keys(a)
    driver.find_element(By.XPATH, '//input[@class="M1" and @name="produced_date"]').send_keys(yesterday)
    driver.find_element(By.XPATH, '//input[@tabindex="1"]').send_keys('GZBX2022')


# 佳洁士
def j():
    a = input("愣着干什么？打字啊！！！！")
    b = int(a)
    if 10001 < b < 35000:
        values_obs = ['13', '13', '13', '13', '125', '125', '125', '5', '125', '125', '125', '125', '125', '125', '125',
                      '125']
    elif 3201 < b < 10000:
        values_obs = ['13', '13', '13', '13', '125', '125', '80', '5', '125', '80', '80', '80', '80', '125', '80',
                      '125']
    elif 1201 < b < 3200:
        values_obs = ['13', '13', '13', '13', '125', '125', '50', '5', '125', '50', '50', '50', '50', '125', '50',
                      '125']
    elif 501 < b < 1200:
        values_obs = ['13', '13', '13', '13', '125', '125', '32', '5', '125', '50', '50', '50', '50', '125', '50',
                      '125']
    elif 281 < b < 500:
        values_obs = ['13', '13', '13', '13', '125', '125', '20', '5', '125', '13', '13', '13', '13', '125', '13',
                      '125']
    else:
        print("无法定义变量")
    yesterday = (datetime.datetime.now() + datetime.timedelta(days=0)).date().strftime('%m-%d-%Y')
    obs = driver.find_elements(By.XPATH, '//input[@name="C_STATS"]')
    try:
        if len(obs) == len(values_obs):
            values_obs.reverse()
        for i in obs:
            i.clear()
            i.send_keys(values_obs.pop())
    except:
        print("\n   手输吧懒人！")
    obsoos = driver.find_elements(By.XPATH, '//input[@name="C_OBSOOS"]')
    for i in obsoos:
        i.send_keys('0')
    select_list = driver.find_elements(By.XPATH, '//select[@class="S4" and @name="C_MEAN"]')
    for i in select_list:
        Select(i).select_by_index(1)
    mean = driver.find_elements(By.XPATH, '//input[@name="C_MEAN"]')
    values_1 = re.findall('Target: </b>(.*?)<br', driver.page_source)
    for i, j in zip(mean[0:4], values_1[0:4]):
        i.send_keys(j)
    std = driver.find_elements(By.XPATH, '//input[@name="C_STDDEV"]')
    std[3].send_keys("0")
    min_1 = driver.find_elements(By.XPATH, '//input[@name="C_MIN"]')
    for i in std[:3]:
        i.send_keys('{:.2f}'.format(random.uniform(0.4, 0.7)))
    for i, j in zip(min_1[:3], values_1[:3]):
        i.clear()
        j = int(j) - 1
        i.send_keys(j)
    max_1 = driver.find_elements(By.XPATH, '//input[@name="C_MAX"]')
    for i, j in zip(max_1[:3], values_1[:3]):
        i.clear()
        j = int(j) + 1
        i.send_keys(j)
    select = driver.find_elements(By.XPATH, '//select[@class="S1" and @name="a_prod_line"]')
    for i in select:
        Select(i).select_by_index(1)
    driver.find_element(By.XPATH, '//input[@class="M1" and @name="a_mfglotqty"]').send_keys(a)
    driver.find_element(By.XPATH, '//input[@class="M1" and @name="produced_date"]').send_keys(yesterday)
    driver.find_element(By.XPATH, '//input[@tabindex="1"]').send_keys('GZBX22')
