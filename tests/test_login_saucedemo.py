from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

def test_locators():
    
    service = Service("/Users/princevaviya/Documents/software-testing/drivers/msedgedriver")
    driver = webdriver.Edge(service=service)

    try:

        driver.get("https://www.google.com")
        print(driver.title)


    finally:
        driver.quit()