from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

youtube_open = False


def open_youtube():

    global youtube_open

    if not youtube_open:

        driver.get("https://www.youtube.com")

        youtube_open = True


def youtube_search(query):

    global youtube_open

    if not youtube_open:

        open_youtube()

        time.sleep(3)

    search = driver.find_element(By.NAME, "search_query")

    search.clear()

    search.send_keys(query)

    search.send_keys(Keys.ENTER)

def youtube_play(video):

    global youtube_open

    if not youtube_open:

        open_youtube()
        time.sleep(3)

    search = driver.find_element(By.NAME, "search_query")
    search.clear()
    search.send_keys(video)
    search.send_keys(Keys.ENTER)

    time.sleep(2)

    first_video = driver.find_element(
        By.ID,
        "video-title"
    )

    first_video.click()    