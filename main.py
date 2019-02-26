
from flask import Flask, render_template

app = Flask(__name__)

# "dummy" data representing a blog post
posts = [
    {
        'author': 'James Jung',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'February 25, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 26, 2019'
    }
]

@app.route('/')
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html", )

if __name__ == '__main__': 
    app.run(debug=True)