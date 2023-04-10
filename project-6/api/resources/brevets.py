"""
Resource: Brevets

Credit to TodoList example for how to handle multiple object behavior.
"""
from flask import Response, request
from flask_restful import Resource


# You need to implement this in database/models.py
from database.models import Brevet

class BrevetsResource(Resource):
    def get(self):
        json_object = Brevet.objects().to_json()
        return Response(json_object, mimetype="application/json", status=200)
    
    def post(self):
        input_json = request.json
        result = Brevet(**input_json).save()
        return{'_id': str(result.id)}, 200