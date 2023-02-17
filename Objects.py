from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Objects import Object
# инициализируем драйвер браузера
driver = webdriver.Chrome()


class Object:

#Реестр заданий на облет
    Reetr_zadan = driver.find_element(By.LINK_TEXT, "Реестр заданий на облет")
    Dobavit_zapis = driver.find_element(By.XPATH, "//span[contains(text(),'Добавить запись')]")