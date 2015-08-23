import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen(input("> "))

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

# TODO: Make this more efficient
# Move list to set (remive duplicates)
set = set(matches)
# Convert back to list
result = list(set)

# TODO: Send results to clipboard
print(result)
