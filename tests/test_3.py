import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_registration(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/reg")
        username = driver.find_element(By.NAME, "username")
        email = driver.find_element(By.NAME, "email")
        password = driver.find_element(By.NAME, "password1")
        password2 = driver.find_element(By.NAME, "password2")
        username.send_keys("qqqez")
        email.send_keys("qqqez@yandex.ru")
        password.send_keys("qweasd123")
        password2.send_keys("qweasd123")
        password.send_keys(Keys.RETURN)
        time.sleep(5)
        self.assertIn("http://127.0.0.1:8000/directories", driver.current_url)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

