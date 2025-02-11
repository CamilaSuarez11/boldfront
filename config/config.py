import os
from selenium import webdriver

BASE_URL = "https://demoqa.com/text-box"


def create_driver():
    """Configura el driver para Selenium apuntando a la ubicación local de chromedriver"""

    # Ruta completa a chromedriver.exe
    chromedriver_path = r"C:\Users\RentAdvisor\boldfront\drivers\chromedriver(package)\chromedriver.exe"

    # Verificar si el chromedriver existe en la ruta proporcionada
    if not os.path.exists(chromedriver_path):
        raise FileNotFoundError(f"El chromedriver no se encuentra en {chromedriver_path}")

    print(f"Usando chromedriver desde: {chromedriver_path}")

    # Crear una instancia del navegador con el chromedriver local
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    driver.maximize_window()
    return driver
