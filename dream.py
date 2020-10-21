from selenium import webdriver
import pymongo

# import time
# from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/home/dinesh/Downloads/chromedriver_linux64/chromedriver")

driver.get("https://www.cricbuzz.com/live-cricket-scorecard/23255/eng-vs-ire-2nd-odi-ireland-tour-of-england-2020")

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myClient["dream"]
col = db["teams"]
batsman = []
bowler = []

team = "Ireland"

# battingUrl = "/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[2]/div[1]/div["
# bowlingUrl = "/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[2]/div[4]/div["

battingUrl="/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[3]/div[1]/div["
bowlingUrl="/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[3]/div[4]/div["

batsmanCount = 8
bowlerCount = 5

matchUrl = "/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[4]/div[2]/div[1]/div[2]"
dateUrl = "/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[4]/div[2]/div[2]/div[2]/span[1]"
venueUrl = "/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[4]/div[2]/div[5]/div[2]"
tossUrl = "/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[4]/div[2]/div[3]/div[2]"
timeUrl = "/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[4]/div[2]/div[4]/div[2]/span[1]"

for x in range(batsmanCount):
    y = str(3 + x)
    batsmanUrl = battingUrl + y + "]";
    print("batsman", batsmanUrl);
    nameUrl = batsmanUrl + "/div[1]";
    outByUrl = batsmanUrl + "/div[2]/span[1]"
    runUrl = batsmanUrl + "/div[3]"
    ballUrl = batsmanUrl + "/div[4]"
    fourUrl = batsmanUrl + "/div[5]"
    sixUrl = batsmanUrl + "/div[6]"
    srUrl = batsmanUrl + "/div[7]"

    # print("url",batsmanurl)

    player = driver.find_element_by_xpath(nameUrl)
    outBy = driver.find_element_by_xpath(outByUrl)
    run = driver.find_element_by_xpath(runUrl)
    ball = driver.find_element_by_xpath(ballUrl)
    four = driver.find_element_by_xpath(fourUrl)
    six = driver.find_element_by_xpath(sixUrl)
    sr = driver.find_element_by_xpath(srUrl)

    # print(player.text,outby.text,run.text,four.text,six.text)
    data = {
        "name": player.text,
        "outby": outBy.text,
        "runs": int(run.text),
        "balls": int(ball.text),
        "four": int(four.text),
        "six": int(six.text),
        "strickrate": float(sr.text)
    }
    batsman.append(data)

for x in range(bowlerCount):
    y = str(x + 2)
    bowlerUrl = bowlingUrl + y + "]"
    print("bowler", bowlerUrl)
    nameUrl = bowlerUrl + "/div[1]"
    overUrl = bowlerUrl + "/div[2]"
    maidenUrl = bowlerUrl + "/div[3]"
    runUrl = bowlerUrl + "/div[4]"
    wicketUrl = bowlerUrl + "/div[5]"
    economyUrl = bowlerUrl + "/div[8]"

    name = driver.find_element_by_xpath(nameUrl)
    over = driver.find_element_by_xpath(overUrl)
    maiden = driver.find_element_by_xpath(maidenUrl)
    run = driver.find_element_by_xpath(runUrl)
    wicket = driver.find_element_by_xpath(wicketUrl)
    economy = driver.find_element_by_xpath(economyUrl)

    data = {
        "name": name.text,
        "over": float(over.text),
        "maiden": int(maiden.text),
        "runs": int(run.text),
        "wickets": int(wicket.text),
        "economy": float(economy.text)
    }
    bowler.append(data)

match = driver.find_element_by_xpath(matchUrl)
date = driver.find_element_by_xpath(dateUrl)
venue = driver.find_element_by_xpath(venueUrl)
toss = driver.find_element_by_xpath(tossUrl)
time = driver.find_element_by_xpath(timeUrl)

insertData = {
    "match": match.text,
    "date": date.text,
    "time": time.text,
    "venue": venue.text,
    "toss": toss.text,
    "team": team,
    "batsman": batsman,
    "bowler": bowler
}

print("InsertData", insertData)
insert = col.insert_one(insertData)

driver.close()
