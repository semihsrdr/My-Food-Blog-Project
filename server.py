from flask import Flask,render_template
import requests,datetime

year=datetime.datetime.now().year

app=Flask(__name__)
respond=requests.get("https://api.npoint.io/485314ccb1a0926f6b95")
food_data=respond.json()


@app.route("/")
def main_page():
    return render_template("index.html",food_data=food_data,year=year)

@app.route("/post/<int:index>")
def go_post(index):
    requested_post=None
    for blog_post in food_data:
        if blog_post["id"]==index:
            requested_post=blog_post
    return render_template("food.html",post=requested_post,year=year)

@app.route("/contact")
def contact_page():
    return render_template("personal.html")

if __name__=="__main__":
    app.run(debug=True)



