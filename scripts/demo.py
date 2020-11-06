# from selenium import webdriver

# path = r'D:/Program Files/Chromedriver'

# url = "https://www.facebook.com/marketplace/coloradosprings/search/?query=cars%20trucks"
# driver = webdriver.Chrome(executable_path = path)
# driver.get(url)
# input("enter to close ")
# print(driver.page_source)

# driver.close()
# driver.quit()

# zoom link: https://byui.zoom.us/j/463055791
#%%
mylist = [1,2,3,4]
mylist[len(mylist):] = [1,2]
mylist.extend([6,7])
mylist

# %%

class Complex():
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

        

x = Complex(realpart = 3, imagpart = -4.5)
x.r
x.i


# %%
class Bag():
    def __init__(self):
        print("Initializing...")
        self.data = []
        

    def add(self, x):
        print("Adding...")
        self.data.extend(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

    def display(self):
        print("Displaying list: ")
        print(self.data)
x = Bag()

x.add(["hi", 'hello', 'bruh'])
x.display()


# %%
