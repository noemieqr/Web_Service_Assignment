#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 14:28:27 2018

@author: noemiequere
"""

from flask import jsonify, request
from flask_restful import Resource
from Model import db, User, Property, PropertySchema

properties_schema = PropertySchema(many=True)
property_schema = PropertySchema()

class PropertyResource(Resource):    
    #Un propriétaire ne peut modifier que les caractéristiques de son bien sans avoir accès à l’édition des autres biens.
    def post(self, property_id):
        
        if 'user-id' not in request.headers:
            return 'Pas de propriétaire spécifié'
        
        user_id = request.headers['user-id']
        
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'Aucune donnée renseignée'}, 400
           
        # Validate and deserialize input
        data, errors = property_schema.load(json_data)
        if errors:
            return {"status": "error", "data": errors}, 422
        
        property = Property.query.filter_by(property_id=property_id).first()
        if not property:
            return "Aucun bien n'a ce numéro"
        
        if int(user_id) != property.owner_id:
            return "L'utilisateur n'est pas le propriétaire de ce bien."
        
        property.owner_id=data['owner_id']
        property.property_name=data['property_name']
        property.description = data['description']  
        property.type_prop = data['type_prop']
        property.city = data['city']
        property.rooms = data['rooms']
        property.car_rooms = data['car_rooms']
    
        db.session.commit()

        result = property_schema.dump(property).data

        return {'status': "success", 'data': result}, 201
   
class PropertyCollectionResource(Resource):
#Les utilisateurs peuvent consulter uniquement les biens d’une ville particulière
    def get(self):
        
        #s'il n'y a pas de user id dans le header, alors liste tous les biens
        if 'user-id' not in request.headers:
            properties = Property.query.all()
            properties = properties_schema.dump(properties).data
            return {"status":"success", "data":properties}, 200
        
        user_id = request.headers['user-id']
        
        user = User.query.filter_by(user_id=user_id).first()
        if not user:
            return {'message': "Cet utilisateur n'existe pas"}, 400
        
        city = user.city_of_interest
        
        properties = Property.query.filter_by(city=city).all()
        if not properties:
            return {'message': "Aucun bien n'est listé dans cette ville"}, 400
        
        properties = properties_schema.dump(properties).data
        return {"status":"success", "data":properties}, 200
    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'Aucune donnée renseignée'}, 400
        # Validate and deserialize input
        data, errors = property_schema.load(json_data)
        if errors:
            return {"status": "error", "data": errors}, 422
        owner_id = User.query.filter_by(user_id=data['owner_id']).first()
        if not owner_id:
            return {'status': 'error', 'message': "Le propriétaire n'a pas été trouvé"}, 400
        property = Property(
            owner_id=data['owner_id'], 
            property_name=data['property_name'],
            description = data['description'],  
            type_prop = data['type_prop'],
            city = data['city'],
            rooms = data['rooms'],
            car_rooms = data['car_rooms']
            )
        db.session.add(property)
        db.session.commit()

        result = property_schema.dump(property).data

        return {'status': "success", 'data': result}, 201
