from scripts.json_handler import *
from time import time


def generate_article_id(data):

	article_id = ""

	if data["source"]["id"] != None:
		article_id += data["source"]["id"]+"_"

	if data["source"]["name"] != None:
		article_id += data["source"]["name"]+"_"

	if data["author"] != None:
		article_id += data["author"]+"_"

	if data["publishedAt"] != None:
		article_id += data["publishedAt"]+"_"	

	return article_id


def add_article(article_id, data):

	article_data = load(article)

	if article_id in article_data.keys():
		return False

	#This is still left
	article_data[article_id] = {"data":data, "keywords":set(data[description.split()]), "likes":0, "dislikes":0, "comments":[]}

	dump(article_data)

	return True


def add_articles(data):

	for i in data:

		add_article(generate_article_id(i), i)

"""
def get_name(article_id):
	
	return load(article)["article_id"]
"""


"""
Database Structure
{user_id: {password:_, likes:set(), dislikes:set()}, current_headlines:[]}

{article_id: {data:{}, keywords:set(), likes:_, dislikes:_, comments:[[user_id, time, comment],]}}
"""


def add_like(article_id, user_id):
	
	user_data = load(user)
	article_data = load(article)

	if article_id in user_data[user_id]["dislikes"]:
		user_data[user_id]["dislikes"].remove(article_id)
		article_data[article_id]["dislikes"] -= 1

	user_data[user_id]["likes"].add(article_id)
	article_data[article_id]["likes"] += 1

	dump(user_data)
	dump(article_data)



def add_dislike(article_id, user_id):
	
	user_data = load(user)
	article_data = load(article)

	if article_id in user_data[user_id]["likes"]:
		user_data[user_id]["likes"].remove(article_id)
		article_data[article_id]["likes"] -= 1

	user_data[user_id]["dislikes"].add(article_id)
	article_data[article_id]["dislikes"] += 1

	dump(user_data)
	dump(article_data)
	

def add_comment(article_id, user_id, comment):
	
	article_data = load(article)
	article_data[article_id]["comments"].append([user_id, time(), comment])
	dump(article_data)


def get_article_data_for_user(article_id, user_id):

	user_data = load(user)
	article_data = load(article)


	







	

