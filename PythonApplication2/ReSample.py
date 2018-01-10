# regular expression
import re

# compiled (fast)
pattern = r"ho"
co = re.compile(pattern)
match_obj = co.match("hoge")

# result is ...  ?
print(match_obj)

# adhoc
pattern = r"ho"
res = re.match(pattern,"hoge")

# result is ...  ?
print(res)

print("-------------------------------- match")
# match
pattern = r"ho"
text = "hogehogeHo"
res = re.match(pattern,text)
print(res)
print(res.group())

print("-------------------------------- search")
# search
res = re.search(pattern, text)
print(res.span(), res.group()) # span(0, 2) is first match. -> *ho*gehogeHo

print("-------------------------------- findall")
# findall
res = re.findall(pattern, text)
if res:
	print(res)

print("-------------------------------- finditer")
# finditer
res = re.finditer(pattern, text)
for match in res:
	print(match)
	print(match.group())
	print(match.span())

print("-------------------------------- split")
# split
res = re.split(",", "ho,ge,fu,ga")
if res:
	print(res)

print("-------------------------------- sub")
# sub
res = re.sub(pattern, "zz", text)
if res:
	print(res)

print("-------------------------------- option")
# using option
# ex. ignorecase
res = re.findall(pattern, text, re.IGNORECASE)
print(res)
