from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# тестирование регистрации пользователя
class RegistrationTest(unittest.TestCase):

    def setUp(self):
        chromePath = "/Users/irinaarygina/Desktop/Тестирование ПО/kursovaya/chromedriver"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get("http://localhost:8081/registration")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    # регистрация пользователя
    def registration(self, username, usersecondname, email, password, password2):
        driver = self.driver

        driver.find_element_by_xpath("//*[@id=\"formName\"]").send_keys(username)
        driver.find_element_by_xpath("//*[@id=\"formSecondName\"]").send_keys(usersecondname)
        driver.find_element_by_xpath("//*[@id=\"inputEmail\"]").send_keys(email)
        driver.find_element_by_xpath("//*[@id=\"inputPassword\"]").send_keys(password)
        driver.find_element_by_xpath("//*[@id=\"inputPasswordRepeat\"]").send_keys(password2)
        time.sleep(1)
        regButton = driver.find_element_by_xpath("//*[@id=\"app\"]/section/main/div/div/button")
        regButton.click()
        time.sleep(2)

    # тест успешной регистрации пользователя
    def testRegistration(self):
        driver = self.driver
        self.registration("Ира", "Ярыгина", "edfgvdrh@mail.ru", "12345", "12345")
        self.assertEqual(driver.current_url, "http://localhost:8081/sign-in")

    # тест неправильной регистрации пользователя
    def testRegistrationError(self):
        driver = self.driver
        self.registration("Ира", "Ярыгина", "er@mail.ru", "12345", "123456789")

        # проверка появления диалогового окна с предупреждением
        wait = WebDriverWait(driver, 10)
        wait.until(EC.alert_is_present())
        alert = driver.switch_to.alert
        self.assertEqual(alert.text, "Пароли не совпадают")


if __name__ == '__main__':
    unittest.main()
