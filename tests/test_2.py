import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/auth")
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        username.send_keys("admin")
        password.send_keys("0000")
        password.send_keys(Keys.RETURN)
        self.assertIn("http://127.0.0.1:8000/directories", driver.current_url)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

