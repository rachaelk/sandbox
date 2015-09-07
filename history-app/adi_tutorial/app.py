from flask import Flask, render_template, request #, jsonify
import requests

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello():
	return render_template('hello.html')


@app.route("/name/<x>")
def name(x):
  return x

#######################################################################
#### Second portion of web app dev tutorial:
# Note: request.form is a mulidict.
@app.route("/search", methods=["GET", "POST"])
def search():
	if request.method == "POST":
		url = "https://api.github.com/search/repositories?q=" + request.form["user_search"]
		response_dict = requests.get(url).json()
		return render_template("results.html", api_data=response_dict)
	else: # request.method == "GET"
		return render_template("search.html")



#######################################################################
#### First portion of web app dev tutorial:
# @app.route("/search/<search_query>")
# def search(search_query):
#   url = "https://api.github.com/search/repositories?q=" + search_query
#   response_dict = parse_response(requests.get(url).json())
#   return jsonify(response_dict)
# def parse_response(response_dict):
# 	r = response_dict['items'][0];
# 	response = {
# 		"total_count" : response_dict['total_count'],
# 		"name" : r['name'],
# 		"owner" : {
# 			"login": r['owner']['login'],
# 			"avatar_url": r['owner']['avatar_url'],
# 			"html_url": r['owner']['html_url']
# 			},
# 		"html_url": r['html_url'],
# 		"description":r['description']
# 		}
# 	return response;
#######################################################################






@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, this page was not found.", 404


if __name__ == "__main__":
	app.run(host="0.0.0.0")