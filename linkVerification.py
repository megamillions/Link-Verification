#! python3
# linkVerification.py - Check that all links on a page are valid,
# and print out any problematic links with error message.

import bs4, requests

# Edit out URL as desired.
url = 'https://tinternet.xyz/'	

# Downloads the URL.
res = requests.get(url)
res.raise_for_status()

# Converts into BeautifulSoup for ease of searching.
soup = bs4.BeautifulSoup(res.text, features='html.parser')

# Add a counter for user feedback.
counter = 0

# Loop through all links found on the page.
for link in soup.select('a[href]'):

	# Create URL to check from web domain.
	l = link.get('href')

	# Check for any errors at URL.
	try:
		requests.get(l).raise_for_status()

	# Print any problematic links.
	except Exception as exc:
		print('There was a problem at %s ~ %s.' % (l, exc))

	counter += 1

# Give feedback once script has been run.
print('All done. We looked at %s links in total.' % str(counter))