# News-App
A web app to view latest news with features like google translate and text to speech.

#changes in app.py
@app.route("/")
def index():
	return render_template("home.html")
  
  if we keep .html it will not redirect to home-page and it will give jinga2 temp error
  
  #newsapiclient is giving error


