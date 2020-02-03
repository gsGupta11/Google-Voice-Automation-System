from selenium import webdriver
def getLinkname(driver):
    a = driver.find_elements_by_xpath("//*[@href]")
    return a