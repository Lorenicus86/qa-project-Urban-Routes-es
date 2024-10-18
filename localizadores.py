from pydoc import classname

from selenium.webdriver.common.by import By

from data import message_for_driver

from_field = (By.ID, 'from')
to_field = (By.ID, 'to')
request_taxi_button = (By.XPATH, '//button[text()="Pedir un taxi"]')
comfort_sel = (By.XPATH, '(//img[@alt="Comfort"])[1]')
phone_field = (By.CSS_SELECTOR, ".np-text")
phone_field_input = (By.ID, 'phone')
next_button = (By.CSS_SELECTOR, ".button.full")
code_field = (By.XPATH, "//input[@id='code' and @class='input']")
confirm_button = (By.XPATH, '//button[text()="Confirmar"]')
payment_method_button = (By.CLASS_NAME, 'pp-value-text')
plus_container_button = (By.CLASS_NAME, 'pp-plus-container')
card_field=(By.ID, 'number')
code_card_field=(By.XPATH, "//input[@id='code' and @name='code']")
anywhere_click=(By.XPATH, "//div[@class='head' and text()='Agregar tarjeta']")
add_button=(By.XPATH, '//button[text()="Agregar"]')
close_button=(By.XPATH, "(//button[@class='close-button section-close'])[3]")
message_for_driver_field=(By.XPATH, '//input[@id="comment"]')
manta_panuelos=(By.XPATH, '//span[@class="slider round"][1]')
helados_sel=(By.CSS_SELECTOR, '.counter-plus')
busqueda_taxi_button=(By.CSS_SELECTOR, '.smart-button-secondary')