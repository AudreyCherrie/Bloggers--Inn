from flask import Blueprint

auth =Blueprint('auth',__name__)
from . import views,forms

'''
a blueprint that handles the authentication request
'''
