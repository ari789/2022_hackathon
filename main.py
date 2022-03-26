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
typingPrint("Good " + part + "...\n")
time.sleep(1)

date = date.today().strftime("%B %d, %Y")
holiday = Functions.getHoliday()
typingPrint("Today is " + date + ", also known as " + '\033[1m' + holiday + '\033[0m' + "\n\n")
time.sleep(1)

# Weather Report
typingPrint(Functions.getWeather() + "\n\n")
time.sleep(1)

# Cat Fact
catFact = typingInput("Would you like to hear a cat fact? \033[1m(y/n) \033[0m")

if catFact == "y":
  print(Functions.getCatFact() + "\n")
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
typingPrint("I should really check out the " + random.choice(responses) + " one out...")

# Top songs


# 

time.sleep(1)  
typingPrint("Good bye!\n")
