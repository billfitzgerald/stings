from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd
import re
import os
import datetime
import tldextract
import csv

## Specify file with search strings
source_file = 'strings.csv' # file should be a csv with two columns named `source_strings` and `precise`

## Select Google or DuckDuckGo
#search_base = 'https://duckduckgo.com/?q='
search_base = 'https://www.google.com/search?q='

##########################################
## Do Not Adjust Values Below This Line ##
##########################################

count = 0


base_domain = input("Enter the domain you are researching. Just put the base domain, ie: facebook.com  ")

d = datetime.datetime.today()
year = d.strftime("%Y")
month = d.strftime("%m")
day = d.strftime("%d")

# create a new Firefox session
driver = webdriver.Firefox()

# read in csv file as dataframe
thank_you = pd.read_csv(source_file) # file should be a table with columns 'source_strings'
 
# build search urls
for a,b in thank_you.iterrows():
	string = b['source_strings']
	if b['precise'] == 'yes':
		string = f'"{string}"'
	else:
		pass
	count += 1
	search_url = f"{search_base}{string} site:{base_domain}"
	print(search_url)
	if count == 1:
		driver.get(search_url)
	elif count == 2:
		driver.execute_script("window.open('about:blank', '02tab');")
		driver.switch_to.window("02tab")
		driver.get(search_url)
	elif count == 3:
		driver.execute_script("window.open('about:blank', '03tab');")
		driver.switch_to.window("03tab")
		driver.get(search_url)
	elif count == 4:
		driver.execute_script("window.open('about:blank', '04tab');")
		driver.switch_to.window("04tab")
		driver.get(search_url)
	elif count == 5:
		driver.execute_script("window.open('about:blank', '05tab');")
		driver.switch_to.window("05tab")
		driver.get(search_url)
	elif count == 6:
		driver.execute_script("window.open('about:blank', '06tab');")
		driver.switch_to.window("06tab")
		driver.get(search_url)
	elif count == 7:
		driver.execute_script("window.open('about:blank', '07tab');")
		driver.switch_to.window("07tab")
		driver.get(search_url)
	elif count == 8:
		driver.execute_script("window.open('about:blank', '08tab');")
		driver.switch_to.window("08tab")
		driver.get(search_url)
	elif count == 9:
		driver.execute_script("window.open('about:blank', '09tab');")
		driver.switch_to.window("09tab")
		driver.get(search_url)
	elif count == 10:
		driver.execute_script("window.open('about:blank', '10tab');")
		driver.switch_to.window("10tab")
		driver.get(search_url)
	elif count == 11:
		driver.execute_script("window.open('about:blank', '11tab');")
		driver.switch_to.window("11tab")
		driver.get(search_url)
	elif count == 12:
		driver.execute_script("window.open('about:blank', '12tab');")
		driver.switch_to.window("12tab")
		driver.get(search_url)
	elif count == 13:
		driver.execute_script("window.open('about:blank', '13tab');")
		driver.switch_to.window("13tab")
		driver.get(search_url)
	elif count == 14:
		driver.execute_script("window.open('about:blank', '14tab');")
		driver.switch_to.window("14tab")
		driver.get(search_url)
	elif count == 15:
		driver.execute_script("window.open('about:blank', '15tab');")
		driver.switch_to.window("15tab")
		driver.get(search_url)
	elif count == 16:
		driver.execute_script("window.open('about:blank', '16tab');")
		driver.switch_to.window("16tab")
		driver.get(search_url)
	elif count == 17:
		driver.execute_script("window.open('about:blank', '17tab');")
		driver.switch_to.window("17tab")
		driver.get(search_url)
	elif count == 18:
		driver.execute_script("window.open('about:blank', '18tab');")
		driver.switch_to.window("18tab")
		driver.get(search_url)
	elif count == 19:
		driver.execute_script("window.open('about:blank', '19tab');")
		driver.switch_to.window("19tab")
		driver.get(search_url)
	elif count > 19:
		print("Wow you are searching for a lot of stuff. \nWe only support opening 20 tabs at a time.\nWhy do you hate the internet?")
	else:
		print("Something is very screwy")
	
print("All Done! Processed {0} search strings.".format(count))
