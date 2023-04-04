#!/usr/bin/env python
# coding: utf-8

# In[6]:


import subprocess
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
import random
import time

START_PAGE = 1
END_PAGE = 10

EMAIL = 'crunch64@yopmail.com'
PWD = 'Tech2022@'


# In[2]:


subprocess.Popen(["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "--remote-debugging-port=9222"])


# In[3]:


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)


# In[8]:


def login():
    driver.get("https://www.crunchbase.com")
    driver.get("https://www.crunchbase.com/login")
    input1 = driver.find_element_by_xpath('//*[@id="mat-input-1"]')
    input1.clear()
    input1.send_keys(EMAIL)
    time.sleep(2)
    input2 = driver.find_element_by_xpath('//*[@id="mat-input-2"]')
    input2.clear()
    input2.send_keys(PWD)
    time.sleep(2)
    btn = driver.find_element_by_xpath('//*[@id="mat-tab-content-0-0"]/div/login/form/button')
    btn.click()

    
try:
    login()
except Exception as e:
    pass


# In[ ]:


driver.get('https://www.crunchbase.com/discover/organization.companies')


# In[ ]:


data = driver.find_elements_by_xpath('//*[@id="cdk-drop-list-0"]/div/div/grid-body/div/grid-row/grid-cell/div/field-formatter')


# In[ ]:


header = driver.find_elements_by_xpath('//*[@id="cdk-drop-list-0"]/div/div/grid-header/grid-column-header')


# In[ ]:


def save_current_page(page):
    data = driver.find_elements_by_xpath('//*[@id="cdk-drop-list-0"]/div/div/grid-body/div/grid-row/grid-cell/div/field-formatter')
    header = driver.find_elements_by_xpath('//*[@id="cdk-drop-list-0"]/div/div/grid-header/grid-column-header')
    headers = [x.text for x in header[1:-1]]
    tmp = [x.text for x in data]
    with open(f"{page}.csv", "w") as f:
        rows = []
        writer = csv.writer(f)
        writer.writerow(headers)
        for i in range(len(data) // len(headers)):
            rows.append(tmp[i * len(headers) : (i+1) * len(headers)])
        writer.writerows(rows)


# In[ ]:


def next_page():
    driver.find_element_by_xpath('/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/discover/page-layout/div/div/container-with-side-rail-drawer/div/div[2]/section/results/div/div/div[1]/div[1]/results-info/div/a[2]/span[1]/div/span').click()


# In[ ]:


for _ in range(START_PAGE-1):
    next_page()
    print("sleep...")
    time.sleep(random.randint(2, 10))

for page in range(START_PAGE, END_PAGE+1):
    print(f"check page {page}")
    save_current_page(page)
    next_page()
    print("sleep...")
    time.sleep(random.randint(2, 10))

