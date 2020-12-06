CS6400 
David Lim, Eric Hsieh, Jiajie Lin

Installing Instructions:

Clone this repo. Make sure MongoDB is installed.
This was tested on Sunday, December 6 on MacOS with:

	$ brew tap mongodb/brew
	$ brew install mongodb-community@4.4

For Python, this project was run on Python version 3.7.3 with the following packages:

	Flask, install with $ pip install flask
	MongoEngine, install with $ pip install mongoengine
	Requests, install with $ pip install requests
	Simplejson, install with $ pip install simplejson

Running Instructions:

To start the MongoDB database, in another terminal, run:

	$ mongod --config /usr/local/etc/mongod.conf

Then, navigate to ../MySQL-and-Python/FlaskApp and run:

	$ python app.py

This python file is the backend for our project and takes care of all the data loading for MongoDB. The data is json_db_lite.json, and is automatically read in and loaded into the database by app.py.

If you want to see the data itself, it can be located at ../MySql-and-Python/json_db_lite.json, which is all the compiled data extracted from every json located in ../MySql-and-Python/jsons/

If more data is wanted, you can load a json into that folder and run ../MySql-and-Python/json_to_db.py.

Obtaining more data:

Install instagram-scraper with

	$ pip install instagram-scraper. 

To scrape more data, run:

	$ instagram-scraper cityname --tag --media-metadata --media-types none

This will download a json containing the top 9 posts with that tag. 

WARNING: As of Dec 6, 2020, there is still a block on instagram's API due to the election results and the spread of fake information. It may not be possible to pull a new json or run json_to_db.py due to these limitations.

