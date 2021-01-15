from selenium import webdriver
import unittest
import time


# тестирование навбара для всех страниц
class NavbarTest(unittest.TestCase):
    def setUp(self):
        chromePath = "/Users/irinaarygina/Desktop/Тестирование ПО/kursovaya/chromedriver"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get("http://localhost:8081/")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    # переход по страницам навбара
    def testNavbarPages(self):
        driver = self.driver
        pagesNameArray = ["Профиль", "Каталог"]
        for i in range(1, 3):
            pageButton = driver.find_element_by_xpath("//*[@id=\"navbarSupportedContent\"]/ul/li[{}]/a".format(i))
            pageButton.click()
            time.sleep(1)
            title_name = driver.find_element_by_class_name("page-title").text
            self.assertEqual(title_name, pagesNameArray[i - 1])

        pageName = "Авторизация"
        pageButton = driver.find_element_by_xpath("//*[@id =\"navbarSupportedContent\"]/form/div/a")
        pageButton.click()
        time.sleep(1)
        title_name = driver.find_element_by_class_name("text-sign").text
        self.assertEqual(title_name, pageName)

        pageName = "Регистрация"
        pageButton = driver.find_element_by_xpath("//*[@id =\"navbarSupportedContent\"]/form/a")
        pageButton.click()
        time.sleep(1)
        title_name = driver.find_element_by_class_name("text-register").text
        self.assertEqual(title_name, pageName)


if __name__ == '__main__':
    unittest.main()
