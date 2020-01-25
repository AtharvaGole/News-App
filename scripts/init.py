#Run this code only at first time load of the application
import json 

with open("data/article_data.json", "w") as file:
	json.dump({},file)

with open("data/user_data.json", "w") as file:
	json.dump({},file)