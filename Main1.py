import requests
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
driver = webdriver.Chrome()
chrome_options = Options() 
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument(f'user-agent={userAgent}')
executable_path = 'chromedriver.exe'

def ButtonClick(xpath):
  btnPath = xpath
  while(True):
    try:
      btn = driver.find_element_by_xpath(btnPath)
      driver.execute_script("arguments[0].click();", btn)
      break
    except NoSuchElementException:
      time.sleep(1)
      print(btnPath)
      ButtonClick(btnPath)
      break

def LableFill(xpath, content):
  inputPosition = xpath
  inputMessage = content
  while(True):
    try:
      inPut = driver.find_element_by_xpath(inputPosition)
      inPut.send_keys(inputMessage)
      break
    except NoSuchElementException:
      time.sleep(1)
      print(inputPosition)
      LableFill(inputPosition, inputMessage)
      break


def FillTheReservation(Name, Phone, Email):
    
  LableFill('/html/body/div[1]/div/div/div/form/section/div[1]/input', Name)
  LableFill('/html/body/div[1]/div/div/div/form/section/div[2]/div[1]/input', Phone)
  LableFill('/html/body/div[1]/div/div/div/form/section/div[3]/input', Email)

  #time.sleep(1)
  #Input1 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/section/div[1]/input')
  #Input2 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/section/div[2]/div[1]/input')
  #Input3 = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/form/section/div[3]/input')

  #Input1.send_keys(Name)
  #Input2.send_keys(Phone)
  #Input3.send_keys(Email)

  print('訂位成功')

  time.sleep(100)
  #btn_5 = driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div[2]')
  #ButtonClickTest()   




url = 'https://inline.app/booking/-LR7EWHI84Fq7C2AdeaE:inline-live-2a466?language=zh-tw'
#海港
#https://inline.app/booking/-MZH-xZRTVVGkgxbWV95:inline-live-2?language=zh-tw
#咖哩飯:
#https://inline.app/booking/-LR7EWHI84Fq7C2AdeaE:inline-live-2a466?language=zh-tw
#https://inline.app/booking/-LR7EWHI84Fq7C2AdeaE:inline-live-2a466/-LR7EWIKquuEfFn8Z-Lc/
#https://www.dcard.tw/f/pet
#https://inline.app/booking/-LR7EWHI84Fq7C2AdeaE:inline-live-2a466?language=zh-tw&utm_source=fordummies&utm_medium=article&utm_campaign=FO2021michelin&utm_content=CHILLIESINE210816michelin
#偽裝自己是使用瀏覽器登入


#driver = webdriver.Chrome(executable_path=executable_path,chrome_options=chrome_options) #套用設定
driver.get(url)
time.sleep(1)

ButtonClick('/html/body/div[1]/div/main/section[2]/div[1]/div[2]/div')    #點用餐日期

#btn0 = driver.find_element_by_xpath('/html/body/div[1]/div/main/section[2]/div[1]/div[2]/div')
#driver.execute_script("arguments[0].click();", btn0)
#time.sleep(1)

ButtonClick('/html/body/div[1]/div/main/section[2]/div[1]/div[3]/div[2]/div[3]/div[2]/div[1]/div[2]/span')    #選擇日期

#btn1 = driver.find_element_by_xpath('/html/body/div[1]/div/main/section[2]/div[1]/div[3]/div[2]/div[3]/div[2]/div[1]/div[2]/span')
#driver.execute_script("arguments[0].click();", btn1)
#time.sleep(1)

ButtonClick('/html/body/div[1]/div/main/section[2]/div[2]/div[1]/div[3]/div/div/button[7]')   #點選...
#/html/body/div[1]/div/main/section[2]/div[2]/div[1]/div[3]/div/div/button[7]
#/html/body/div[1]/div/main/section[2]/div[3]/div[1]/div[3]/div/div/button[7]
#/html/body/div[1]/div/div/main/div[3]/div[2]/div[4]/button[1]
          
#btn2 = driver.find_element_by_xpath('/html/body/div[1]/div/main/section[2]/div[2]/div[1]/div[3]/div/div/button[7]')
#driver.execute_script("arguments[0].click();", btn2)
#time.sleep(1)

ButtonClick('/html/body/div[1]/div/div/main/div[2]/div[2]/div[4]/button[1]')    #點選時間
#btn3 = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div[2]/div[2]/div[4]/button[1]')
#driver.execute_script("arguments[0].click();", btn3)
#time.sleep(1)

ButtonClick('/html/body/div[1]/div/div/main/div[3]/div[2]/button')    #按下用餐時段
#btn4 = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div[3]/div[2]/button')
#driver.execute_script("arguments[0].click();", btn4)
#time.sleep(1)
    
    
Name =  '謝昀霖'
Phone = '0912292900'
Email = 'lawrence820111@gmail.com'

FillTheReservation(Name, Phone, Email)

time.sleep(100)








#r = requests.get(url, headers=headers)

#print(r.status_code)

#if r.status_code == requests.codes.ok:
  #print("OK")
  #檢查是否成功登入

#soup = BeautifulSoup(r.text,"html.parser")
#print(r.text)



#my_data = {'key1': 'value1', 'key2': 'value2'}

#r = requests.post(url=url , data = my_data, headers=headers)