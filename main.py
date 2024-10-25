import data
from selenium import webdriver
from UrbanRoutesPage import UrbanRoutesPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def get_routes_page(self):
        return UrbanRoutesPage(self.driver)

    def test_set_from_address(self):
        self.driver.get(data.urban_routes_url)
        routes_page = self.get_routes_page()

        address_from = data.address_from
        routes_page.set_from(address_from)

        assert routes_page.get_from() == address_from

    def test_set_to_address(self):
        routes_page = self.get_routes_page()
        address_to = data.address_to
        routes_page.set_to(address_to)

        assert routes_page.get_to() == address_to

    def test_select_comfort_tariff(self):
        routes_page = self.get_routes_page()
        routes_page.click_request_taxi_button()
        routes_page.click_comfort_sel()

        assert routes_page.is_comfort_selected()

    def test_fill_phone_number(self):
        routes_page = self.get_routes_page()
        routes_page.click_phone_field()
        phone_number = data.phone_number
        routes_page.set_phone(phone_number)
        routes_page.click_next_button()
        routes_page.set_code()
        routes_page.click_confirm_button()
        WebDriverWait(routes_page.driver, 10).until(EC.text_to_be_present_in_element(routes_page.phone_field, phone_number))
        assert routes_page.get_phone() == phone_number

    def test_fill_card_number(self):
        routes_page = self.get_routes_page()
        routes_page.click_payment_method_button()
        routes_page.click_plus_container_button()

        field_card = data.card_number
        routes_page.set_card(field_card)

        field_code_card = data.card_code
        routes_page.set_code_card(field_code_card)

        routes_page.press_tab()

        routes_page.click_add_button()
        routes_page.click_close_button()

        assert routes_page.get_card() == "Tarjeta"

    def test_message_for_driver(self):
        routes_page = self.get_routes_page()

        test_message = data.message_for_driver
        routes_page.set_message_for_driver(test_message)
        assert routes_page.get_message_for_driver() == test_message

    def test_select_manta_panuelos(self):
        routes_page = self.get_routes_page()
        routes_page.act_manta_panuelos()

        assert routes_page.is_manta_panuelos_selected()

    def test_order_helados(self):
        routes_page = self.get_routes_page()
        routes_page.double_click_helados_sel()

        assert routes_page.get_helados_count() == 2

    def test_display_taxi_modal(self):
        routes_page = self.get_routes_page()
        routes_page.click_busqueda_taxi_button()

        assert routes_page.is_taxi_modal_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
