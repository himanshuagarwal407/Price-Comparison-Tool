from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import cgi

path = "C:\\Users\\Asus\\PycharmProjects\\PCT\\pct\\chromedriver.exe"

driver = webdriver.Chrome(path)

driver.get("https://amazon.in")
print(driver.title)

form = cgi.FieldStorage()
searchterm = form.getvalue('Searchbox')
print(searchterm)
search = driver.find_element_by_id("twotabsearchtextbox")
search.send_keys("Samsung Galaxy A51 Mobile")
search.send_keys(Keys.RETURN)

try:
    price = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole"))
    )
    print("price is")
    print(price.text)

    title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "a-size-medium a-color-base a-text-normal"))
    )

    print("title is")
    print(title.text)

except:
    driver.quit()
    print("inside exception")

driver.quit()
