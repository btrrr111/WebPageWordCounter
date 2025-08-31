import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def search():
    url = None
    word = None
    count = None
    error = None
    if request.method == "POST":
        url = request.form.get("insert_url")
        word = request.form.get("insert_word")
        if url and word:
            word = word.lower()
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
                "Accept-Language": "en-US,en;q=0.9",
            }
            try:
                response = requests.get(url, headers=headers)
                soup = BeautifulSoup(response.text, "html.parser")
                count = soup.get_text().lower().count(word)
            except requests.exceptions.RequestException:
                error = "Please insert a valid URL."
        else:
            error = "Please provide both a valid URL and a word to search for."
    return render_template("index.html", url=url, word=word, count=count, error=error)


if __name__ == ("__main__"):
    app.run(debug=True)
