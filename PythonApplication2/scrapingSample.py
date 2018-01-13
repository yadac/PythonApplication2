import re

with open("python-site.html", encoding="utf-8") as f:
	html = f.read()

# retrieve href attribute
# <a href="xxx"></a>
try:
	for row in re.findall(r"<a.*?</a>", html, re.DOTALL):
		# change expression from text
		url = re.search(r"href=[\"'](.*?)[\"']", row).group(1)
		print(url)
except AttributeError as e:
	print("EXCEPTION RAISE!!!")
	print(row)

print("-------------------- beautifulsoup4")

from bs4 import BeautifulSoup

# default encoding of open methods is not "utf-8"? 
# -> depend on platform (in my casse, default is "shift-jis", so i need to "utf-8" explicitly).
with open("python-site.html", encoding="utf-8") as f:
	html = f.read()
soup = BeautifulSoup(html, "html.parser")
tags = soup.find_all("a")
for tag in tags:
	print(tag.get("href"))
