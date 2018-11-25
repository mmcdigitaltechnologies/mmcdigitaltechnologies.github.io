from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
    dadurl = "https://icanhazdadjoke.com/"

    response = requests.get(dadurl, headers={"Accept":"application/json"})
    #print("code = {}".format(response.status_code))

    jokeResponse = response.json()

    return render_template("index.html",joke=jokeResponse['joke'])

if __name__ == "__main__":
    app.run(debug=True)