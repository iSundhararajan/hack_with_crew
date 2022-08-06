# hack_with_crew
## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the pip to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file with the following line:
API_KEY=YOUR_API_KEY

*Note: Add your own Google Maps API key in the .env file in order to use the map functionality*

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000`
