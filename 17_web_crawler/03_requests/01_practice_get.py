#21-2-1
#requests.get()
#py -m pip install requests

import requests

url='http://decathlon.tw'
htmlfile = requests.get(url)
print(type(htmlfile))
