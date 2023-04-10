# UOCIS322 - Project 5 #

## Update

## Description
* This project is an implementation of a controle time calculator that is based on RUSA's calculator. 
* The page allows the user to select a brevet distance and then  enter control point distances in km or miles within the brevet. * The calculator returns back the open and close times per the rules outlined on the RUSA site.
* This implementation allows for storage of a set of control points using MongoDB.


## Algorithm
 * The algorithm works by taking a date entered and adding a certain amount of time that is calculated by dividing a the distance
   by a given rate. The rates are on RUSA's website and a further explanation about how exactly times are calculated. For the
   most part the calculation is a leg distance divided by that legs fastest rate for the open time and slowest for close. Each
   leg is calculated then summed together for a final time. 
 * `An example could be 890 in a 1000km brevet. The first leg 0-200 = 200/ 34, then 200-400 = 200/ 32 then 400-600 = 200 / 30 and finally 600-890 = 290 / 28.` Each of these results would be converted to minutes and hours and then applied to the start time. More information about what rates are used when can be found with the links below.
 
 * There are a few exceptions, all brevets * have a fixed ending time, even if the length is up to 20 percent over. The other    exception is that closing times for controls * within the first 60km have an increased window to allow those who started late to still race.

## Installation and Setup
* The first step to using this project is to clone the repo onto your local machine. You are going to want to make sure you have 
docker installed as well. Specifically you'll want to make sure you have docker compose available.
* You will then want to either modifify the port number in `brevets/default.ini` if you do not want to use the default port number of `5000`.
* After cloning the repo navigate into the `brevets` directory and run `docker compose up -d`. The `-d` flag is optional.
* Once the server is up and running you can navigate to your local host in the web browser at the portnumber you set earlier.


## Usage
* Once you have the program installed and setup the usage is rather simple. Select a brevet distance from the drop down, a start 
date from the calendar and then enter control distances in either miles or km. 
* After entering the value and clicking out of the box the open and close time's will be sent automatically. The page does prevent you from entering any `negative` distances as control points. 
* It also will alert you if you try to enter a control that is `too far` (more than 20 percent of the brevet) past the alloted buffer at the end.
* If you `clear` the calendar and try to submit a time`today's date and time` will be used.

* After entering the desired amount of `controls` you can hit the `submit` button and the results will be saved to a database. However it is worth noting with the current implementation only the most recent set of data sent using the `submit` button can be retrieved.
* If you wish to display the results you can press the `display` button and the results of the last submit will be displayed.

## Authors

Michal Young, Ram Durairajan. Updated by Ali Hassani.
