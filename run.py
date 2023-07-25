# import the Flask class
from flask import Flask, render_template
import os

# create an instance of it and store it in a variable called 'app'
app = Flask(__name__)  # flask needs this to know where to look for
# templates & static files


# decorator to match URLs to view functions
@app.route("/")  # "/" indicates to browse the root directory
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":  # "__main__" d name of d default module in Python

    # run the app with the following arguments
    app.run(
        # use the os module get the 'IP' env var if it exists &
        # set a default val in case it doesn't
        host=os.environ.get("IP", "0.0.0.0"),
        # use the os module to cast 'PORT' as an integer and
        # a default val of the commonly used flask port
        port=int(os.environ.get("PORT", "5000")),
        # set debug to true to allow us to debug code at the development stage
        debug=True
    )
