from selenium import webdriver

driver= webdriver.Chrome()

driver.get("https://www.nike.com.br/")

driver.maximize_window()

driver.quit()