import os
import json
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()  # Loads the environment variables from the .env file

app = Flask(__name__)

os.getenv("API_KEY")
def load_info_from_json(filename) -> dict:
    """
    Loads profile data by parsing the JSON file provided.

    :param: The JSON file to parse
    :return: A dict containing all the JSON info parsed
    """
    # Get the relative path for the JSON data
    path = f'{os.getcwd()}/{filename}'
    # Open the file and return its parsed contents
    # UTF-8 encoding is used to parse apostrophes correctly
    with open(path, "r", encoding='utf8') as file:
        return json.load(file)

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
    data = load_info_from_json('run_results.json')
    info = data["data"]
    return render_template('mymap.html', info=info, url=os.getenv("URL"), API_KEY=os.getenv("API_KEY"))

# Route for handling 404 errors
@app.errorhandler(404)
def not_found(e):
    """
    Redirects any invalid URL to the landing page.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)