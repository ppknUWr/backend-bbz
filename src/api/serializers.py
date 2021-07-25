from django import db
from django.db.models import query
import api.json_worker as json_worker
from api.models import models
from bbz_project.settings import DEBUG

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

def serializer_get_db_data(db_id):
    #available_dbs = json_worker.get_models()['models'] #just debug
    selected_db = int(db_id) 
    #print(available_dbs[selected_db], "\n")

    raw_db_data = models[selected_db]

    #get all fields available in the model
    print(raw_db_data._meta.get_fields(), "\n")

    db_fields = [field.name for field in raw_db_data._meta.get_fields()]
    print(db_fields)
    #dumb as fuck
    querylength = len(list(raw_db_data.objects.values_list(db_fields[0], flat=True)))
    #print(querylength)
    db_data = {key : {} for key in range(0, querylength)}
    #print(db_data)

    for field in db_fields:
        fieldset = list(raw_db_data.objects.values_list(field, flat=True))
        index = 0
        for value in fieldset:
            db_data[index].update({field : value})
            index += 1
        
    #for x in range(querylength):
    #    print(db_data[x], "\n")
    
    return db_data