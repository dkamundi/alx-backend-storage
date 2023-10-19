#!/usr/bin/env python3
"""inserts a new document in a collection based on kwargs"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    returns new id
    """
    id = mongo_collection.insert(kwargs)
    return id
