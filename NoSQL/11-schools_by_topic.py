#!/usr/bin/env python3
""" returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """ mongo_collection will be the pymongo collection object
    """
    documents = mongo_collection.find({"topics": topic})
    list_docs = [i for i in documents]
    return list_docs
