from selenium import webdriver

path = r'D:/Program Files/Chromedriver'

url = "https://www.facebook.com/marketplace/coloradosprings/search/?query=cars%20trucks"
driver = webdriver.Chrome(executable_path = path)
driver.get(url)
input("enter to close ")
print(driver.page_source)

driver.close()
driver.quit()
