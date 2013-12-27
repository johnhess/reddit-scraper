"""
Scrape the front page of reddit.com
"""
from bs4 import BeautifulSoup
import requests

reddit = requests.get('http://www.reddit.com')
reddit_soup = BeautifulSoup(reddit.text)

title_links = reddit_soup.find_all('a', class_="title")

# strip out some hidden results
actual_links = [l for l in title_links if l.parent.parent.parent.parent.get('id', None) == "siteTable"]

print "There are {0} links on this page:".format(len(title_links))
for tl in actual_links:
	# print information about each link
	print u"   {0}: {1}".format(tl.parent.parent.parent.span.text, tl.text)

	# if it's an image, download it
	href = tl.get('href') 
	if ".jpg" in href:
		filename = "imgs/" + href.split("/")[-1]
		img = requests.get(href)

		with open(filename, 'wb') as f:
			for chunk in img.iter_content():
				f.write(chunk)
