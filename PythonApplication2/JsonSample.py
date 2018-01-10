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
str = json.dumps(data, ensure_ascii = False)
print(str)