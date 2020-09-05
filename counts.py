# import
import requests
from bs4 import BeautifulSoup
import time


# home url
url = "https://www.worldometers.info/coronavirus/"


# input from user
country_id = input("Enter the valid country name or press enter to view global counts\t").lower()

print("\n")
original = country_id
if len(country_id.split()) > 1:
    id = ("-").join(country_id.split())

place = ""
world = True

if country_id:
    place = "/country/" + country_id + "/"
    world = False
url = url + place
time.sleep(1)
r = requests.get(url)
doc = BeautifulSoup(r.text, "html.parser")
mylist = ["Cases", "Death", "Recovered"]
index = 0
if world:
    print("WORLD\n")
else:
    print(original.upper() + "\n")
for counts in doc.select(".maincounter-number"):
    print(mylist[index] + ":\t" + counts.text)

    index += 1

