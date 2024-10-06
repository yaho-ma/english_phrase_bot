import time
import traceback

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager  # pip install webdriver-manager

service = Service(ChromeDriverManager().install())


def go_to_page(my_url: str, search_phrase: str, num_videos: int = 1):
    mydriver = webdriver.Chrome(service=service)

    video_url_list = []

    try:
        mydriver.get(my_url)
        time.sleep(0)

        # Find the input field by its ID 'q'
        search_box = mydriver.find_element(By.ID, 'q')  # Find the input field by its ID 'q'
        search_box.send_keys(search_phrase)  # Type the search phrase in the input field
        search_box.send_keys(Keys.RETURN)  # press 'Enter' to start the search
        time.sleep(0)



        for number in range(num_videos):

            #mydriver.switch_to.frame('player')
            iframe_element = mydriver.find_element(By.ID, 'player')

            video_url = iframe_element.get_attribute('src')

            print(f" this is the video URL: {video_url}")
            video_url_list.append(video_url)

            # click the Next button
            #mydriver.switch_to.default_content()
            #next_button = mydriver.find_element(By.ID, 'b_next')
            #next_button.click()

            #mydriver.switch_to.frame('player')

            #time.sleep(2)






    except Exception as ex:
        print(f'Oh NOOO!!! An error has occured {ex}')
        traceback.print_exc()
    finally:
        mydriver.close()
        mydriver.quit()

    formatted_video_list = []
    for i, url in enumerate(video_url_list):
        formatted_video_list.append(f'{i + 1}) {url}')
    formatted_video_links = '\n\n'.join(formatted_video_list)

    if formatted_video_links:
        return formatted_video_links
    else:

        return "No video URLs found."
