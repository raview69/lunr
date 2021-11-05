from termcolor import colored
from selenium import webdriver   # for webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep


ab = open('ip.txt', 'r').read().splitlines()
abb = open('ip.txt', 'r').readlines()
ba = len(abb)

for i in range(0, ba):
  try:
    a = PROXY = f"{ab[0+i]}"
    s = Service('/Users/machintoshd/.wdm/drivers/chromedriver/mac64/95.0.4638.17/chromedriver')
    option = webdriver.ChromeOptions()
    option.add_argument('--proxy-server=%s' % a)
    option.add_argument('headless')
    driver = webdriver.Chrome(service=s, options=option)
    driver.get('https://lnr.app/s/GgqXoj')
    sleep(2)
    driver.quit()
    print(colored('Visit Sucessfully', 'green'))
  except :
    print(colored('Visit Failed', 'red'))
def testUserLocationDenver(self):
	self.chrome.get(self.url)
	search = self.chrome.find_element_by_id('user-city')
	self.assertIn('Denver', search.text)
