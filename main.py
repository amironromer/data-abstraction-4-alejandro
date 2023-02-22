# make sure you fork this and git repo it
# go to the shell command screen and type
# pip install -r requirements.txt
#to install the necessary components
import requests
from bs4 import BeautifulSoup
import csv
# get the html
url = "https://www.amazon.com/Best-Sellers-Books/zgbs/books"
headers = {
  'user-agent':
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
#get all books
books = soup.find_all(id="gridItemRoot")
# print(books[15])
# book = books[15]

# csv_headers = ['rank', 'title', 'author', 'price']
# with open('amazon_books.csv', 'a', encoding='utf-8', newline='') as f:
#   writer = csv.writer(f)
#   writer.writerow(['rank', 'title', 'author', 'price'])
  


for book in books:
  rank = book.find('span', class_="zg-bdg-text").text[1:]
  print(rank)
  children = book.find('div', class_='zg-grid-general-faceout').div
  children.contents[0]
  title = children.contents[1].text
  author = children.contents[2].text
  price = children.contents[-1].text
  print(title)
  print(author)
  print(price)


csv_headers = ['rank', 'title', 'author', 'price']
with open('amazon_books.csv', 'a', encoding='utf-8', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(['rank', 'title', 'author', 'price'])