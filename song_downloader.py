from selenium import webdriver as wbd
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys
from bs4 import  BeautifulSoup as Soup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import  SoupStrainer
import file_move
from song_input import song_name_func

#song name to download

song = song_name_func()



#driver
if song!="":
    driver = wbd.Chrome('C:\\Users\\devar\\.wdm\\drivers\\chromedriver\\80.0.3987.106\\win32\\chromedriver.exe')
    url = "https://www.google.com/"
    driver.get(url)
    song+="\n"
    wait = WebDriverWait(driver,10)
    #search input of google
    wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input'))).send_keys(song)
    page = Soup(driver.page_source,'lxml')
    html= driver.page_source
    song_link = ""
    for link in Soup(html, features = 'lxml',parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            if link['href'].find("https://www.youtube.com/watch?v=")!=-1:
                song_link = str(link['href'])
                break

    #url for site that converts youtube videos to mp3
    downloader_url = "https://ytmp3.cc/en13/"

    driver.get(downloader_url)
    wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="input"]'))).send_keys(song_link)

    wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="submit"]'))).click()

    wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="buttons"]/a[1]'))).click()


    #file is downloading -- wait for 60seconds then move the filename
    #change according to your internet speed
    time.sleep(30)
    file_move.moving()
    driver.stop_client()
    driver.quit()
