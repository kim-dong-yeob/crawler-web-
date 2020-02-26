import urllib.request as req
import simplejson as json
import time
import os

while True:
    url = "https://www.naver.com/srchrank?frm=main&ag=all&gr=1&ma=-2&si=0&en=0&sp=0"

    savePath = "./naver.json"
    textPath = "./naver.txt"
    
    req.urlretrieve(url, savePath)

    keyword = json.load(open(savePath, 'r', encoding="utf-8"))

    f = open(textPath, 'a')
    f.write(str(keyword['ts']) + '\n')
    for k in keyword['data']:
        print(k['rank'], k['keyword'])
        w = str(k['rank']) + ' ' + str(k['keyword']) + '\n'
        f.write(w)
    f.write('\n\n')
    f.close()
    
    time.sleep(60)
