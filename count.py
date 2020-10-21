from selenium import webdriver

driver=webdriver.Chrome(executable_path="/home/dinesh/Downloads/chromedriver_linux64/chromedriver")
driver.get("https://www.cricbuzz.com/live-cricket-scorecard/23255/eng-vs-ire-2nd-odi-ireland-tour-of-england-2020")
div = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[2]/div[1]")

driver.close()