#Python Typing Text Effect - www.101computing.net/python-typing-text-effect/
import time,os,sys, random
from datetime import datetime, date
import Functions


def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value  


# Greeting
part = Functions.getPartOfDay(datetime.now().hour)    
typingPrint("Good " + part + "!\n")
time.sleep(1)

date = date.today().strftime("%B %d, %Y")
holiday = Functions.getHoliday()
typingPrint("Today is " + date + ", also known as " + holiday + "\n\n")
time.sleep(1)

# Daily quote
typingPrint("A quote for you:\n")
typingPrint('"' + Functions.getQuote() + '"\n\n')
time.sleep(1)
typingPrint("Was that inspirational?\n")
typingPrint("Maybe not.\n\n")
time.sleep(1)

# Weather Report
typingPrint(Functions.getWeather() + "\n\n")
time.sleep(1)

# Cat Fact
catFact = typingInput("Would you like to hear a cat fact? (y/n) ")

if catFact == "y":
  typingPrint(Functions.getCatFact() + "\n\n")
elif catFact == "n":
  responses = ["Oh well.", "Fine.", "I forgot you hate cats.", ">:(", "Maybe tomorrow.", "Wrong answer.", "Lame."]
  typingPrint(random.choice(responses) + "\n\n")
else:
  typingPrint("Invalid answer!")  
time.sleep(1)

# Top google searches
df = Functions.getSearchTrends()
typingPrint("These are the most searched terms on Google today: \n")
typingPrint("1. " + df[0][0] + "\n")
typingPrint("2. " + df[0][1] + "\n")
typingPrint("3. " + df[0][2] + "\n")
typingPrint("4. " + df[0][3] + "\n")
typingPrint("5. " + df[0][4] + "\n\n")
time.sleep(1)
responses = ["1st", "2nd", "3rd", "4th", "5th"]
typingPrint("I should really check out the " + random.choice(responses) + " one...\n\n")
time.sleep(1)


# Top songs
chart = Functions.getTopSongs()
typingPrint("These are the top trending songs right now:\n")
typingPrint("1. " + chart[0].title + " by " + chart[0].artist + "\n")
typingPrint("2. " + chart[1].title + " by " + chart[1].artist + "\n")
typingPrint("3. " + chart[2].title + " by " + chart[2].artist + "\n")
typingPrint("4. " + chart[3].title + " by " + chart[3].artist + "\n")
typingPrint("5. " + chart[4].title + " by " + chart[4].artist + "\n")
time.sleep(1)
typingPrint("Listen to them here: https://www.billboard.com/charts/hot-100/ \n\n")
time.sleep(2)

typingPrint("*Yawn*\n")
time.sleep(1)  
typingPrint("I think that's enough for today. \n")
typingPrint("Until next time...")
time.sleep(1)
typingPrint("<3")
