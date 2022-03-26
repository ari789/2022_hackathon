import requests
import random, time
import pandas as pd                        
from pytrends.request import TrendReq
import billboard

# takes current hour as input
# returns appropriate part of day for greeting
def getPartOfDay(h):
    return (
        "Morning"
        if 5 <= h <= 11
        else "Afternoon"
        if 12 <= h <= 17
        else "Evening"
        if 18 <= h <= 22
        else "Night"
    )

# returns one of today's wacky holidays (from API linked)
def getHoliday():
    try:
        res = requests.get('https://national-api-day.herokuapp.com/api/today')
        if res.status_code == 200:
            day = (res.json()['holidays'][random.randrange(0,10,1)])
        else :
            day = "Error retrieving wacky holiday."
        return day
    except:
        return("Something went wrong! Try Again!")

# returns a random quote (from API linked)
def getQuote():
	try:
		res = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
		if res.status_code == 200:
			json_data = res.json()
			data = json_data['data']

			return(data[0]['quoteText'])
		else:
			return("Error retrieving quote")
	except:
		return("Something went wrong! Try Again!")

# returns weather data as a readable string (from API linked)
def getWeather():
    try:
        res = requests.get('http://api.weatherapi.com/v1/current.json?key=2083c355a3ec413ca48202829222603&q=auto:ip&aqi=no')
        if res.status_code == 200:
            data = parseWeather(res)
        else :
            data = "Error retrieving weather data."
        return data
    except:
        return("Something went wrong! Try Again!")

# takes in raw weather data 
# parses and returns as readable string
def parseWeather(res):
    name = res.json()['location']['name']    
    data = "Your weather report for " + name + " is ready!\n"
    time.sleep(1)

    skies = res.json()['current']['condition']['text']    
    data += "The forecast is " + skies + " today, "
    
    wind = res.json()['current']['wind_mph']
    if(wind >= 5.0 and wind < 15.0):
        data += "with a gentle breeze. "
    elif(wind >= 15.0 and wind < 25.0):
        data += "with some wind. "
    elif(wind >= 25.0):
        data += "with strong winds. "
    else:
        data += "with very little wind. "
    
    time.sleep(1)

    temp = int(res.json()['current']['temp_f'])
    data += "The temperature right now is " + str(temp) + u'\N{DEGREE SIGN}' + "F"

    return data


# returns a random cat fact (from API linked)
def getCatFact():
    try:
        res = requests.get('https://cat-fact.herokuapp.com/facts/random')    
        if res.status_code == 200:
            fact = (res.json()['text'])
        else :
            fact = "Error retrieving cat fact."
        return fact
    except:
        return("Something went wrong! Try Again!")

# uses Google trends API for python (pytrends)
# returns top 3 Google searches of the day
def getSearchTrends():
    pytrend = TrendReq()
    df = pytrend.trending_searches(pn='united_states')
    df.head()
    return df

def getTopSongs():
    return billboard.ChartData('hot-100')

