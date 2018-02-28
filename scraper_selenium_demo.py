from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Chrome_driver
chrome_path = r"C:\Users\lima.l\Desktop\chromedriver.exe"
#Open chrome window
driver = webdriver.Chrome(chrome_path)
driver.get('https://www.similarweb.com/website/champion.gg')
#waiting for the elements to appear
element_present = EC.presence_of_element_located((By.CLASS_NAME, 'websitePage-trafficShare'))
try:
    WebDriverWait(driver, 20).until(element_present)
except:
    None
#find the class
referals = driver.find_element_by_class_name("websitePage-list")
referals = referals.find_elements_by_class_name("websitePage-listItem")
#Get the data from "Referals" so we can extract how this website get his users or most of it
for referal in referals:
    a =  referal.find_element_by_class_name("websitePage-listItemLink")
    url =  a.get_attribute("data-shorturl")
    span =  referal.find_element_by_class_name("websitePage-trafficShare")
    rate = span.get_attribute("textContent")
    print(rate)
    print(url)