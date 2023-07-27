# import the Flask class
from flask import Flask, render_template, request, flash
import os
import json
if os.path.exists("env.py"):
    import env

# create an instance of it and store it in a variable called 'app'
app = Flask(__name__)  # flask needs this to know where to look for
# templates & static files

app.secret_key = os.environ.get("SECRET_KEY")


# decorator to match URLs to view functions
@app.route("/")  # "/" indicates to browse the root directory
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    # initialise an empty list
    data = []
    # instruct Python to open the JSON file in order to read it
    # and assign the contents of the file to a new variable
    with open("data/company.json", "r") as json_data:
        # set the empty data list to equal the parsed JSON data
        data = json.load(json_data)
    # data list is passed in the return statement with the name of company
    return render_template("about.html", page_title="About", company=data)


# route for member details view
@app.route("/about/<member_name>")  # <> pass data from URL path to view
def about_member(member_name):
    # create an empty object to store the data
    member = {}
    # open the company.json file for read-only and refer to it as json_data
    with open("data/company.json", "r") as json_data:
        # create variable for the data that was pulled through
        data = json.load(json_data)
        # iterate through the data
        for obj in data:
            # check if object's url key(file) is equal to member_name(url)
            if obj["url"] == member_name:
                # set empty member to be equal to the obj instance in loop
                member = obj

    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


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
