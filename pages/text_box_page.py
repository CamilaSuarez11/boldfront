from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TextBoxPage:
    def __init__(self, driver):
        self.driver = driver
        self.user_name_input = (By.ID, 'userName')
        self.user_email_input = (By.ID, 'userEmail')
        self.current_address_input = (By.ID, 'currentAddress')
        self.permanent_address_input = (By.ID, 'permanentAddress')
        self.submit_button = (By.XPATH, '//button[@id="submit"]')
        self.name_output = (By.XPATH, "//p[@id='name']")
        self.email_output = (By.XPATH, "//div[@class='mt-4 row']//div[@class='border']//p[2]")
        self.current_address_output = (By.XPATH, "//p[@id='currentAddress']")
        self.permanent_address_output = (By.XPATH, "//p[@id='permanentAddress']")

    def open(self):
        self.driver.get('https://demoqa.com/text-box')

    def fill_form(self, user_name, user_email, current_address, permanent_address):
        """Llena los campos del formulario"""
        self.driver.find_element(*self.user_name_input).send_keys(user_name)
        self.driver.find_element(*self.user_email_input).send_keys(user_email)
        self.driver.find_element(*self.current_address_input).send_keys(current_address)
        self.driver.find_element(*self.permanent_address_input).send_keys(permanent_address)

    def submit_form(self):
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.submit_button)
        )

        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

        submit_button.click()

        # Solo esperamos que los resultados sean visibles después de hacer clic en enviar
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.name_output)
        )

    def get_output(self):
        try:
            name = self.driver.find_element(*self.name_output).text.strip()
            email = self.driver.find_element(*self.user_email_input).text.strip()
            current_address = self.driver.find_element(*self.current_address_output).text.strip()
            permanent_address = self.driver.find_element(*self.permanent_address_output).text.strip()

            return name, email, current_address, permanent_address
        except Exception as e:
            print(f"Ocurrió un error al obtener los resultados: {e}")
            return None, None, None, None
