# -*- coding: utf-8 -*-
"""
Created on Thu Feb 07 23:14:31 2019

@author: avgbndt
"""
import csv
from random import randint
from time import sleep
from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#%%

import params

#%%
class LiSpider(object):
    def __init__(self, username, password, query, output="output"):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(r'/home/geckodriver')
        self.writer = csv.csvWriter(open(f"{output}.csv", "w"))

    def prep(self):
        self.writer.csvWriterow(["username", "position", "education", "country_city", "url"])
        driver.get('https://www.linkedin.com/')
        sleep(randint(3, 6))
        driver.find_element_by_xpath('//a[text()="Sign in"]').click()
        sleep(randint(3, 6))
        
    def login(self):
        uname_input = driver.find_element_by_name('session_key')
        uname_input.send_keys(self.username)
        sleep(randint(3, 6))
        passwd_input = driver.find_element_by_name('session_password')
        passwd_input.send_keys(self.password)
        sleep(randint(3, 6))
        driver.find_element_by_xpath('//button[text()="Sign in"]').click()
        sleep(randint(3, 6))

    def g_search(self):
        driver.get('https://www.google.com/')
        sleep(randint(3, 6))
        s_input = driver.find_element_by_name('q')
        s_input.send_keys(self.query)
        sleep(randint(3, 6))
        s_input.send_keys(Keys.RETURN)
        sleep(randint(3, 6))
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

            education = ', '.join(select.xpath('//*[contains(@class, "pv-entity__school-name")]/text()')\
                    .extract())  # List to String

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

            self.writer.writerow([username,
                                position,
                                education,
                                country_city,
                                url])

            print("Row succesfully written")

    def go(self):
        self.prep()
        self.login()
        self.g_search()
        # Finish
        driver.quit()

if __name__ == "__main__":

    scrapper = LiSpider(params.uname, params.passwd, params.output_file, params.query)
