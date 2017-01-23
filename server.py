from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE

@app.route("/")
def home_page():
    """shows homepage"""
    render_template("index.html")


@app.route("/application-form")
def app_form():
    """shows application page"""
    positions = ["Software engineer", "QA Engineer", "Product Manager"]

    render_template("application-form.html")

@app.route("/application-success")
def sub_form():

    appfirst = request.args.get("firstname")
    applast = request.args.get("lastname")
    appposition = request.args.get("position")
    
    return render_template("application-response.html", firstname=appfirst, lastname=applast, position=appposition)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
