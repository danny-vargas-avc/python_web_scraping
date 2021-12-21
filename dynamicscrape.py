from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = Service('/Users/danny/Desktop/chromedriver')

option = webdriver.Chrome(service=driver)
url = 'https://www.imdb.com/chart/top/'
option.get(url)

soup = BeautifulSoup(option.page_source, 'html.parser')

totalScrapedInfo = []
links = soup.select('table tbody tr td.titleColumn a')
first10 = links[:10]
for anchor in first10:
  option.get('https://www.imdb.com/' + anchor['href'])
  infoList = option.find_element(By.CSS_SELECTOR, '.ipc-inline-list')
  information = infoList.find_elements(By.CSS_SELECTOR, "[role='presentation']")
  scrapedInfo = {
    'title': anchor.text,
    'year': information[0].text,
    'duration': information[2].text,
  }
  totalScrapedInfo.append(scrapedInfo)

print(totalScrapedInfo)