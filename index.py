import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse

image = []; name = []; face = []; personality = []; where = []
count = 0
for i in range(0, 5):
    url = ("http://faculty.ndhu.edu.tw/~aowoo-welfare/area" + str(i) + ".html")
    domain = "{}://{}".format(urlparse(url).scheme, urlparse(url).hostname)
    html = requests.get(url)
    html.encoding = "utf-8"
    sp = BeautifulSoup(html.text, 'lxml')
    photo = sp.find_all('img')
        
    for data in photo:
        src = data.get('src')
        targets = [src]
        for t in targets:
            if t != None and ('.jpg' in t or '.png' in t):
                if t.startswith('http'):
                    image.append(t)
                else:
                    image.append(domain + t)
                    
    for items in (sp.find_all('img')):
        if not os.path.exists('doggo'):
            os.mkdir('doggo')
        catch = requests.get(('http://faculty.ndhu.edu.tw/~aowoo-welfare/' + items.get('src')))
        with open('doggo/' + image[count].replace('http://faculty.ndhu.edu.twimage/dogs/', '').replace('.jpg', '') + ".jpg", "wb") as file:
            file.write(catch.content)
            file.flush()
        file.close()
        count = count + 1
print('The photo of the doggo are all in the file now!')