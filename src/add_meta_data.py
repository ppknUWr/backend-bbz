import django
import json
import os

from django import db

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bbz_project.settings")
django.setup()

from api.models import MetaDBInfo
import api.json_worker as json_worker
from django.contrib.auth.models import User

u = User.objects.get(username = "root") # Default user for any bibliography
path_to_json = "/data/meta_data.json"

if __name__ == "__main__":
    print("Starting saving meta data")
    meta_data = json_worker.get_models(path_to_json)
    #print(meta_data)
    db_meta = [MetaDBInfo(db_name = x['db_name'], real_db_name = x['real_db_name'], author = x['author']) for x in meta_data]
    MetaDBInfo.objects.bulk_create(db_meta)
    
