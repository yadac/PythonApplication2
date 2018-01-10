import json

data = {
	"title" : "json-sample",
	"date" : "2017.11.22",
	"items" : [{
			"title" : "title-1",
			"contents" : "contents-1"
		},
		{
			"title" : "title-2",
			"contents" : "contents-2"
		}]
}

# output to file
save_path = "sample.json"
with open(save_path, "w") as outfile:
	json.dump(data, outfile, ensure_ascii = False)

# convert to string
#str = json.dumps(data)
#print(str)
# if string includes 2-byte character, you need to ensure_ascii.
str = json.dumps(data, ensure_ascii = False)
print(str)

# read json-file
try:
	# this object is disposed automatically???
	with open("sample.json", "r") as f:
		data = json.load(f)
		print(data)
		print(data["title"])
		print(data["date"])
		print(data["items"])
except json.JSONDecodeError as e:
	print("JSONDecodeError:", e)