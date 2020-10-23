from selenium import webdriver
import pymongo

# import time
# from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/home/spe/Desktop/python/dream11/chromedriver/chromedriver")

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myClient["ipl"]
col = db["play"]
batsman = []
bowler = []
batsman2 = []
bowler2 = []

codearr = ["30449/rcb-vs-kxip-31st","30450/mi-vs-kkr-32nd"]
teamarr = ["RCB","KKR"]
batsmanCountarr = [8,7]
bowlerCountarr = [6,5]
team2arr = ["KXIP","MI"]
batsmanCount2arr = [4,4]
bowlerCount2arr =  [6,6]


# ##############################  url and match   #################################
# code = "30445/dc-vs-rr-30th"

# ##############################    Match Link    #################################
# Commentary = "https://www.cricbuzz.com/cricket-scores/"+code+"-match-indian-premier-league-2020"               
# Scorecard = "https://www.cricbuzz.com/live-cricket-scorecard/"+code+"-match-indian-premier-league-2020"


# ##########################     First Off      ###################################
# team = "DC"
# batsmanCount = 8
# bowlerCount = 6
# battingUrl = "/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[2]/div[1]/div["               
# bowlingUrl = "/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[2]/div[4]/div["


# ##########################     Second Off      ###################################
# team2 = "RR"
# batsmanCount2 = 9
# bowlerCount2 =  5
# battingUrl2 = "/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[3]/div[1]/div["            
# bowlingUrl2 = "/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[3]/div[4]/div["
#             #    /html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[3]/div[4]/div[2]/div[1] 
#             #    /html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[3]/div[2]/div[2]/div[1]/a[1]


##########################      GET Score and Man of the match  ###################################
for d in range(len(codearr)):
    Commentary = "https://www.cricbuzz.com/cricket-scores/"+codearr[d]+"-match-indian-premier-league-2020"               
    Scorecard = "https://www.cricbuzz.com/live-cricket-scorecard/"+codearr[d]+"-match-indian-premier-league-2020"


# ##########################     First Off      ###################################
    team = teamarr[d]
    batsmanCount = batsmanCountarr[d]
    bowlerCount = bowlerCountarr[d]
    battingUrl = "/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[2]/div[1]/div["               
    bowlingUrl = "/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[2]/div[4]/div["


# ##########################     Second Off      ###################################
    team2 = team2arr[d]
    batsmanCount2 = batsmanCount2arr[d]
    bowlerCount2 =  bowlerCount2arr[d]
    battingUrl2 = "/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[3]/div[1]/div["            
    bowlingUrl2 = "/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[3]/div[4]/div["




    driver.get(Commentary)
    team1ScoreBoard = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[2]/div[4]/div[3]/div[2]/div[2]/div[1]/div[1]/h2[1]')
    team2ScoreBoard = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[2]/div[4]/div[3]/div[2]/div[2]/div[1]/div[1]/h2[2]')
    mom = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[2]/div[4]/div[3]/div[2]/div[2]/div[3]/a[1]')

    score1 = team1ScoreBoard.text
    score2 = team2ScoreBoard.text
    mom = mom.text

    print(score1,score2,mom)


    ###############################     Open ScoreCard       #################

    driver.get(Scorecard)


    ##############################     GET Common Details   ############################################

    matchUrl = "/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[4]/div[2]/div[1]/div[2]"
    dateUrl = "/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[4]/div[2]/div[2]/div[2]/span[1]"
    venueUrl = "/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[4]/div[2]/div[5]/div[2]"
    tossUrl = "/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[4]/div[2]/div[3]/div[2]"
    timeUrl = "/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[4]/div[2]/div[4]/div[2]/span[1]"
    resultUrl = "/html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[1]"


    match = driver.find_element_by_xpath(matchUrl)
    date = driver.find_element_by_xpath(dateUrl)
    venue = driver.find_element_by_xpath(venueUrl)
    toss = driver.find_element_by_xpath(tossUrl)
    time = driver.find_element_by_xpath(timeUrl)
    result = driver.find_element_by_xpath(resultUrl)

    ########################    First off Batting   #################################
    for x in range(batsmanCount):

        y = str(3 + x)
        batsmanUrl = battingUrl + y + "]"
        # print("batsman", batsmanUrl)
        nameUrl = batsmanUrl + "/div[1]"
        outByUrl = batsmanUrl + "/div[2]/span[1]"
        runUrl = batsmanUrl + "/div[3]"
        ballUrl = batsmanUrl + "/div[4]"
        fourUrl = batsmanUrl + "/div[5]"
        sixUrl = batsmanUrl + "/div[6]"
        srUrl = batsmanUrl + "/div[7]"

        # print("url",batsmanUrl)

        player = driver.find_element_by_xpath(nameUrl)
        outBy = driver.find_element_by_xpath(outByUrl)
        run = driver.find_element_by_xpath(runUrl)
        ball = driver.find_element_by_xpath(ballUrl)
        four = driver.find_element_by_xpath(fourUrl)
        six = driver.find_element_by_xpath(sixUrl)
        sr = driver.find_element_by_xpath(srUrl)

        print(player.text,outBy.text,run.text,four.text,six.text)
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

    #################################   First Off Bowling   ##############################
    for x in range(bowlerCount):
        y = str(x + 2)
        bowlerUrl = bowlingUrl + y + "]"

        # print("bowler", bowlerUrl)

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

        print("bowler",name.text)

        data = {
            "name": name.text,
            "over": float(over.text),
            "maiden": int(maiden.text),
            "runs": int(run.text),
            "wickets": int(wicket.text),
            "economy": float(economy.text)
        }
        bowler.append(data)


    ########################    Second off Batting   #################################
    for a in range(batsmanCount2):
        b = str(3 + a)
        batsmanUrl2 = battingUrl2 + b + "]"
        # print("batsman", batsmanUrl2)
        nameUrl2 = batsmanUrl2 + "/div[1]"
        outByUrl2 = batsmanUrl2 + "/div[2]/span[1]"
        runUrl2 = batsmanUrl2 + "/div[3]"
        ballUrl2 = batsmanUrl2 + "/div[4]"
        fourUrl2 = batsmanUrl2 + "/div[5]"
        sixUrl2 = batsmanUrl2 + "/div[6]"
        srUrl2 = batsmanUrl2 + "/div[7]"

        # print("url",batsmanUrl2)

        player2 = driver.find_element_by_xpath(nameUrl2)
        outBy2 = driver.find_element_by_xpath(outByUrl2)
        run2 = driver.find_element_by_xpath(runUrl2)
        ball2 = driver.find_element_by_xpath(ballUrl2)
        four2 = driver.find_element_by_xpath(fourUrl2)
        six2 = driver.find_element_by_xpath(sixUrl2)
        sr2 = driver.find_element_by_xpath(srUrl2)

        print(player2.text,outBy2.text,run2.text,four2.text,six2.text)
        data2 = {
            "name": player2.text,
            "outby": outBy2.text,
            "runs": int(run2.text),
            "balls": int(ball2.text),
            "four": int(four2.text),
            "six": int(six2.text),
            "strickrate": float(sr2.text)
        }
        batsman2.append(data2)

    #################################   Second Off Bowling   ##############################
    for a in range(bowlerCount2):
        b = str(a + 2)
        bowlerUrl2 = bowlingUrl2 + b + "]"

        # print("bowler", bowlerUrl2)

        nameUrl2 = bowlerUrl2 + "/div[1]"
        overUrl2 = bowlerUrl2 + "/div[2]"
        maidenUrl2 = bowlerUrl2 + "/div[3]"
        runUrl2 = bowlerUrl2 + "/div[4]"
        wicketUrl2 = bowlerUrl2 + "/div[5]"
        economyUrl2 = bowlerUrl2 + "/div[8]"

        name2 = driver.find_element_by_xpath(nameUrl2)
        over2 = driver.find_element_by_xpath(overUrl2)
        maiden2 = driver.find_element_by_xpath(maidenUrl2)
        run2 = driver.find_element_by_xpath(runUrl2)
        wicket2 = driver.find_element_by_xpath(wicketUrl2)
        economy2 = driver.find_element_by_xpath(economyUrl2)

        print("bowler",name2.text)

        data2 = {
            "name": name2.text,
            "over": float(over2.text),
            "maiden": int(maiden2.text),
            "runs": int(run2.text),
            "wickets": int(wicket2.text),
            "economy": float(economy2.text)
        }
        bowler2.append(data2)

    



    insertData = {
        "match": match.text,
        "date": date.text,
        "time": time.text,
        "venue": venue.text,
        "toss": toss.text,    
        "result":result.text,
        "score":score1,
        "mom":mom,
        "team": team,
        "batsman": batsman,
        "bowler": bowler
    }

    insertData2 = {
        "match": match.text,
        "date": date.text,
        "time": time.text,
        "venue": venue.text,
        "toss": toss.text,
        "result":result.text,
        "score":score2,
        "mom":mom,
        "team": team2,    
        "batsman": batsman2,
        "bowler": bowler2
    }

    print("InsertData", insertData)
    # insert1 = col.insert_one(insertData)
    # insert2 = col.insert_one(insertData2)

driver.close()


# /html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[3]/div[2]/div[2]/div[1]/a[1]
# /html[1]/body[1]/div[1]/div[2]/div[4]/div[2]/div[3]/div[4]/div[2]/div[1]