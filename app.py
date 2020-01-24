from flask import Flask, render_template
import requests
#from scripts.news import *
import json


app = Flask(__name__)


@app.route("/")
def index():
   return render_template("home.html")


@app.route("/article")
def article():

   title = "Rahul, Iyer show their worth as India make light work of 204 target "
   source = "Cricbuzz"
   author = "Cricbuzz Staff"
   description = "Not the city, the $57 million-funded cryptocurrency custodian startup. When someone wants to keep tens or hundreds of millions of dollars in Bitcoin, Ethereum, or other coins safe, they put them in Anchorage’s vault. And now they can trade straight from custo…"
   urlToImage = "https://techcrunch.com/wp-content/uploads/2020/01/Anchorage-Trading-1.png?w=740"
   publishedAt = "2020-01-15T11:57:30Z"


   return render_template("main.html", title = title, source = source, author = author, description = description, urlToImage = urlToImage, publishedAt = publishedAt)


@app.route("/top_headlines")
def top_headlines():
	"""
	url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=4ef5a79a65d84f11a06907c1356fb056')
	response = requests.get(url)
	"""
	
	"""
	newsapi = NewsApiClient(api_key='4ef5a79a65d84f11a06907c1356fb056')

	top_headlines = newsapi.get_top_headlines(
		category = 'sports',
     	language = 'en',
     	country = 'in')

	data = json.dumps(top_headlines)
	
	return data
	"""

	return get_top_headlines(q = "Rohit Sharma", category = "sports", country = "in")


if __name__ == "__main__":
   app.run(debug = True)


   
   
