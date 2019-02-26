
from flask import Flask, render_template
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# SECRET_KEY generated using built-in Python library, secrets
# import secrets
# secrets.token_hex(16) creates a random 16 digit value
app.config["SECRET_KEY"] = "2d971c13806bda77a4c3060fd5e89866"

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

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", )

@app.route("/register")
def register():
    # Create instance of Registration form.
    form = RegistrationForm()
    return render_template("register.html", title="Register", form=form)

@app.route("/login")
def login():
    # Create instance of Login form.
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == '__main__': 
    app.run(debug=True)