import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import json
import sys

# first param is what to search and the second is how many page to scroll
search = sys.argv[1]
numberofpage = sys.argv[2]

# Open twitter with requested search

browser = webdriver.Firefox()
numpage=int(numberofpage)
browser.get('https://twitter.com/search?q="'+ search +'"')

# Scroll requested number of pages

while numpage != 0:
  browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
  time.sleep(1)
  numpage= numpage - 1

data={}
data['tr'] = []
tweets = browser.find_elements_by_class_name("content")
# Get all tweets 
for tweet in tweets:
  t= tweet.find_element_by_class_name("tweet-text")
  name= tweet.find_element_by_class_name("fullname")
  username=tweet.find_element_by_class_name("username")
  comment = tweet.find_element_by_xpath("(//span[@class='ProfileTweet-actionCount'])[1]").get_attribute("data-tweet-stat-count")
  retweet = tweet.find_element_by_xpath("(//span[@class='ProfileTweet-actionCount'])[2]").get_attribute("data-tweet-stat-count")
  like =  tweet.find_element_by_xpath("(//span[@class='ProfileTweet-actionCount'])[3]").get_attribute("data-tweet-stat-count")
  data['tr'].append({
  'tweet': t.text,
  'name': name.text,
  'username': username.text,
  'comment': comment,
  'retweet': retweet,
  'like': like
  })
# Store json  in data.txt
with open('data.txt', 'w') as outfile:  
    json.dump(data, outfile)
