# HackTheMap
## Inspiration
Our team was initially brought together by one common interest: a Hackathon! Hackathons are competitive programming events where people can build innovative projects and network with like-minded individuals. 

In other words, it is the perfect place to find hackers from the local community. 

However, many of us have a hard time in finding them, especially in-person hackathons, and usually miss out on registration. Sure, there are plenty of hackathon websites but without the right tool, hackers unfortunately miss out on these amazing events just because they are not aware that they are ongoing!

In the spirit of friendship and bringing hackers together, we created HacktheMap.

**HacktheMap provides an intuitive interface with 2 simple goals:**
- Help individuals find the in-person hackathons happening at their local areas
- Unite hackers from all corners of the world and hopefully see amazing friendships sprout and thrive!

## What it does
HacktheMap is a web app that aims to help users find hackathons near them. When the user goes to the website, they will be taken to the homepage. They can click the Explore button in the homepage, in which they will be taken to the interactive map that has active hackathons. The user can looks through the in-person hackathons and sign up for the ones they are interested in. Furthermore, the user can contact the admin via the Contact Us page as well as read about the goals. 

## How we built it
- UI Design: Figma
- Frontend: HTML, CSS, Javascript
- Backend: Flask(with Python)
- Styling: Tailwind CSS

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

## Setting up scheduled, automated web scrapping
If you would like HackTheMap to update itself automatically and in real time, one suggestion is to use a cron job when hosting.
First, find the full path to the scrapper.py script folder and python3:
```bash
$ pwd
$ which python3
```

Then, you may edit your crontab file or make one if it does not exist:
```bash
$ crontab -e
```

The crontab file will open on the VIM editor (or your default editor), add the cron command with the scheduled frequency you would like the script to scrape the data
Here is an example of the data being scrapped hourly (every hour, it updates the data in real time to be displayed on map):
```bash
0 * * * * ( insert here full path to python3 )( insert here full path to the scrapper.py directory )
```

You can use the following command to verify cron job was successfully added:
```bash
$ crontab -l
```

This will ensure the dataset.json file is up to date every hour.
