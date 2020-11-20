# Databases-Advanced
Opdracht Scraper
Commands to run in terminal to make Scraper.py work:
sudo apt-get update -y
sudo apt-get install -y python-beautifulsoup



Opdracht Mongo
Commands to enter into terminal to start up MongoDB Server:
sudo apt-get install mongodb
give ubuntu password
press enter
type y
press enter

when done type
sudo apt-get update, enter
sudo service mongodb start, enter, says job is already running if not this will start mongodb

mongo to go into mongodbshell

show dbs;, to show already made db's

to create new db
use mydb; 

to see which db you're in, db;

to insert something into the nosql collection in the db
db.mycol.inster({"name": "mark", "age": "50", ....});

show collections;

db.mycol.find();
