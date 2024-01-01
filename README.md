# Vocal commands

Vocal commands is a little application that able you to ask it to do sings, like give you the weather, search something on your web browser, etc.
## Features

- Can respond to "bonjour"
- Close the app if you say "Au revoir"
- Repeat what you said if you say "répéte"
- Give you the weather (only for Limoges only, still WIP) if you say "météo"
- Can search something on your browser with "cherche" followed by what you want to search



## Installation

First, create a venv:

Windows:
````
py -m venv venv
````
On linux:
````
python3 -m venv venv
````

Install the dependencies:

Windows:
````
.\venv\Scripts\activate
pip install -r requirements.txt
````

Linux:
````
source venv/bin/activate
pip install -r requirements.txt
````

If it doesn't work on linux (debian based), try this:
````
sudo apt-get install libasound-dev
sudo apt-get install portaudio19-dev
pip install --upgrade --force-reinstall pyaudio
pip install -r requirements.txt
````

Change the .env with the path of the web browser you want the application to use.
## Authors

- [@Namularbre](https://github.com/Namularbre)
