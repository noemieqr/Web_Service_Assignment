#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 13:22:34 2018

@author: noemiequere
"""

from flask import Flask
from marshmallow import Schema, fields, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()

class Property(db.Model):
    __tablename__ = 'bien_immobilier'
    property_id = db.Column(db.Integer, primary_key=True)
    property_name = db.Column(db.String(20))
    description = db.Column(db.String(120))
    type_prop = db.Column(db.String(20))
    city = db.Column(db.String(20))
    rooms = db.Column(db.Integer)
    car_rooms = db.Column(db.String(120))
    owner_id = db.Column(db.Integer, db.ForeignKey('utilisateurs.user_id', ondelete='CASCADE'), nullable=False)
    owner = db.relationship('User', backref=db.backref('bien_immobiler', lazy='dynamic' ))


    def __init__(self, property_name, description, type_prop, city, rooms, 
                 car_rooms, owner_id):
        self.property_name = property_name
        self.description = description  
        self.type_prop = type_prop
        self.city = city
        self.rooms = rooms
        self.car_rooms = car_rooms
        self.owner_id = owner_id


class User(db.Model):
    __tablename__ = 'utilisateurs'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    surname = db.Column(db.String(150), nullable=False)
    city_of_interest = db.Column(db.String(150), nullable=False)
    birthDate = db.Column(db.Date)

    def __init__(self, name, surname, city_of_interest, birthDate):
        self.name = name
        self.surname = surname  
        self.city_of_interest = city_of_interest
        self.birthDate = birthDate

class UserSchema(ma.Schema):
    user_id = fields.Integer()
    name = fields.String(required=True)
    surname = fields.String(required=True)
    city_of_interest = fields.String(required=True)
    birthDate = fields.Date()


class PropertySchema(ma.Schema):
    property_id = fields.Integer(dump_only=True)
    owner_id = fields.Integer(required=True)
    property_name = fields.String(required=True, validate=validate.Length(1))
    description = fields.String(required=True)
    type_prop = fields.String(required=True)
    city = fields.String(required=True)
    rooms = fields.Integer(required=True)
    car_rooms = fields.String(required=True)