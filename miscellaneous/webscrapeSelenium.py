from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome("chromedriver")

driver.get("https://amazon.com")
driver.maximize_window()