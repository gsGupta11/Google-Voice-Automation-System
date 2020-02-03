import time
from selenium import webdriver
def clickLink(driver,c):
    links = driver.find_elements_by_xpath("//h3[@class='LC20lb'or'r']")
    links[c].click()