import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Search(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        self.assertIn("Всё здесь", driver.title)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

