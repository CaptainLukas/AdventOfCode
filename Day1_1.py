#Day 1.1
from bs4 import BeautifulSoup as bs

url = 'https://adventofcode.com/2021/day/1/input'

f = urllib.request.urlopen(url)
soup = bs(f.read())
print(soup)