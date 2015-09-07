from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello():
	return "Hello, world!"


@app.route("/name/<x>")
def name(x):
  return x



@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, this page was not found.", 404


if __name__ == "__main__":
	app.run(host="0.0.0.0")