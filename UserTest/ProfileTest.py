from selenium import webdriver
import unittest
import time


# тестирование страницы профиля
class ProfileTest(unittest.TestCase):

    def setUp(self):
        chromePath = "/Users/irinaarygina/Desktop/Тестирование ПО/kursovaya/chromedriver"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get("http://localhost:8081/profile")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    # проверка перехода на страницы входа и регистрации по кнопкам, если пользователь еще не авторизовался
    def testProfilePage(self):
        driver = self.driver

        buttonSignIn = driver.find_element_by_xpath("//*[@id=\"app\"]/section/main/div/div/p[2]/button[1]")
        buttonSignIn.click()
        time.sleep(1)
        self.assertEqual(driver.current_url, "http://localhost:8081/sign-in")
        time.sleep(2)
        driver.back()
        time.sleep(2)

        buttonRegistration = driver.find_element_by_xpath("//*[@id=\"app\"]/section/main/div/div/p[2]/button[2]")
        buttonRegistration.click()
        time.sleep(1)
        self.assertEqual(driver.current_url, "http://localhost:8081/registration")
        time.sleep(2)
        driver.back()

    # выход из профиля пользователя по кнопке "Выход"
    def testExit(self):
        driver = self.driver
        buttonSignIn = driver.find_element_by_xpath("//*[@id=\"app\"]/section/main/div/div/p[2]/button[1]")
        buttonSignIn.click()
        time.sleep(1)

        # вход пользователя
        driver.find_element_by_xpath("//*[@id=\"email\"]").send_keys("irina@mail.ru")
        driver.find_element_by_xpath("//*[@id=\"password\"]").send_keys("12345")
        time.sleep(1)
        signInButton = driver.find_element_by_xpath("//*[@id=\"app\"]/section/main/div/div/div[2]/form/button")
        signInButton.click()
        time.sleep(2)

        # выход пользователя
        buttonExit = driver.find_element_by_xpath("//*[@id=\"app\"]/section/main/div/div/button")
        buttonExit.click()
        time.sleep(2)
        self.assertEqual(driver.find_element_by_xpath("//*[@id=\"app\"]/section/main/div/div/h2").text,
                         "К сожалению, вы еще не зашли.")


if __name__ == '__main__':
    unittest.main()