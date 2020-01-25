from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='4ef5a79a65d84f11a06907c1356fb056')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='Cricket', country="in")

print(top_headlines)