# -*- coding: utf-8 -*-
"""
Created on Thu Feb 07 23:14:31 2019

@author: crsdprnc
"""
import csv
from time import sleep
from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#%%
import params

#%% Opening Output File
csvWriter = csv.csvWriter(open(params.output_file, 'w'))
csvWriter.csvWriterow(['username',
                       'position',
                       'education',
                       'country_city',
                       'url'])

#%% Setting up Selenium
driver = webdriver.Firefox(r'/home/geckodriver'); sleep(3)

#%% Driver on LinkedIn Website
driver.get('https://www.linkedin.com/'); sleep(10)
driver.find_element_by_xpath('//a[text()="Sign in"]').click(); sleep(5)

#%% Account Login
uname_input = driver.find_element_by_name('session_key')
uname_input.send_keys(params.uname); sleep(5)
passwd_input = driver.find_element_by_name('session_password')
passwd_input.send_keys(params.passwd); sleep(5)
driver.find_element_by_xpath('//button[text()="Sign in"]').click(); sleep(10)

#%% Google Search
driver.get('https://www.google.com/'); sleep(5)
s_input = driver.find_element_by_name('q')
s_input.send_keys(params.query); sleep(10)
s_input.send_keys(Keys.RETURN); sleep(5)

#%% Looping through search results
results = driver.find_elements_by_xpath('//*[@class="r"]/a[1]')
results = [i.get_attribute('href') for i in results]

for i in results:
    driver.get(i)
    sleep(8)
    select = Selector(text=driver.page_source)

    username = select.xpath('//title/text()').extract_first()
    username = username.split(' | ')[0]

    position = select.xpath('//h2/text()').extract_first()
    position = position.strip()

    education = ', '.join(
                select.xpath('//*[contains(@class, "pv-entity__school-name")]/text()').extract()
    )  # List to String

    country_city = select.xpath('//*[@class="t-16 t-black t-normal inline-block"]/text()').extract_first()
    country_city = country_city.strip()

    url = str(driver.current_url)

    print(f'''
          {username}
          {position}
          {education}
          {country_city}
          {url}
          ''')

    csvWriter.writerow([username,
                        position,
                        education,
                        country_city,
                        url])

    print("Row succesfully written")

# Finish
driver.quit()
