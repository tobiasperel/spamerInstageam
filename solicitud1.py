import time
import re
import platform
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from data1 import *

sistema = platform.system()

if sistema == 'Windows':
    driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
else:
    chromeOptions = Options()
    chromeOptions.headless = True
    driver = webdriver.Chrome(executable_path="./chromedriver",
    options=chromeOptions)


driver.get("https://www.instagram.com/espn/followers/")

#driver.get(f"window.open('about:blank','{instagram_link}');")

#f"window.open('about:blank','{diccionarioStreamer[i][0]}');"

#iniciado automatico
while True:
    try:
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input').send_keys(instagram_username)
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input').send_keys(instagram_pwd)
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]').click()
        break
    except:
       pass

time.sleep(5)

while True:
    try:
        driver.get("https://www.instagram.com/espn/followers")
        break
    except:
       pass

#-----------------------------------------------------------------------------------------------------------------------

def empezarSeguir(cod):
    while True:
        try:
            driver.execute_script(cod)
            break
        except:
            continue

def entrarAFollowers():
    while True:
        try:
            driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
            break
        except:
            pass



time.sleep(3)
codigo = '''
const btnList = [...document.getElementsByClassName("sqdOP  L3NKy   y3zKF     ")]

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

const clickearBotones = async () => {
	for (let b of btnList) {
		await sleep(Math.random()*(15000-10000)+10000)
		b.click()
    }
    window.location.href = "https://www.instagram.com/espn/"
}

clickearBotones()
'''

contador = 0
while True:
    entrarAFollowers()
    time.sleep(30)
    print('sisi')
    empezarSeguir(codigo)
    print(1)
    time.sleep(300)
    print(2)
    if (contador % 7 == 0):
        time.sleep(600)