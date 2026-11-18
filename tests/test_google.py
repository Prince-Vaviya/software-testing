
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By


def test_edge_browser():

    service = Service("./drivers/msedgedriver")

    driver = None

    try:
        print("Starting Microsoft Edge...")

        driver = webdriver.Edge(service=service)

        print("Opening Python.org...")
        driver.get("https://www.google.com/")

        assert "Google" in driver.title

        print("Title:", driver.title)
        element = driver.find_element(By.ID, "ti6dpd")
        print("Edge automation successful!")

    finally:
        if driver:
            driver.quit()
