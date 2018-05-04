#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 14:19:16 2018

@author: noemiequere
"""

from flask import request
from flask_restful import Resource
from Model import db, User, UserSchema

users_schema = UserSchema(many=True)
user_schema = UserSchema()

class UserResource(Resource):
    #user can access his personal information
    def get(self, user_id):
        user_id = request.headers['user-id']
        user_id = int(user_id)
        
        user = User.query.filter_by(user_id=user_id).first()
        return user_schema.dump(user).data
    
    #update new user
    def post(self, user_id):
        
        if 'user-id' not in request.headers:
            return "Pas d'utilisateur spécifié"
        user_id = request.headers['user-id']
        
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'Aucune donnée entrée'}, 400
        # Validate and deserialize input
        data, errors = user_schema.load(json_data)
        if errors:
            return errors, 422
        
        user = User.query.filter_by(user_id=user_id).first()
        if not user:
            return {'message': "Cet utilisateur n'existe pas"}, 400
        
        if int(user_id) != user.user_id:
            return "Vous n'etes pas sur votre page d'informations personelles."
        
        user.name=data['name']
        user.surname=data['surname']
        user.city_of_interest=data['city_of_interest']
        user.birthDate=data['birthDate']
     
        db.session.commit()

        result = user_schema.dump(user).data

        return { "status": 'success', 'data': result }, 201
    
    
    #delete user
    def delete(self, user_id):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = user_schema.load(json_data)
        if errors:
            return errors, 422
        
        user = User.query.filter_by(user_id=user_id).first()
        if not user:
            return "Cet utilisateur n'existe pas!"
        
        if int(user_id) != user.user_id:
            return "L'utilisateur n'est pas sur sa page page d'informations personelles."
        
        db.session.delete(user)
        db.session.commit()

        result = user_schema.dump(user).data

        return { "status": 'success', 'data': result}, 204

class UserCollectionResource(Resource):
    #get all users
    def get(self):
        users = User.query.all()
        users = users_schema.dump(users).data
        return {'status': 'success', 'data': users}, 200
    
        #create user
    def put(self):        
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400

        data, errors = user_schema.load(json_data)
        if errors:
            return errors, 422
        
        user = User(
            name = data['name'], 
            surname=data['surname'],
            city_of_interest=data['city_of_interest'],
            birthDate = data['birthDate']
            )
        db.session.add(user)
        db.session.commit()

        result = user_schema.dump(user).data
        return { 'status': 'success', 'data': result }, 201
    
    
    