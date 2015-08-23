import re
from urllib.request import FancyURLopener
from bs4 import BeautifulSoup


class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

url = input("> ")

myopener = MyOpener()
html = myopener.open(url)

soup = BeautifulSoup(html, "html.parser")

emailREX = re.compile(r'''(
                      mailto:                           # mailto
                      ([a-z0-9!#$%&'*+\/=?^_`{|}~-]+    # username
                      @                                 # @ symbol
                      [a-z0-9]+                         # domain
                      \.[a-zA-Z0-9-.]+)"                # tld
                      )''', re.VERBOSE)

hits = str(soup)
matches = []

# soup.findAll(hits)
for groups in emailREX.findall(hits):
    matches.append(groups[1])

set = set(matches)
result = list(set)
# print(hits)
print(result)
