from newsapi import NewsApiClient
import json


api_key = "4ef5a79a65d84f11a06907c1356fb056"


def get_top_headlines(q = "", category = "", language = "en", country = "us"):

	newsapi = NewsApiClient(api_key = api_key)
	
	#try:
	if category == "":
		top_headlines = newsapi.get_top_headlines(q = q, language = language, country = country)
	else:
		top_headlines = newsapi.get_top_headlines(q = q, category = category, language = language, country = country)

	#top_headlines = json.dumps(top_headlines)
	
	return top_headlines["articles"]

	#except:
	#	return -1



def get_everything(from_param, to, q = "", category = "", language = "en", sort_by = "relevancy"):

	newsapi = NewsApiClient(api_key = api_key)
	
	#try:
	if category == "":
		everything = newsapi.get_everything(q = q, language = language, from_param = from_param, to = to, sort_by = sort_by)
	else:
		everything = newsapi.get_everything(q = q, category = category, language = language, from_param = from_param, to = to, sort_by = sort_by)

	#everything = json.dumps(everything)
	
	return everything["articles"]

	#except:
	#	return -1







