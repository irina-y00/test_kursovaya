from selenium import webdriver
import unittest
import time


# тестирование переходов на другие страницы с главной страницы
class CatalogTest(unittest.TestCase):
    def setUp(self):
        chromePath = "/Users/irinaarygina/Desktop/Тестирование ПО/kursovaya/chromedriver"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get("http://localhost:8081/catalog/")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    # переход на страницу фильма
    def testFilms(self):
        driver = self.driver
        filmsNames = ["Пираты Карибского моря: Мертвецы не рассказывают сказки", "Джокер", "Основатель"]
        for i in range(1, 4):
            film = driver.find_element_by_xpath(
                "//*[@id=\"app\"]/section/main/div/div/div/div[2]/div/div[{}]/div/h5/a".format(i))
            film.click()
            time.sleep(2)
            filmName = driver.find_element_by_class_name("film-title").text
            self.assertEqual(filmName, filmsNames[i - 1])
            driver.back()
            time.sleep(2)

    # проверка фильтра по категории при выборе чекбокса на примере категории "Драмы"
    def testCategory(self):
        driver = self.driver
        filmsNames = []
        checkbox = driver.find_element_by_id('Драмы')
        checkbox.click()
        time.sleep(2)
        buttonApply = driver.find_element_by_xpath("//*[@id=\"app\"]/section/main/div/div/div/div[1]/div/div/button")
        buttonApply.click()
        time.sleep(2)
        for element in driver.find_elements_by_class_name("film-name"):
            filmsNames.append(element.text)
        self.assertFalse("Пираты Карибского моря: Мертвецы не рассказывают сказки" in filmsNames)
        self.assertTrue("Джокер" in filmsNames)
        self.assertTrue("Основатель" in filmsNames)

    # проверка совместного использования фильтров при выборе двух чекбоксов
    def testCategoryFilling(self):
        driver = self.driver
        filmsNames = []
        checkbox = driver.find_element_by_id('Фэнтези')
        checkbox.click()
        time.sleep(1)
        checkbox = driver.find_element_by_id('Боевики')
        checkbox.click()
        time.sleep(1)
        buttonApply = driver.find_element_by_xpath("//*[@id=\"app\"]/section/main/div/div/div/div[1]/div/div/button")
        buttonApply.click()
        time.sleep(2)
        for element in driver.find_elements_by_class_name("film-name"):
            filmsNames.append(element.text)
        self.assertTrue(
            "Пираты Карибского моря: Мертвецы не рассказывают сказки" in filmsNames and len(filmsNames) == 1)


if __name__ == '__main__':
    unittest.main()
