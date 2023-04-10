# UOCIS322 - Project 1 #

This project will get you started with creating a simple webpage server.

## Getting started

Directory structure:

* the "pages" (HTML files and their assets) will be located in DOCROOT. For this project that location is the `pages/` directory. Make sure you specify this in your `credentials.ini`!

* Everything that's located in `pageserver/`. That consists of a Python application (`pageserver.py`) that starts listening at a specified port and handles requests. This is the key file you'll be editing for this project.

* There's a configuration parser, much like the one seen in [project-0](https://github.com/UO-CIS322/project-0), but a more detailed version. It not only looks for your `credentials.ini` file, both in `pageserver/` and the parent directory and falls back to `default.ini` if missing, it also allows you to override those settings through CLI. These will be discussed in the lab.


## Grading Rubric

* If everything works as expected, 100 will be assigned.
* If existing pages and files are NOT handled correctly, 30 points will be docked.
* For each of the errors not handled correctly (403, and 404), 15 points will be docked.
* If `README.md` is not updated with your name and info, 10 points will be docked.
* If `credentials.ini` is commited, 10 points will be docked.
* If the repo clones, but `make install` or `make run` throws an error, 10 will be assigned.
* If `credentials.ini` is incorrect or not submitted, 0 will be assigned.

## Authors

Michal Young, Ram Durairajan.

## Updated Information
* Name: Jesse Baxter
* Position: Student at UO
* Contact: jbaxer@uoregon.edu

## Project Description

* There are no requirements for installion after the repo has been cloned. 

* The project starts a local python server via the `make start` command. Make start creates a server that can be accessed via the port in the `credentials.ini` file if present otherwise it defaults to `port 5000` in the `default.ini` file. This port can be changed and it is recommended to change it to less used random 4 digit number. 

* The server accepts only `GET` requests and will throw an error if any other type is presented. The server also forbids the use of `~` and `..` in queries and an error will be thrown if one is used. Other than these rules if a file name contains the query vale then that file will be returned. For example, a query of `example` would return a potential 
`example.txt` file.

* In order to stop the server the `make stop` command can be used. However, if that fails to kill the process the process ID can be found in the `,pypid.` file in the home directory. The command `kill -9 pid` can then be used.

* Information about starting and stopping the server can be found in the `start.sh` and 
`stop.sh` files. 
