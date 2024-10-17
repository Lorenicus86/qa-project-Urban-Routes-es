import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


urban_routes_url = 'https://cnt-1bc1f8fe-0f06-40ee-a8ab-3a323bf8013a.containerhub.tripleten-services.com?lng=es'
address_from = 'East 2nd Street, 601'
address_to = '1300 1st St'
phone_number = '+1 123 123 12 12'
card_number, card_code = '1234 5678 9100', '111'
message_for_driver = 'Traiga un aperitivo'
