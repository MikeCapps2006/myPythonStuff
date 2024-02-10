import requests
import lxml
import bs4

two_star_ratings = []
for n in range(1, 51):
    scrape_url = 'https://books.toscrape.com/catalogue/page-{}.html'.format('n')
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    books = soup.select('.product_pod')

    for book in books:
        if (len(book.select('.star-rating.Two')) != 0):
            two_star_ratings.append(book.select('a')[1]['title'])

for book in two_star_ratings:
    print(book)


