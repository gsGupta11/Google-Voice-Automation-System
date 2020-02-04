from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def formFill(driver):
    inpFields = driver.find_elements_by_xpath("//input[@type='text' or 'number' or 'url']")
    return inpFields