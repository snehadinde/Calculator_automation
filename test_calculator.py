from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By


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
    num1 = 423
    num2 = 525
    expected_result = 222075

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
    num1 = 4000
    num2 = 200
    expected_result = 20

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
    num1 = -234234
    num2 = 345345
    expected_result = 111111

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
    num1 = 234823
    num2 = -23094823
    expected_result = 23329646

    browser.find_element(By.XPATH,'/html/body').send_keys(num1)
    browser.find_element(By.XPATH,'//div[2]/span[4][@class="sciop"]').click()
    browser.find_element(By.XPATH,'/html/body').send_keys(num2)
    browser.find_element(By.XPATH,'//div[5]/span[4][@class="scieq"]').click()
    time.sleep(2)

    actual_result_str = browser.find_element(By.XPATH,'//div[2][@id="sciOutPut"]').text
    actual_result = int(actual_result_str)
    assert actual_result == expected_result

    browser.find_element(By.XPATH,'//div[5]/span[3][@class="scieq"]').click()

