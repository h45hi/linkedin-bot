# Linkedin Bot
A selenium based LinkedIN bot which will search for given post and download their resume. I developed it for HR/ Recruitment executive to automate the process of browsing for candidates and downloading their resume.

## Cloning repo to local machine
In order to clone this repo to your local machine execute the following

```bash
$ git clone git@github.com:h45hi/linkedin-bot.git
```

## Create a virtual environment
It is always a good practice to run each project in isolated environment. To create an isolated environment execute the following command after moving into directory.

```bash
$ virtualenv venv
```
## Activating virtual environment
Now that the environment is created, it's time to activate.
For Linux
```bash
$ source venv/bin/activate
```
For Windows
```bash
\venv\Scripts\activate
```
After successfully activating virtual environment you will see (venv) at start of terminal/cmd line.

## Installing dependencies
### Python dependencies
In order for script to work it depends on some external libraries, to install all dependencies execute

```bash
$ pip install -r requirements.txt
```
### Drivers
For running script in chrome, download [driver](https://sites.google.com/a/chromium.org/chromedriver/).
For running script in firefox, download [driver](https://github.com/mozilla/geckodriver/releases).
Please remember to place driver in location
```bash
$ usr/bin
```
## Execute script
After installing all dependencies script can execute sucessfully, to run execute

 ```bash
$ python linkedin_bot.py
```
