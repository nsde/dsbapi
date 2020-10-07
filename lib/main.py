import requests as rq
from bs4 import BeautifulSoup

url = "https://app.dsbcontrol.de/data/9c9bcbc1-132d-442c-bf82-52494b33d947/d08b92ff-6c3e-43e8-8457-6d24f4cb305a/subst_001.htm"
r = rq.get(url)
bs = BeautifulSoup(r.text, "lxml")
found = bs.findAll("span")[3:]
for item in found:
    try:
        print(str(item).replace('<span style="color: #010101">', "").replace("</span>", ""))
    except:
        print("ERROR")