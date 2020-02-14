from flask import Flask, render_template, url_for, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from scripts.news import *
import json


app = Flask(__name__)
CORS(app)


country_codes = ['ae', 'ar', 'at', 'au', 'be', 'bg', 'br', 'ca', 'ch', 'cn', 'co', 'cu', 'cz', 'de', 'eg', 'fr', 'gb', 'gr', 'hk', 'hu', 'id', 'ie', 'il', 'in', 'it', 'jp', 'kr', 'lt', 'lv', 'ma', 'mx', 'my', 'ng', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ro', 'rs', 'ru', 'sa', 'se', 'sg', 'si', 'sk', 'th', 'tr', 'tw', 'ua', 'us', 've', 'za']

@app.route("/")
def index():
	return render_template("login.html")

@app.route("/rss")
def rss():
	return render_template("rss.html")

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/article")
def article():

	title = "Rahul, Iyer show their worth as India make light work of 204 target "
	source = "Cricbuzz"
	author = "Cricbuzz Staff"
	description = "Not the city, the $57 million-funded cryptocurrency custodian startup. When someone wants to keep tens or hundreds of millions of dollars in Bitcoin, Ethereum, or other coins safe, they put them in Anchorage’s vault. And now they can trade straight from custo…"
	urlToImage = "https://techcrunch.com/wp-content/uploads/2020/01/Anchorage-Trading-1.png?w=740"
	publishedAt = "2020-01-15T11:57:30Z"


	return render_template("main.html", title = title, source = source, author = author, description = description, urlToImage = urlToImage, publishedAt = publishedAt)


@app.route("/explore")
def explore():

	category = request.args.get("category")
	country = request.args.get("country")

	if category == None:
		category = ""

	if country == None:
		country = "us"

	data = get_top_headlines(category = category, country = country)[:8]

	print(data[:3])

	return render_template("explore.html", slide = data[:3], data = data[3:], category = category, country = country, country_codes = country_codes)


@app.route("/load_more")
def load_more():

	curr = int(request.args.get("total_posts"))
	data = get_top_headlines(category = request.args.get("category"), country = request.args.get("country"))
	t = 5

	return jsonify(data = data[curr:min(curr+t, len(data))])


@app.route("/load_category")
def load_category():

	category = request.args.get("category")
	country = request.args.get("country")

	if category == None:
		category = ""

	if country == None:
		country = "us"

	data = get_top_headlines(category = category, country = country)[:8]

	print(data[:3])

	return jsonify(slide = data[:3], data = data[3:])


@app.route("/search_articles")
def search_articles():

	q = request.args.get("q")
	
	curr = int(request.args.get("total_posts"))
	data = get_everything("2020-01-01", "2020-01-25", q = q)
	t = 5

	return jsonify(data = data[curr:min(curr+t, len(data))])


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


   
   
