# scrapping all the information from mlh website to get hackahton information

from bs4 import BeautifulSoup
import requests
import json

# Target the Hackathon website
url = "https://mlh.io/seasons/2023/events"
result = requests.get(url)
# Parse the HTML of the website
doc = BeautifulSoup(result.text, "html.parser")
#print(doc)
hybrid = doc.find_all("span")
# parent = hybrid[0].parent
#print(hybrid)

dataset = open("dataset.log", "w")

Person = []
hack_list = []
#filter out only the in-person events
for element in hybrid:
    if "In-Person" in element.text:
        Hackathons_dict = {}
        Person.append(element)
        # Get enough parent layers to have all information needed
        outer = element.parent.parent.parent

        # make a dictionary entry for each hackathon
        Hackathons_dict["hack_url"] = outer.get('href')
        Hackathons_dict["hack"] = outer.find_all("h3", {"class":"event-name"})[0].text.strip()
        Hackathons_dict["date"] = outer.find_all("p", {"class":"event-date"})[0].text.strip()
        Hackathons_dict["loc"] = outer.find_all("span", itemprop = True)[0].text + ", " + outer.find_all("span", itemprop = True)[1].text
        
        hack_list.append(Hackathons_dict)
        #dump as json format

dataset.write(json.dumps(hack_list,indent=2))