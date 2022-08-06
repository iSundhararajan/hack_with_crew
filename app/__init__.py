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

# Route for the profile page
@app.route('/map')
def map():
    """
    Loads profile dynamically from the JSON file and serves profile page.
    
    If profile could not be found, redirects to the landing page.
    """
    return render_template('map.html', url=os.getenv("URL"), API_KEY=os.getenv("API_KEY"))

# Route for handling 404 errors
@app.errorhandler(404)
def not_found(e):
    """
    Redirects any invalid URL to the landing page.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)