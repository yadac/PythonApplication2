import re
from urllib.request import urlopen

f = urlopen("https://www.python.jp/about/")

# f = httpResponse type
print(type(f))

# define encoding default as utf-8
enc_type = f.info().get_content_charset(failobj = "utf-8")

# meta tag exists in 1024 bytes
#   <meta charset="utf-8" />
str = f.read()
d_str = str[:1024].decode("ascii", errors = "replace")
match = re.search(r"charset=[\"]?([\w-]+)", d_str)
if match:
	print(match)
	enc_type = match.group(1)
else:
	print("un-match!!")

print(enc_type)
print(f.getheader("Content-Type"))

# http status 2xx = ok, 4xx = error, 5xx = server error
# print(f.status)

# decode by utf-8
data = f.read().decode(enc_type)
print(data)

wf = open("python-site.txt", "w", encoding = "utf-8")
wf.write(data)
wf.close()



