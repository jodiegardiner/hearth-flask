from flask import Flask, render_template
import unirest

app = Flask(__name__)





@app.route('/')
def get_html():
    response = unirest.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/sets/Classic?collectible=1", headers={"X-Mashape-Key": "jNTlEK3pimmshwzUrACNgjrooKjUp10tmZOjsnv8ZSu1niWIJn"})
    cards = response.body
    print cards
    return render_template("index.html", cards=cards)


if __name__ == '__main__':
    app.run()
