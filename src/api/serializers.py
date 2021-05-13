import api.json_worker as json_worker
from api.models import models

"""
Function to serialize dynamic models into JSON format
@Param:
@Return: data: Dict -> Dictionary with names of models & information code
"""
def serializer_prepare_model_names():
    data = dict()
    data["result"] = dict()
    data["result"]["names"] = list()
    for index, model in enumerate(models):
        data["result"]["names"].append({"id": index, "name": model._meta.object_name})

    if len(data["result"]["names"]) == len(models):
        data["result"]["code"] = 1 # CODE: Everything is ok
    else:
        data["result"]["code"] = 100 # CODE: Number of models returned from API is less/greater than dynamic models loaded into Django
    return data