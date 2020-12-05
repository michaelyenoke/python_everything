#  https://www.youtube.com/channel/UCFdTiwvDjyc62DBWrlYDtlQ/search?query=ptt

# Step One - requests - get

import requests

res = requests.get('https://www.ptt.cc/bbs/Food/index.html')
#以前會需要 verify = false

print(res.text)


# Step Two - beautiful soup
import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.ptt.cc/bbs/Food/index.html')
soup = BeautifulSoup(res.text)
for entry in soup.select('.r-ent'):
    #print(entry)
    #print(entry.select('.title'))
    #print(entry.select('.date'))
    #print(entry.select('.date')[0].text)
    print(entry.select('.date')[0].text, entry.select('.author')[0].text,entry.select('.title')[0].text)
