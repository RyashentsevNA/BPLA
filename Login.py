from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# инициализируем драйвер браузера
driver = webdriver.Chrome()
driver.get("http://aisgin.dmz.test.ot/master/Account/Login")
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[5]/div/div/div/div[4]/button" ).click()
#Ввод логина
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[5]/div/div/div/div[5]/form/label[1]/span/input" ).send_keys("3")
#Ввод пароля
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[5]/div/div/div/div[5]/form/label[2]/span/input" ).send_keys("password123")
#Клик по "Войти"
driver.find_element(By.ID, "login-btn" ).click()
#паузаа
time.sleep(5)
mp= "Главная"
tests=driver.find_element(By.XPATH, "/html/body/nav/div[1]/ul/li[1]/a" ).text
if mp == tests:
    print('Test passed')
else:
    print('Test fail')
# закрыть браузер
driver.quit()