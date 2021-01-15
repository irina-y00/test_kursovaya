from selenium import webdriver
import unittest
import time


# тестирование входа пользователя в профиль
class SignInTest(unittest.TestCase):

    def setUp(self):
        chromePath = "/Users/irinaarygina/Desktop/Тестирование ПО/kursovaya/chromedriver"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get("http://localhost:8081/sign-in")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    # переход на страницу регистрации по ссылке "Зарегестрироваться"
    def testGoReg(self):
        driver = self.driver
        buttonReg = driver.find_element_by_class_name("btn-sign")
        buttonReg.click()
        time.sleep(1)
        self.assertEqual(driver.current_url, "http://localhost:8081/registration")

    # вход пользователя на сайт
    def signIn(self, emale, password):
        driver = self.driver

        driver.find_element_by_xpath("//*[@id=\"email\"]").send_keys(emale)
        driver.find_element_by_xpath("//*[@id=\"password\"]").send_keys(password)
        time.sleep(1)
        signInButton = driver.find_element_by_xpath("//*[@id=\"app\"]/section/main/div/div/div[2]/form/button")
        signInButton.click()
        time.sleep(2)

    # тестирование успешного входа на сайт
    def testSignIn(self):
        driver = self.driver
        self.signIn("irina@mail.ru", "12345")
        self.assertEqual(driver.find_element_by_xpath("//*[@id=\"app\"]/section/main/div/div/h1[2]").text,
                         "irina@mail.ru")


if __name__ == '__main__':
    unittest.main()
