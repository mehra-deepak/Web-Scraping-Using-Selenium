from selenium import webdriver
import requests
import bs4
import os
import pandas as pd
import numpy as np

    

#new, top, mix, track and artist urls
happy_url= "https://soundcloud.com/happymusic" 
sad_url= "https://soundcloud.com/the-titania-1/emotional-sad-music"
neutral_url= "https://soundcloud.com/freebmusic"
angry_url ="https://soundcloud.com/angermusicpublishing"
surprised_url="https://soundcloud.com/energetic-substance"
_url_end ="&filter.duration=epic"

#create the selenium browser
browser = webdriver.Chrome("C:\\Users\\Lenovo\\Desktop\\moodyplayer\\chromedriver.exe")
browser.get("https://soundcloud.com/")

#main menu
print()
print(">>> Welcome to the Python Soundcloud Scraper!")
print(">>> Explore the Top, New and Hot charts for all genres")
print(">>> Search for tracks, artists, and mixes")
print()

def function(mood):
    while(True):
        
        if mood == "happy":
            browser.get(happy_url)
            continue
        if mood == "sad":
            browser.get(sad_url )
            continue
        if mood == "surprised":
            browser.get(surprised_url)
            continue
        if mood == "angry":
            browser.get(angry_url)
            continue

       
function('happy')



    
