# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestFAceboooooooooooooooook2():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testFAceboooooooooooooooook2(self):
    self.driver.get("https://egc-guadalquivir-vis.herokuapp.com/visualizer/2/")
    self.driver.set_window_size(1298, 863)
    self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(1) > img").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".\\_51m-:nth-child(2)").text == "Compartir en Facebook"
  