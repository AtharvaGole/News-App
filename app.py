from flask import Flask, render_template
import requests
import json


app = Flask(__name__)


@app.route("/")
def index():
   return render_template("index.html")


@app.route("/top_headlines")
def top_headlines():
	url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=4ef5a79a65d84f11a06907c1356fb056')
	response = requests.get(url)
	data = json.dumps(response.json())

	return data



if __name__ == "__main__":
   app.run(debug = True)
   
   
   
