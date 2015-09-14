# This is a quick and dirty script to scrape domainlore.uk for all the currently active listings
# There may be some out of range errors as it needs fine tuning.
# Can be extended with the email script and using launchd or a cron job to automagically send the results daily.

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen("http://domainlore.uk")
soup = BeautifulSoup(url, "html")

mylist = []
domain = soup.findAll('table', id="spotlight")
# print(len(domain))
listings = [[td.getText() for td in domain[i].findAll('td')] for i in range(len(domain))]

listings = list(listings[0])
# print(len(listings))

num = 0
for i in listings:
    print(listings[num])
    if num <= len(listings) - 6:
        num += 5
    if num >= len(listings) - 5:
        print(listings[num])
        break
