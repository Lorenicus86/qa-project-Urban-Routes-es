import data
from selenium import webdriver
import time
from codigo import  retrieve_phone_code

from data import phone_number, card_number
from localizadores import phone_field
from metodos import UrbanRoutesPage

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        time.sleep(3)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        routes_page.click_request_taxi_button()
        routes_page.click_comfort_sel()
        routes_page.click_phone_field()
        phone_number = data.phone_number
        routes_page.set_phone(phone_number)
        assert routes_page.get_phone() == phone_number
        routes_page.click_next_button()
        routes_page.set_code()
        routes_page.click_confirm_button()
        routes_page.click_payment_method_button()
        routes_page.click_plus_container_button()

        time.sleep(3)

        field_card = data.card_number
        routes_page.set_card(field_card)
        assert routes_page.get_card() == field_card
        field_code_card = data.card_code
        routes_page.set_code_card(field_code_card)
        assert routes_page.get_code_card() == field_code_card
        routes_page.press_tab()
        time.sleep(3)
        routes_page.click_add_button()

        time.sleep(3)
        routes_page.click_close_button()
        time.sleep(3)

        field_message_for_driver = data.message_for_driver
        routes_page.set_message_for_driver(field_message_for_driver)
        assert routes_page.get_message_for_driver() == field_message_for_driver
        time.sleep(3)
        routes_page.act_manta_panuelos()
        time.sleep(3)
        routes_page.double_click_helados_sel()
        time.sleep(3)
        routes_page.click_busqueda_taxi_button()
        time.sleep(50)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
