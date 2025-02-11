import os
from selenium import webdriver

BASE_URL = "https://demoqa.com/text-box"


def create_driver():

    chromedriver_path = r"C:\Users\RentAdvisor\boldfront\drivers\chromedriver(package)\chromedriver.exe"

    if not os.path.exists(chromedriver_path):
        raise FileNotFoundError(f"El chromedriver no se encuentra en {chromedriver_path}")

    print(f"Usando chromedriver desde: {chromedriver_path}")

    driver = webdriver.Chrome(executable_path=chromedriver_path)
    driver.maximize_window()
    return driver
