#Covers.com Odds Listing Scraper.  

covers_nfl_live_odds_url = 'http://www.covers.com/odds/football/nfl-spreads.aspx'

#Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

#Get a browser window
browser = webdriver.Firefox()
browser.get(covers_nfl_live_odds_url)
assert 'NFL Football Odds' in browser.title



#This is a hackey way to allow the links above to finish loading before shit is pulled.  There is praobably a better way.
sleep(5)

#Fetch Games List And Current Spread
home_teams = browser.find_elements_by_xpath("//div[@class='team_home']//strong")
home_team_text = []
for i in home_teams:
	home_team_text.append(i.text)

away_teams = browser.find_elements_by_xpath("//div[@class='team_away']//strong")
away_team_text = []
for i in away_teams:
	away_team_text.append(i.text)


spread = browser.find_elements_by_xpath("//div[@class='covers_bottom']")
spread_float = []
for i in spread:
	spread_float.append(float(i.text))


games = zip(away_team_text, home_team_text, spread_float)
#You now have your games.

favorites = []
for i in games:
	li = list(i)
	odds = i[2]
#	print odds
	if odds > 0: 
		li.append('visitor')
	elif odds < 0:
		li.append('home')
	else:
		li.append('none')
	favorites.append(li)

for i in favorites:
	print i


#Quit your browser once you get all your data pulled. 
browser.quit()





