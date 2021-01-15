from selenium import webdriver
import unittest
import time


# тестирование переходов на другие страницы с главной страницы
class FilmsTest(unittest.TestCase):
    def setUp(self):
        chromePath = "/Users/irinaarygina/Desktop/Тестирование ПО/kursovaya/chromedriver"
        self.driver = webdriver.Chrome(executable_path=chromePath)
        self.driver.get("http://localhost:8081/")
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    # переход к товарам из раздела "рекомендуем вам" по нажатию на "смотреть подробнее"
    def testHitFilmsByGo(self):
        driver = self.driver
        filmNames = ["Пираты Карибского моря: Мертвецы не рассказывают сказки", "Джокер", "Основатель"]
        for i in range(1, 4):
            hitFilm = driver.find_element_by_xpath(
                "//*[@id=\"app\"]/section/main/div/div[2]/div/div[{}]/div/div/a".format(i))
            hitFilm.click()
            time.sleep(2)
            filmName = driver.find_element_by_class_name("film-title").text
            self.assertEqual(filmName, filmNames[i - 1])
            driver.back()
            time.sleep(2)


if __name__ == '__main__':
    unittest.main()
