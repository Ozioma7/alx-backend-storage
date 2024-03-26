#!/usr/bin/env python3
""" MongoDB Operations using pymongo """


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document based on kwargs """
    return mongo_collection.insert(kwargs)
