from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# инициализируем драйвер браузера
driver = webdriver.Chrome()
driver.set_window_size(1920,1080)
# неявное ожидание
# driver.implicitly_wait(60)
driver.get("http://aisgin.dmz.test.ot/master/Account/Login")
driver.find_element(By.ID, "forms-auth-btn" ).click()
#Ввод логина
driver.find_element(By.ID, "Login" ).send_keys("3")
#Ввод пароля
driver.find_element(By.ID, "Password" ).send_keys("password123")
#Клик "Войти"
driver.find_element(By.ID, "login-btn" ).click()
#Нажимает реестр заданий на облет
WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Реестр заданий на облет" ))).click()
time.sleep(20)
#Нажимает Добавить запись

WebDriverWait(driver, 160).until(expected_conditions.presence_of_element_located((By.XPATH, "//tbody/tr[2]/td[1]" )))
try:
    elementik = WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Добавить запись')]" )))
finally:
    elementik.click()
#Выбор ОКРУГА
driver.find_element(By.ID, "realestateAo").click()
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[1]/div/div/div[1]" ).click()
time.sleep(2)
#Тип облета
driver.find_element(By.CLASS_NAME, "ant-radio-input" ).click()
time.sleep(2)
#Вид съемки
driver.find_element(By.XPATH, "/html/body/div/section/section/main/div/div/div[2]/div[1]/div[1]/div[2]/div/form/div[3]/div/div[2]/div/div/div/label[1]/span[1]/input" ).click()
driver.find_element(By.XPATH, "/html/body/div/section/section/main/div/div/div[2]/div[1]/div[1]/div[2]/div/form/div[3]/div/div[2]/div/div/div/label[2]/span[1]/input" ).click()
time.sleep(2)
#Кадастровый номер
driver.find_element(By.ID, "realestateNfKadastralNumber" ).send_keys("77:77:7777777:777777")
time.sleep(2)
#Адрес
driver.find_element(By.XPATH, "//input[@id='realestateNfAddress']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='realestateNfAddress']" ).send_keys("Автотест")

#Планируемый срок облета
driver.find_element(By.XPATH, "/html/body/div[1]/section/section/main/div/div/div[2]/div[1]/div[1]/div[2]/div/form/div[7]/div/div/div/div/div/div/div[2]/div/div/div/div/input").click()
time.sleep(3)

#Нажать кнопку сохранить
element = driver.find_element(By.XPATH, "//span[contains(text(),'Сохранить')]")
driver.execute_script("arguments[0].scrollIntoView();", element)
driver.find_element(By.XPATH, "//span[contains(text(),'Сохранить')]").click()
time.sleep(5)


#Проверка на элемент: статус Запланировано и план полета
status = driver.find_element(By.XPATH, "//span[contains(text(),'Запланировано')]").text
plan = driver.find_element(By.XPATH, "//a[contains(text(),'План полета')]").text
status_obleta='Запланировано'
flightplan = 'План полета'
if status == status_obleta and flightplan ==plan:
    print('Тест пройден')
else:
    print('Все сломалось')


# Это можно сделать через класс expected_conditions. Нужно указать его, а потом через точку — само условие. Частые условия:
# element_to_be_clickable — элемент кликабелен.
# presence_of_element_located — ожидает наличие элемента на странице.
# visibility_of_element_located — проверяет, что элемент есть на странице и его видно.
# # Ожидание, что кнопка станет кликабельной, не больше 3 секунд
# #WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.TAG_NAME, "button")))

#By.CLASS_NAME # поиск по наименованию атрибута class
#By.CSS_SELECTOR # поиск по CSS-селектору
#By.ID # поиск по атрибуту id
#By.LINK_TEXT # поиск по тексту ссылки (имеется в виду не сама ссылка вида https://..., а текст внутри объекта ссылки, в следующем уроке будет пример
#By.PARTIAL_LINK_TEXT # поиск по части текста ссылки, то же условие, что и для By.linkText(text)
#y.NAME # поиск по атрибуту name
# By.TAG_NAME # поиск по HTML-тегу
# By.XPATH # поиск по XPath