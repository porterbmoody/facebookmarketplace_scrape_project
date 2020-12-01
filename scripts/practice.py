# from selenium import webdriver
# from bs4 import BeautifulSoup
import random
from datetime import datetime
wait_time = random.randint(2000*60, 3000*60)/99
print('Waiting:', round(wait_time/60, 2), "mins to run again.")
now = datetime.now()

dt_string = now.strftime("%H:%M:%S")
print("Running again at:", dt_string)
print(type(dt_string))
print("at:",  round(wait_time/60, 0))


# # driver path
# driver_path = r'D:/Program Files/chromedriver'
# # your url
# url = "https://www.facebook.com/marketplace/coloradosprings/search/?query=cars%20and%20trucks"

# print("Creating driver...")
# driver = webdriver.Chrome(executable_path = driver_path)


# print("opening url...")
# driver.get(url)

# ## now parse with bs4
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# input()
# path_out = 'D:/BYUI/fall 2020/Side Projects/facebookmarketplace_scrape_project/scripts/fb.html'
# with open(path_out, "w") as f:
#     f.write(soup)
    


# print("Closing...")
# # close
# driver.close()
# driver.quit()
