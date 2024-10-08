from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    title_list = [item["title"] for item in response]
    subtitle_list = [item["subtitle"] for item in response]
    return render_template("index.html", title_lists=title_list, subtitle_lists=subtitle_list)


@app.route('/contact')
def get_contact_page():
    return render_template("contact.html")


@app.route('/about')
def get_aboutme_page():
    return render_template("about.html")


@app.route('/<text>')
def get_post(text):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    title_list = [item["title"] for item in response]
    subtitle_list = [item["subtitle"] for item in response]
    body = [item["body"] for item in response]

    if text == 'life_of_cactus':
        return render_template("post.html", title=title_list[0], subtitle=subtitle_list[0], body=body[0])
    if text == 'top_15_things':
        return render_template("post.html", title=title_list[1], subtitle=subtitle_list[1], body=body[1])
    if text == 'Intermittent_Fasting':
        return render_template("post.html", title=title_list[2], subtitle=subtitle_list[2], body=body[2])


if __name__ == '__main__':
    app.run()
