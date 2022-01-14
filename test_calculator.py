from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
import json

result = json.load(open('testdata.json','r'))



@pytest.fixture(scope="module")
def setup():
    global browser
    browser = webdriver.Chrome(executable_path='./chromedriver/chromedriver.exe')
    browser.get('https://www.calculator.net/')
    browser.maximize_window()
    time.sleep(2)
    yield
    browser.close()

def test_multiplication(setup):
    value = result.get('multiplication')
    num1 = value[0]
    num2 = value[1]
    expected_result = value[2]

    browser.find_element(By.XPATH,'/html/body').send_keys(num1)
    browser.find_element(By.XPATH, '//div[3]/span[4][@class="sciop"]').click()  #multiplication key
    browser.find_element(By.XPATH,'/html/body').send_keys(num2)
    browser.find_element(By.XPATH,'//div[5]/span[4][@class="scieq"]').click()

    time.sleep(2)
    actual_result_str= browser.find_element(By.XPATH,'//div[2][@id="sciOutPut"]').text
    actual_result = int(actual_result_str)
    assert expected_result == actual_result

    browser.find_element(By.XPATH,'//div[5]/span[3][@class="scieq"]').click()   #all clear(AC) key

def test_division(setup):
    value = result.get('division')
    num1 = value[0]
    num2 = value[1]
    expected_result = value[2]

    browser.find_element(By.XPATH,'/html/body').send_keys(num1)
    browser.find_element(By.XPATH,'//div[4]/span[4][@class="sciop"]').click()   #division key
    browser.find_element(By.XPATH,'/html/body').send_keys(num2)
    browser.find_element(By.XPATH,'//div[5]/span[4][@class="scieq"]').click()

    time.sleep(2)
    actual_result_str = browser.find_element(By.XPATH,'//div[2][@id="sciOutPut"]').text
    actual_result = int(actual_result_str)
    assert actual_result == expected_result

    browser.find_element(By.XPATH,'//div[5]/span[3][@class="scieq"]').click()

def test_addition(setup):
    value = result.get('addition')
    num1 = value[0]
    num2 = value[1]
    expected_result = value[2]

    browser.find_element(By.XPATH,'/html/body').send_keys(num1)
    browser.find_element(By.XPATH,'//div[1]/span[4][@class="sciop"]').click()  #addition key
    browser.find_element(By.XPATH,'/html/body').send_keys(num2)
    browser.find_element(By.XPATH,'//div[5]/span[4][@class="scieq"]').click()

    time.sleep(2)
    actual_result_str = browser.find_element(By.XPATH,'//div[2][@id="sciOutPut"]').text
    actual_result = int(actual_result_str)
    assert actual_result == expected_result

    browser.find_element(By.XPATH,'//div[5]/span[3][@class="scieq"]').click()

def test_subtraction(setup):
    value = result.get('subtraction')
    num1 = value[0]
    num2 = value[1]
    expected_result = value[2]

    browser.find_element(By.XPATH,'/html/body').send_keys(num1)
    browser.find_element(By.XPATH,'//div[2]/span[4][@class="sciop"]').click()
    browser.find_element(By.XPATH,'/html/body').send_keys(num2)
    browser.find_element(By.XPATH,'//div[5]/span[4][@class="scieq"]').click()
    time.sleep(2)

    actual_result_str = browser.find_element(By.XPATH,'//div[2][@id="sciOutPut"]').text
    actual_result = int(actual_result_str)
    assert actual_result == expected_result

    browser.find_element(By.XPATH,'//div[5]/span[3][@class="scieq"]').click()

