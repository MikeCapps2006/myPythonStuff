from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json
import csv

page_url = 'https://alansimpson.me/python/scrape_sample.html'
req = Request(page_url)
req.add_header('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')
rawpage = urlopen(req)
status = rawpage.code

print(type(rawpage))
print(status)

soup = BeautifulSoup(rawpage, 'html5lib')

content = soup.article

links_list = []

for link in content.find_all('a'):
    #Try to get the href, image url, and text
    try:
        url = link.get('href')
        img = link.img.get('src')
        text = link.span.text
        links_list.append({'url': url,
                       'img': img,
                       'text': text})
    #If the row is missing anything.....
    except AttributeError:
        #skip it, and don't crash
        pass

#Save it to a JSON file
with open('links.json', 'w', encoding='utf-8') as links_file:
    json.dump(links_list, links_file, ensure_ascii=False)


#Save it to a CSV file
with open('links.csv', 'w', newline='') as csv_out:
    csv_writer = csv.writer(csv_out)
    #Create the header row
    csv_writer.writerow(['url', 'img', 'text'])

    for row in links_list:
        csv_writer.writerow([str(row['url']), str(row['img']), str(row['text'])])
