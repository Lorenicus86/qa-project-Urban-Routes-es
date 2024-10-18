import data
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from localizadores import from_field, to_field

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver
        self.from_field = from_field  # Asignar from_field a un atributo de la instancia
        self.to_field = to_field      # Asignar to_field a un atributo de la instancia

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_personal(self, personal_click):
        self.driver.find_element(*self.personal_sel).click()
        time.sleep(10)