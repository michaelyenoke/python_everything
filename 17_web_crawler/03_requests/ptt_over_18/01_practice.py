# [爬蟲實戰] 如何告訴PTT我已滿18並順利抓取八卦版的文章 ? : https://www.youtube.com/watch?v=G5MDpnGsE-k

# Step One : 進入前有18禁限制

import requests
res = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html') # varify - 驗證
print(res.text)


# Step Two : 解決 18 禁問題:在 get 前要先處理 post
# 進入 F12 > Network > 按下over18?...頁面 > Headers > 按下 Yes -  ptt.cc/ask/over18 > From Data: from: bbs/Gossiping/index.html;yes:yes

import requests

payload = {
    'from':'/bbs/Gossiping/index.html',
    'yes':'yse'
}
rs = requests.session()
res = rs.post('https://ptt.cc/ask/over18', data = payload)
res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html') 
print(res.text)
