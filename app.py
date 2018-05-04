#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 13:22:18 2018

@author: noemiequere
"""

from flask import Blueprint
from flask_restful import Api
from resources.User import UserResource
from resources.User import UserCollectionResource
from resources.Property import PropertyResource
from resources.Property import PropertyCollectionResource
#from flask.ext.sqlalchemy import SQLAlchemy

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(UserCollectionResource, '/User')
api.add_resource(UserResource, '/User/<int:user_id>')