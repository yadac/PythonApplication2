import re

with open("python-site.html", encoding = "utf-8") as f:
	html = f.read()

# retrieve href attribute
# <a href="xxx"></a>
for row in re.findall(r"<a.*?</a>", html, re.DOTALL):
	url = re.search(r"<a href=\"(.*?)\">", row).group(1)
	print(url)

