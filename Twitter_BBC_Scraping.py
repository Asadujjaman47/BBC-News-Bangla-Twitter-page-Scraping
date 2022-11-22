# Import Dependencies
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

PATH = "C:\driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://twitter.com/login")

driver.set_window_size(1920, 1080)

subject = "bbcbangla"



# Setup the log in
sleep(8)
username = driver.find_element(By.XPATH,"//input[@name='text']")
username.send_keys("username")
next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
next_button.click()

sleep(10)
password = driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys('password')
log_in = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
log_in.click()


# Search item and fetch it
sleep(5)
search_box = driver.find_element(By.XPATH, "//input[@data-testid='SearchBox_Search_Input']")
search_box.send_keys(subject)
search_box.send_keys(Keys.ENTER)

sleep(5)
people = driver.find_element(By.XPATH, "//span[contains(text(),'People')]")
people.click()


sleep(5)
profile = driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[1]/div/div/div")
#profile = driver.find_element(By.XPATH, "//*[data-testid='UserCell']")
profile.click()


UserTags=[]
TimeStamps=[]
Tweets=[]
Replys=[]
reTweets=[]
Likes=[]

articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
while True:
    for article in articles:
        UserTag = driver.find_element(By.XPATH,".//div[@data-testid='User-Names']").text
        UserTags.append(UserTag)
        
        TimeStamp = driver.find_element(By.XPATH,".//time").get_attribute('datetime')
        TimeStamps.append(TimeStamp)
        
        Tweet = driver.find_element(By.XPATH,".//div[@data-testid='tweetText']").text
        Tweets.append(Tweet)
        
        Reply = driver.find_element(By.XPATH,".//div[@data-testid='reply']").text
        Replys.append(Reply)
        
        reTweet = driver.find_element(By.XPATH,".//div[@data-testid='retweet']").text
        reTweets.append(reTweet)
        
        Like = driver.find_element(By.XPATH,".//div[@data-testid='like']").text
        Likes.append(Like)
        
        UserTags = list(set(UserTags))
        TimeStamps = list(set(TimeStamps))
        Tweets = list(set(Tweets))
        Replys = list(set(Replys))
        reTweets = list(set(reTweets))
        Likes = list(set(Likes))
        
        
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(3)
    articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
    
    size = list(set(Tweets))
    if len(size) > 20:
        break


print(len(UserTags),
len(TimeStamps),
len(Tweets),
len(Replys),
len(reTweets),
len(Likes))

import pandas as pd

df = pd.DataFrame(zip(UserTags,TimeStamps,Tweets,Replys,reTweets,Likes)
                  ,columns=['UserTags','TimeStamps','Tweets','Replys','reTweets','Likes'])

df.head()


df.to_excel(r"C:\data\DATA.xlsx", index=False)

import os
os.system('start "excel" "C:\data\\DATA.xlsx"')
