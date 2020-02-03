from selenium import webdriver
def getBtn(driver):
    a=driver.find_element_by_tag_name("button")
    return a
    # TOdo - type-btn waale bhi rakhne hn 