from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from codigo import retrieve_phone_code
from selenium.webdriver.common.action_chains import ActionChains

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.from_field = (By.ID, 'from')
        self.to_field = (By.ID, 'to')
        self.request_taxi_button = (By.XPATH, '//button[text()="Pedir un taxi"]')
        self.comfort_sel = (By.XPATH, '(//img[@alt="Comfort"])[1]')
        self.comfort_val = (By.XPATH, "//div[contains(text(), 'Manta y pañuelos')]")
        self.phone_field = (By.CLASS_NAME, 'np-text')
        self.phone_field_input = (By.ID, 'phone')
        self.next_button = (By.CSS_SELECTOR, ".button.full")
        self.code_field = (By.XPATH, "//input[@id='code' and @class='input']")
        self.confirm_button = (By.XPATH, '//button[text()="Confirmar"]')
        self.payment_method_button = (By.CLASS_NAME, 'pp-value-text')
        self.plus_container_button = (By.CLASS_NAME, 'pp-plus-container')
        self.card_field = (By.ID, 'number')
        self.code_card_field = (By.XPATH, "//input[@id='code' and @name='code']")
        self.add_card_button = (By.XPATH, "//div[@class='head' and text()='Agregar tarjeta']")
        self.add_button = (By.XPATH, '//button[text()="Agregar"]')
        self.close_button = (By.XPATH, "(//button[@class='close-button section-close'])[3]")
        self.message_for_driver_field = (By.XPATH, '//input[@id="comment"]')
        self.manta_panuelos = (By.XPATH, '//span[@class="slider round"][1]')
        self.manta_panuelos_sel = (By.CSS_SELECTOR, "input.switch-input")
        self.helados_sel = (By.CSS_SELECTOR, '.counter-plus')
        self.busqueda_taxi_button = (By.CSS_SELECTOR, '.smart-button-secondary')
        self.car_image = (By.CSS_SELECTOR, "img[alt='Car'][src='/static/media/kids.075fd8d4.svg']")
        self.add_helados_value=(By.CSS_SELECTOR, '.counter-value')

    def set_from(self, from_address):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.from_field))
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.to_field))
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_request_taxi_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.request_taxi_button))
        self.driver.find_element(*self.request_taxi_button).click()

    def click_comfort_sel(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.comfort_sel))
        self.driver.find_element(*self.comfort_sel).click()

    def is_comfort_selected(self):
        return self.driver.find_element(*self.comfort_val).is_displayed()

    def click_phone_field(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.phone_field))
        self.driver.find_element(*self.phone_field).click()

    def set_phone(self, input_phone_field):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.phone_field_input))
        self.driver.find_element(*self.phone_field_input).send_keys(input_phone_field)

    def get_phone(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.phone_field))
        return self.driver.find_element(*self.phone_field).text

    def click_next_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.next_button))
        self.driver.find_element(*self.next_button).click()

    def set_code(self):
        code = retrieve_phone_code(self.driver)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.code_field))
        self.driver.find_element(*self.code_field).send_keys(code)

    def get_code(self):
        return self.driver.find_element(*self.code_field).get_property('value')

    def click_confirm_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.confirm_button))
        self.driver.find_element(*self.confirm_button).click()

    def click_payment_method_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.payment_method_button))
        self.driver.find_element(*self.payment_method_button).click()

    def click_plus_container_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.plus_container_button))
        self.driver.find_element(*self.plus_container_button).click()

    def set_card(self, field_card):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.card_field))
        self.driver.find_element(*self.card_field).send_keys(field_card)

    def get_card(self):
        return self.driver.find_element(*self.payment_method_button).text

    def set_code_card(self, field_code_card):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.code_card_field))
        self.driver.find_element(*self.code_card_field).send_keys(field_code_card)

    def get_code_card(self):
        return self.driver.find_element(*self.code_card_field).get_property('value')

    def press_tab(self):
        actions = ActionChains(self.driver)
        actions.send_keys("\u0009")  # "\u0009" código Unicode para Tab
        actions.perform()

    def click_add_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_button))
        self.driver.find_element(*self.add_button).click()

    def click_close_button(self):
        close_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.close_button)
        )
        close_button.click()

    def set_message_for_driver(self, field_message_for_driver):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.message_for_driver_field))
        self.driver.find_element(*self.message_for_driver_field).send_keys(field_message_for_driver)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.message_for_driver_field).get_property('value')

    def act_manta_panuelos(self):
        slider = self.driver.find_element(*self.manta_panuelos)
        action = ActionChains(self.driver)
        action.click_and_hold(slider).move_by_offset(20, 0).release().perform()

    def is_manta_panuelos_selected(self):
        manta_element = self.driver.find_element(*self.manta_panuelos_sel)
        return manta_element.is_selected()

    def double_click_helados_sel(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.helados_sel))
        action = ActionChains(self.driver)
        action.double_click(element).perform()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(self.add_helados_value, "2"))

    def get_helados_count(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.add_helados_value)
        )
        count_text = self.driver.find_element(*self.add_helados_value).text
        return int(count_text) if count_text.isdigit() else 0

    def click_busqueda_taxi_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.busqueda_taxi_button))
        self.driver.find_element(*self.busqueda_taxi_button).click()

    def is_taxi_modal_displayed(self):
        WebDriverWait(self.driver, 40).until(
            EC.visibility_of_element_located(self.car_image)
        )
        return self.driver.find_element(*self.car_image).is_displayed()