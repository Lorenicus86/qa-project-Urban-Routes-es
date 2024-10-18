from os import close

import data
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from codigo import retrieve_phone_code
from localizadores import from_field, to_field, request_taxi_button, comfort_sel, phone_field, phone_field_input, \
    next_button, code_field, confirm_button, payment_method_button, plus_container_button, card_field, code_card_field, \
    add_button, close_button, message_for_driver_field, manta_panuelos, helados_sel, busqueda_taxi_button
from selenium.webdriver.common.action_chains import ActionChains


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.from_field = from_field
        self.to_field = to_field
        self.request_taxi_button = request_taxi_button
        self.comfort_sel = comfort_sel
        self.phone_field = phone_field
        self.phone_field_input = phone_field_input
        self.next_button = next_button
        self.code_field = code_field
        self.confirm_button = confirm_button
        self.payment_method_button = payment_method_button
        self.plus_container_button = plus_container_button
        self.card_field=card_field
        self.code_card_field=code_card_field
        self.add_button=add_button
        self.close_button=close_button
        self.message_for_driver_field=message_for_driver_field
        self.manta_panuelos=manta_panuelos
        self.helados_sel=helados_sel
        self.busqueda_taxi_button=busqueda_taxi_button

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_request_taxi_button(self):
        time.sleep(5)
        self.driver.find_element(*self.request_taxi_button).click()

    def click_comfort_sel(self):
        time.sleep(5)
        self.driver.find_element(*self.comfort_sel).click()

    def click_phone_field(self):
        time.sleep(5)
        self.driver.find_element(*self.phone_field).click()

    def set_phone(self, input_phone_field):
        self.driver.find_element(*self.phone_field_input).send_keys(input_phone_field)

    def get_phone(self):
        return self.driver.find_element(*self.phone_field_input).get_property('value')

    def click_next_button(self):
        time.sleep(5)
        self.driver.find_element(*self.next_button).click()

    def set_code(self):
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.code_field).send_keys(code)

    def get_code(self):
        return self.driver.find_element(*self.code_field).get_property('value')

    def click_confirm_button(self):
        time.sleep(5)
        self.driver.find_element(*self.confirm_button).click()

    def click_payment_method_button(self):
        time.sleep(5)
        self.driver.find_element(*self.payment_method_button).click()

    def click_plus_container_button(self):
        time.sleep(5)
        self.driver.find_element(*self.plus_container_button).click()

    def set_card(self, field_card):
        self.driver.find_element(*self.card_field).send_keys(field_card)

    def get_card(self):
        return self.driver.find_element(*self.card_field).get_property('value')

    def set_code_card(self, field_code_card):
        self.driver.find_element(*self.code_card_field).send_keys(field_code_card)

    def get_code_card(self):
        return self.driver.find_element(*self.code_card_field).get_property('value')

    def press_tab(self):
        actions = ActionChains(self.driver)
        actions.send_keys("\u0009")  # "\u0009" código Unicode para Tab
        actions.perform()

    def click_add_button(self):
        time.sleep(5)
        self.driver.find_element(*self.add_button).click()

    def click_close_button(self):
        close_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.close_button)
        )
        close_button.click()

    def set_message_for_driver(self, field_message_for_driver):
        self.driver.find_element(*self.message_for_driver_field).send_keys(field_message_for_driver)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.message_for_driver_field).get_property('value')

    def act_manta_panuelos(self):
        # Encuentra el elemento del slider
        slider = self.driver.find_element(*self.manta_panuelos)

        # Crea una acción para mover el slider
        action = ActionChains(self.driver)
        action.click_and_hold(slider).move_by_offset(20, 0).release().perform()

    def double_click_helados_sel(self):
        time.sleep(5)

        element = self.driver.find_element(*self.helados_sel)  # Encuentra el elemento
        action = ActionChains(self.driver)  # Inicializa ActionChains
        action.double_click(element).perform()  # Realiza el doble clic

    def click_busqueda_taxi_button(self):
        time.sleep(5)
        self.driver.find_element(*self.busqueda_taxi_button).click()