import json
import os

"""
Functon to fetch MODELS from data/models.json
@Param: -
@Return: dict: models -> JSON files that handle dynamic models
"""

def get_models():
    with open("api/data/models.json", "r") as json_file:
        data = json.load(json_file)
        return data