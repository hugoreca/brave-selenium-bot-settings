from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# *************** Selenium set-up variables ***************

# The location where the .exe of your browser is located
BINARY_LOCATION = "C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe"

# The path of the chromedriver.exe, this file is requisite for the bot to be initialized
PATH = "C:\Development\chromedriver.exe"

# Options object so we can 'trick' selenium to think that Brave is Google Chrome
options = Options()
options.binary_location = BINARY_LOCATION
driver = webdriver.Chrome(options=options, executable_path=PATH)

# *************** Selenium set-up variables ***************

#The URL you want to browse
URL = "https://www.google.com/"

#Open the browser at the forms url
driver.get(URL)