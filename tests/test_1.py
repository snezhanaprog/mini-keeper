import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        self.assertIn("Всё здесь", driver.title)

    def test_login(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/auth")
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        username.send_keys("admin")
        password.send_keys("0000")
        password.send_keys(Keys.RETURN)
        self.assertIn("http://127.0.0.1:8000/directories", driver.current_url)

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
        #self.assertIn("http://127.0.0.1:8000/directories", driver.current_url)

    def test_add_directory_with_auth(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/auth")
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        username.send_keys("admin")
        password.send_keys("0000")
        password.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/directory/add/")
        name = driver.find_element(By.NAME, "name")
        parent = driver.find_element(By.NAME, "parent")
        type = driver.find_element(By.NAME, "type")
        submit_button = driver.find_element(By.ID, "form-add__btn")
        name_input = "directory_name"
        type_input = "public"
        parent_input = 1
        name.send_keys(name_input)
        parent.send_keys(parent_input)
        type.send_keys(type_input)
        submit_button.click()
        time.sleep(5)

    def test_url_with_auth(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/auth")
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        username.send_keys("admin")
        password.send_keys("0000")
        password.send_keys(Keys.RETURN)
        time.sleep(5)

        a_main = driver.find_element(By.NAME, "main")
        a_main.click()
        time.sleep(2)
        a_my_keeper = driver.find_element(By.NAME, "my_keeper")
        a_my_keeper.click()
        time.sleep(2)
        a_other_keeper = driver.find_element(By.NAME, "other_keeper")
        a_other_keeper.click()
        time.sleep(2)
        a_exit = driver.find_element(By.NAME, "exit")
        a_exit.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

