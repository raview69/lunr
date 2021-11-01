from termcolor import colored
from selenium import webdriver   # for webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
from selenium.webdriver.chrome.service import Service


def testUserLocationDenver(self):
	self.chrome.get(self.url)
	search = self.chrome.find_element_by_id('user-city')
	self.assertIn('Denver', search.text)
 
ab = PROXY = "kontol"
s = Service('/Users/machintoshd/.wdm/drivers/chromedriver/mac64/95.0.4638.17/chromedriver')
option = webdriver.ChromeOptions()
option.add_argument('--proxy-server=%s' % ab)
option.add_argument('headless')
driver = webdriver.Chrome(service=s, options=option)
driver.get('https://lnr.app/s/GgqXoj')
driver.quit()
print(colored('Visit Sucessfully', 'green'))

