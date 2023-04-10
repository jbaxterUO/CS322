# UOCIS322 - Project 6 #

## Overview
This project took project five and re-organized `Brevets` into two separate services:

* Web (Front-end)
	* Time calculator (basically everything you had in project 4)
* API (Back-end)
	* A RESTful service to expose/store structured data in MongoDB.

## After Update

* Implemented a RESTful API in `api/`:
	* Data schema using MongoEngine for Checkpoints and Brevets was implemented:
		* `Checkpoint`:
			* `distance`: float, required, (checkpoint distance in kilometers), 
			* `location`: string, optional, (checkpoint location name), 
			* `open_time`: datetime, required, (checkpoint opening time), 
			* `close_time`: datetime, required, (checkpoint closing time).
		* `Brevet`:
			* `length`: float, required, (brevet distance in kilometers),
			* `start_time`: datetime, required, (brevet start time),
			* `checkpoints`: list of `Checkpoint`s, required, (checkpoints).
	* Using `/brevets/`:
		* GET `http://API:PORT/api/brevets` displays all brevets stored in the database.
		* GET `http://API:PORT/api/brevet/ID` displays brevet with id `ID`.
		* POST `http://API:PORT/api/brevets` inserts brevet object in request into the database.
		* DELETE `http://API:PORT/api/brevet/ID` deletes brevet with id `ID`.
		* PUT `http://API:PORT/api/brevet/ID` updates brevet with id `ID` with object in request.
	
## Usage

* Download repo and naviagate into the download. Run the command `cp .env-example .env` to make sure you have all your environment variables established. Afterwards run `docker compose up` to start the service. You can then naviage to `127.0.0.1:5002` and the brevets calculator from project-5 will be visable. 

* You can select a `brevet distance` and a `start date`. Then enter checkpoints and the times will be automatically calculated. After you are finished hit the `submit` button. The brevet information will be stored in a database using MongoDB. You can press the `display` button to retrive and display `the last submitted brevet`. As the name implies `clear` just clears all the input fields. 


## Authors

Michal Young, Ram Durairajan. Updated by Ali Hassani.
