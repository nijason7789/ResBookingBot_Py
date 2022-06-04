import requests
from bs4 import BeautifulSoup

Name =  '謝昀霖'
Phone = '0912292900'
url = 'https://inline.app/booking/-LR7EWHI84Fq7C2AdeaE:inline-live-2a466?language=zh-tw'
#https://inline.app/booking/-LR7EWHI84Fq7C2AdeaE:inline-live-2a466/-LR7EWIKquuEfFn8Z-Lc/
#https://www.dcard.tw/f/pet
#https://inline.app/booking/-LR7EWHI84Fq7C2AdeaE:inline-live-2a466?language=zh-tw&utm_source=fordummies&utm_medium=article&utm_campaign=FO2021michelin&utm_content=CHILLIESINE210816michelin
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}
#偽裝自己是使用瀏覽器登入

r = requests.get(url, headers=headers)

print(r.status_code)

if r.status_code == requests.codes.ok:
  print("OK")
  #檢查是否成功登入

soup = BeautifulSoup(r.text,"html.parser")
print(r.text)



#my_data = {'key1': 'value1', 'key2': 'value2'}

#r = requests.post(url=url , data = my_data, headers=headers)