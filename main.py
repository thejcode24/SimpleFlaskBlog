
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# SECRET_KEY generated using built-in Python library, secrets
# import secrets
# secrets.token_hex(16) creates a random 16 digit value
app.config["SECRET_KEY"] = "2d971c13806bda77a4c3060fd5e89866"

# sqlite:///site.db is the relative filepath
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

# Create SQLAlchemy database instance
db = SQLAlchemy(app)

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

@app.route("/register", methods=["GET", "POST"])
def register():
    # Create instance of Registration form.
    form = RegistrationForm()

    # Check form for valid info in registration form
    if form.validate_on_submit():
        # Use flash() to show a quick message on-screen
        flash(f"Account Succesfully Created for {form.username.data}!", "success")
        # After successful creation of login, show home page
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    # Create instance of Login form.
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == "admin@home.gg" and form.password.data == "123":
            flash(f"You are now logged in as {form.email.data}", "success")
            return redirect(url_for("home"))
    return render_template("login.html", title="Login", form=form)


if __name__ == '__main__': 
    app.run(debug=True)