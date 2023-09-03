from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from config import name, passw



#путь для нашего веб драйвера
service = Service(executable_path='./geckodriver.exe')

#объявлем переменную для дополнительных опций вроде user agent и тд
options = webdriver.FirefoxOptions()


driver = webdriver.Firefox(service=service, options=options)



try:
    #открываем в максимальном разрешении 
    driver.maximize_window()
    #переходим по ссылки
    driver.get('https://lk.irkat.ru/login')

    time.sleep(4)
    #делаем скриншот открывшего экрана
    
    
    #ищём поле для ввода логина
    login_input = driver.find_element(By.ID, 'input-24')
    #чистим поле для записи данных
    login_input.clear
    #вводим данные
    login_input.send_keys(name)
    time.sleep(3)



    #повторяем подобные функции с заполнением пароля 
    password_input = driver.find_element(By.ID, 'input-27')

    password_input.clear

    password_input.send_keys(passw)
    time.sleep(3)
    password_input.send_keys(Keys.ENTER)

    time.sleep(4)


    #заходим во вкладку с расписанием
    schedule = driver.find_element(By.XPATH, '/html/body/div[1]/div/nav/div[1]/div[2]/div[10]').click()
    time.sleep(5)
    #делаем скриншот с расписанием
    driver.save_screenshot('schedule.png')





except Exception as e:
    print(e)

finally:
    driver.close
    driver.quit


