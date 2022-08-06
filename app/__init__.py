import os
import json
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()  # Loads the environment variables from the .env file

app = Flask(__name__)

os.getenv("API_KEY")

# Route for the landing page
@app.route('/')
def index():
    """
    Serves the landing page.
    """
    return render_template('index.html', title="HackTheMap", url=os.getenv("URL"))

# Route for the map page
@app.route('/map')
def map():
    return render_template('map.html', url=os.getenv("URL"), API_KEY=os.getenv("API_KEY"))


# Route for the account page
@app.route('/account')
def account():
    return render_template('account.html', url=os.getenv("URL"))

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contactus.html', url=os.getenv("URL"))


# Route for the goal page
@app.route('/goal')
def goal():
    return render_template('goals.html', url=os.getenv("URL"))

# Route for handling 404 errors
@app.errorhandler(404)
def not_found(e):
    """
    Redirects any invalid URL to the landing page.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)