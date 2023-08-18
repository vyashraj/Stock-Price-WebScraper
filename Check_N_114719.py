from selenium.webdriver.common.by import By
from selenium import webdriver as wd
import Check2_Interface_N_114723 as q
from tkinter import *
global r_price
global wd1 
class Start:
    CO = wd.ChromeOptions()
    CO.add_argument("--headless")
    wd1=wd.Chrome(r'C:\Users\91749\Downloads\chromedriver\chromedriver.exe', options=CO)
    def __init__(self):
        CO =self.CO
        wait_imp = 10
        CO.add_experimental_option('useAutomationExtension', False)
        CO.add_argument('--ignore-certificate-errors')
        CO.add_argument('--start-maximized')
        CO.add_argument("--ignore-ssl-errors")
        self.wd1.implicitly_wait(wait_imp)
        print ("*************************************************************************** \n")
        print("                     Starting Program, Please wait ..... \n")
        print("Connecting...")
    def fetch(self,link ,xpath ,name="Trading Website"):
        self.wd1.get(link)
        f_price = self.wd1.find_element(By.CLASS_NAME, xpath)
        r_price = f_price.text
        print(r_price)
        return r_price

def checkkk(l1,l2,xpath):
    a=Start()
    b=Start()
    while True:
        p1=a.fetch(l1,xpath)
        p2=a.fetch(l2,xpath)
        q.create(p1,p2)