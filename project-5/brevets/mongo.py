from pymongo import MongoClient
import os

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)

db = client.brevets

collection = db.controls_list


def insert_brevet(controls):
    """
    Inserts a list of dictionaries holding information on control points.

    Inputs a list titled 'brevets_list' which holds a list of controls as dictionaries. 

    Controls are made up of km, start_time, close_time
    
    brevets_list = [{miles: miles, km: km, location: location, start_time: start_time, close_time: close_time}, {}, {}]

    Returns the unique ID assigned to the document as a primary key.
    """
    output = collection.insert_one({
        "controls": controls
    })

    _id = output.inserted_id
    return str(_id)


def get_brevet():
    """
    Retrieves the most recent document in the controls_list collection in the brevets db.

    Returns controls(list of dictionaries representing a single control)
    """

    cont_list = collection.find().sort("_id", -1).limit(1)

    for brevets_list in cont_list:
        return brevets_list["controls"]