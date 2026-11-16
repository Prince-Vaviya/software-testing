
from selenium import webdriver
from selenium.webdriver.edge.service import Service


def test_edge_browser():

    service = Service("./drivers/msedgedriver")

    driver = None

    try:
        print("Starting Microsoft Edge...")

        driver = webdriver.Edge(service=service)

        print("Opening Python.org...")
        driver.get("https://www.python.org")

        assert "Python" in driver.title

        print("Title:", driver.title)
        print("Edge automation successful!")

    finally:
        if driver:
            driver.quit()
