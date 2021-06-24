import json
import os
from bbz_project.settings import STATIC_ROOT

"""
Functon to fetch MODELS from data/models.json
@Param: -
@Return: data: Dict -> JSON files that handle dynamic models
Test commit
"""

def get_models():
    with open(STATIC_ROOT + "/data/models.json", "r") as json_file:
        data = json.load(json_file)
        return data