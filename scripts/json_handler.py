import json


user = "data/user_data.json"
article = "data/article_data.json"


def load(filename):
	
	data = {}
	with open(filename, "r") as file:
		data = json.load(file)
	return data


def dump(filename, data):
	
	with open(filename, "w") as file:
		json.dump(data, filename)
	


	

