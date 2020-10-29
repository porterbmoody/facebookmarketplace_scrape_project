#%%
try:
    import requests
    from bs4 import BeautifulSoup
    import pprint
    from selenium import webdriver
    import time
    import random
    import pandas as pd
    import re
    from selenium.webdriver.chrome.options import Options
    import numpy as np
    from termcolor import colored
    import connect_to_mysql
except ImportError as ex:
    print(ex)


path = r'D:/Program Files/Chromedriver'
url = "https://www.facebook.com/marketplace/coloradosprings/search/?query=cars%20trucks "
break_ = colored("---------------------------------------------------------------------", 'yellow')
# %%
username = "porterbmoody@gmail.com"
password = "Yoho1mes"
# password = str(input("Enter password: "))
def fb_login():
    """ returns soup
    """
    print(colored("Connecting...", "green"))
    global driver
    driver = webdriver.Chrome(executable_path = path)
    driver.get(url)

    time.sleep(random.randint(200,300)/100)

    print(break_)
    print(colored("Scrolling...", 'yellow'))
    scroll_down()
    time.sleep(random.randint(200,300)/100)

    print(break_)
    print(colored("Scrolling...", 'yellow'))
    scroll_down()
    time.sleep(random.randint(200,300)/100)

    print(break_)
    print(colored("Scrolling...", 'yellow'))
    scroll_down()
    time.sleep(random.randint(200,300)/100)

    
    return BeautifulSoup(driver.page_source, 'html.parser')


    print(break_)

def alt_element(a):
    return a[::2]

def scrape_soup(soup):

    results_title     = soup.find_all(class_='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7')
    results_price     = soup.find_all(class_='d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb mdeji52x a5q79mjw g1cxx5fr lrazzd5p oo9gr5id')
    results_mile      = soup.find_all(class_='a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5 ojkyduve')
    result_link       = soup.find_all(class_ = 'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 p8dawk7l')
    prices            = []
    titles            = []
    locations         = []
    miles             = []
    years             = []
    links             = []
    # results_mile = soup.find_all('div', {"class" : "rq0escxv j83agx80 cbu4d94t i1fnvgqd muag1w35 pybr56ya f10w8fjw k4urcfbm c7r68pdi suyy3zvx"})

    line_number = 0
    
    for mile in result_link:
        # print(len(mile))


        row = mile.find_all(class_ = 'aahdfvyu fsotbgu8')
        
        if len(row) == 4:
            link = "https://www.facebook.com" + mile.attrs['href']
            links.append(link)
            print(link, sep = "\n")
            for m in row:

                if  line_number % 4 == 0:
                    # price = re.replace('$', '', m.find(class_ = "hlyrhctz").text)
                    # prices.append(int(re.replace(',', '', price)))
                    
                    prices.append(m.find(class_ = "hlyrhctz").text)
                    
                elif line_number % 4 == 1:
                    # print(re.findall('^\d{4}', m.text))
                    titles.append(m.text)
                    print(m.text)
                    try:
                        years.append(int(re.findall('^\d{4}', m.text)[0]))
                    except:
                        years.append(np.nan)
                elif line_number % 4 == 2:
                    locations.append(m.text)

                elif line_number % 4 == 3:
                    miles.append(m.text)

                line_number += 1

    
    print(break_)

    print("Titles: ", len(titles), "Miles: ", len(miles), "prices:", len(prices), "Location:", len(locations),"Link:", len(links))
    if len(links) == len(titles):
        # del links[-1]
        print(colored("We're all good", 'green'))
    dat = (pd.DataFrame({
            "title"    : titles,
            "miles"    : miles,
            "price"    : prices,
            "location" : locations,
            "link"     : links
        }).query('price != "Sold" and price != "Pending"').assign(
        year  = lambda x: x['title'].str.extract(r'^(\d{4})').astype("Float32"),
        price = lambda x: x['price'].str.replace("$", "").str.replace(",", "").astype("Float32"),
        miles = lambda x: x['miles'].str.extract("(\d+)").astype("Float32")*1000
        ))

    
    dat.to_csv("data/cars.csv", index = False)

def keep_open():
    input("Press Enter to close")


def scroll_down():
    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height



def main():
    
    # scrape_soup(fb_login())
    # with open("facebook.html", mode = "rb") as infile:
    #     soup = BeautifulSoup(infile, 'html.parser')
    #     scrape_soup(soup)

    scrape_soup(fb_login())
    keep_open()
    driver.close()

if __name__ == "__main__":
    main()


    # print(break_)
    # print("Miles:", len(miles), "Prices:", len(prices))
    # print(break_)
    # for mile in results_mile:
    #     if bool(re.search('miles', mile.text)) == True:
    #         miles.append(mile.text)
    #         # print("Appending:", mile.text)
    #     elif mile.text == '':
    #         miles.append("None")
    #         print("Skipping:", mile.text)
    # ##### Prices
    # for price, mile in zip(results_price, miles):

    #     if mile == "None":
    #         miles.remove(mile)
    #         print(break_)
    #         print("Removing ",mile,"from miles,", price.text)
    #         print(break_)
    #         continue
    #     else:
    #         print(break_)
    #         print("Appending:",price.text, "Mile:",mile)
    #         prices.append(price.text)
            

    # for title in results_title:

    #     titles.append(title.text)
    #     years.append(int(re.findall('\d{4}', title.text)[0]))


    # while len(miles) > len(years):
    #     print("Miles", len(miles),"<", len(years), "Titles: ", len(titles), "Prices: ", len(prices), " Deleting: ", miles[-1])
    #     del miles[-1]
        # del years[-1]
        # del titles[-1]
        # del prices[-1]