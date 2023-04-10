"""
Jesse Baxter's Flask API.
"""

from flask import Flask
from flask import request
from flask import abort
import os
import configparser


app = Flask(__name__)
root= "/pages"



def parse_config(config_paths):
	"""
	Very similar to the code in project0, credit for the functionality to the author of Lab0
	Looks for files in directory to see if one matches the passed name. If there is no credentials.ini
	falls looks for default.ini. If credentials exist  it parses them and returns the parsed version
	of the file.

	input: config_paths
	A list of file titles to search for. Titles should be strings.

	returns: config
	A parsed version of the config file where major sections are the first key
	and variables under each section are the second key.
	Ex.
	[DEFAULT]
	NAME = name

	Name can be accesed via ["DEFAULT"]["NAME"]
	"""

	#Set default path to none so that it can be checked after looking for files
	config_path = None
	#Iterate through the directory to look for a matching file name
	for path in config_paths:
		#If file name matches return
		if os.path.isfile(path):
			config_path = path
			break
	#No update means file wasn't found, throw error
	if config_path is None:
		raise RuntimeError("Configuration file not found!")


	config = configparser.ConfigParser()
	config.read(config_path)
	return config


#Default response when sever is pinged without a query
@app.route("/")
def default_response():
	return "<h1>Welcome to the homepage!</h1>"


@app.errorhandler(404)
def page_not_found(e):
	with open(f'./{root}/404.html') as response:
		return response.read(), 404

@app.errorhandler(403)
def illegal_character(e):
	with open(f'./{root}/403.html') as response:
		return response.read(), 403

@app.errorhandler(400)
def illegal_request(e):
	with open(f'./{root}/400.html') as response:
		return response.read(), 400

#Handles responses that have a query attached to them
@app.route("/<query>")
def check_request(query):
	
	path = f'./{root}/{query}'
	#Only accept get requests, if another is sent respond with error.
	if request.method == 'GET':

		#Check for illegal characters, return 403 page and 403 code
		if ".." in query or "~" in query:
			abort(403)

		#If file is found return it's contents and 200 code
		elif os.path.isfile(path):
			with open(path) as response:
				return response.read(), 200
		
		#Return 404 page and 404 code
		else:
			abort(404)

	else:
		abort(400)


if __name__ == "__main__":
	#Search and parse config file to get debug and port values from credential.ini/default.ini
	config = parse_config(["credentials.ini", "default.ini"])
	debug = config["SERVER"]["DEBUG"]
	port = config["SERVER"]["PORT"]

	app.run(debug=debug, host="0.0.0.0", port=port)
