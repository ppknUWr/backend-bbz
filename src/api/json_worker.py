import json
import os
from bbz_project.settings import STATIC_ROOT

"""
Functon to fetch MODELS
@Param: -
@Return: data: Dict -> JSON files that handle dynamic models
"""

def get_models(path_to_file):
    with open(STATIC_ROOT + path_to_file, "r") as json_file:
        data = json.load(json_file)
        return data
