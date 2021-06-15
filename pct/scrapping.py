from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrapp(request):

    searchterm = request.POST.get('Searchbox','default')
    print("Product: ", searchterm)

    path = "C:\\Users\\Asus\\PycharmProjects\\PCT\\pct\\chromedriver.exe"

    driver = webdriver.Chrome(path)

    driver.get("https://amazon.in")
    print(driver.title)

    search = driver.find_element_by_id("twotabsearchtextbox")
    search.send_keys(searchterm)
    search.send_keys(Keys.RETURN)

    try:
        price = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole"))
        )
        print("price of ", searchterm, "in amazon.in:")
        pro_price=price.text
        print(pro_price)

    except:
        pro_price='Not available'
        driver.quit()
        print("inside exception")

    driver.quit()

    driver1=webdriver.Chrome(path)
    driver1.get('https://www.flipkart.com/')

    search=driver1.find_element_by_class_name('LM6RPg')
    search.send_keys(searchterm)
    search.send_keys(Keys.RETURN)

    try:
        heading = WebDriverWait(driver1, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, '_3wU53n'))
        )

        print("Heading: ", heading.text)

        print("Entered try block")
        price1 = WebDriverWait(driver1, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "_1uv9Cb"))
        )
        print("price of ", searchterm, " in flipkart.com: ")
        pro_price1 = price1.text
        print(pro_price1)

    except:
        pro_price1='Not available'
        driver1.quit()
        print("Inside exception")

    driver1.quit()

    param = {'Site1':'Amazon', 'Site2':'Flipkart', 'Product':searchterm, 'Price1':pro_price, 'Price2':pro_price1}

    return render(request, 'output.html', param)
