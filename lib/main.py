import requests as rq
from bs4 import BeautifulSoup

url = "https://app.dsbcontrol.de/data/9c9bcbc1-132d-442c-bf82-52494b33d947/d08b92ff-6c3e-43e8-8457-6d24f4cb305a/subst_001.htm"
r = rq.get(url)
bs = BeautifulSoup(r.text, "lxml")
found = bs.findAll("td")

currentItem = ""
finalList = []
currentList = []

for item in found:
    aboutToPrint = str(item).split(">") # I sink here is si problem
    aboutToPrint = aboutToPrint[1].replace("</span>", "").replace("</td","").replace('<span style="color: #010101"',"").replace("<b","").replace("\xa0","")
    if aboutToPrint == " " or aboutToPrint == "---" or aboutToPrint == "" or aboutToPrint == "-----":
        pass
    
    # elif aboutToPrint.startswith("0"):
        # pass

    else:
        if aboutToPrint.startswith("0") or aboutToPrint.startswith("Q") or aboutToPrint == ("EF"):
            aboutToPrint = aboutToPrint.replace("0","")
            finalList.append(currentList)
            currentList = []
    
        currentItem += aboutToPrint
        currentList.append(aboutToPrint)

# print(finalList)

for item in finalList:
    print(item)