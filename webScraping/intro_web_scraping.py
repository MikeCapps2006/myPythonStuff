import requests
import bs4

""" res = requests.get('http://www.example.com')
soup = bs4.BeautifulSoup(res.text, 'lxml')

title_tag = soup.select('title')[0]
print(title_tag.get_text()) """

""" res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text, 'lxml')
headlines = soup.select('.mw-headline')

for headline in headlines:
    print(headline.get_text())
 """


res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text, 'lxml')

image_info = soup.select('.mw-file-element')

computer = image_info[1]

image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')

f = open('new_image.jpg', 'wb')
f.write(image_link.content)
f.close()