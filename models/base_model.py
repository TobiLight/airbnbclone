#!/usr/bin/python3
# File: base_model.py
# Auhtors: Oluwatobiloba Light && 
"""
Defines a base model class BaseModel
"""

import uuid

class BaseModel():
    """
    Defines all common attributes/methods for other classes
    """
    def __init__(self, id=None, created_at=None, updated_at= None):
        """
        Initialize the class
        """
        
    def __str__(self):
        """Returns the string representation of the object"""
        return ""