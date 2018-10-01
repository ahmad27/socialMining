import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
import sys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException

# Arguments for the python code 
search = sys.argv[1]
user1 = sys.argv[2]
password1 = sys.argv[3]
data1 = sys.argv[4]
# transform arguments to string to work in functions
user = str(user1)
password = str(password1)
data=str(data1)
# Login to Facebook
browser =  webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
browser.get('https://www.facebook.com')
browser.find_element_by_xpath("//input[@name='email']").send_keys(user)
browser.find_element_by_xpath("//input[@name='pass']").send_keys(password)
browser.find_element_by_xpath("//input[starts-with(@id, 'u_0_')][@value='Log In']").click()

# Search posts with the query given in input
browser.get('https://www.facebook.com/search/posts/?q="' + search + '"')
data={}
data['tr'] = []
posts = browser.find_elements_by_class_name("fb_content")
# Get all posts
for post in posts:
  user= post.find_element_by_class_name("fwb")
  print(user.text)
  #txt= post.find_element_by_class_name("text_exposed_root")
  #print(txt.text)
  #test=post.find_element_by_xpath("(//form)")
  #form=post.find_element_by_xpath("(//form[@class='commentable_item'])")
  
  print(test.text)
  data['tr'].append({
  'test': test.text,
  'user': user.text,
#  'username': username.text,
#  'comment': comment,
#  'like': like
  })
# Store json  in facebookpost.txt
with open('facebookpost.txt', 'w') as outfile:  
    json.dump(data, outfile)
