from scripts.json_handler import *


def add_user(user_id, password):

	user_data = load(user)

	if user_id in user_data.keys():
		return False

	user_data[user_id] = {"password":password, "likes":set(), "dislikes":set(), "current_headlines": []}

	dump(user_data)

	return True




