
# Section: Import modules
import django
import os
import json
import time

pl_alphabet = [
    'a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i',
    'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's',
    'ś', 't', 'u', 'w', 'y', 'z', 'ź', 'ż'
] # Polish alphabet to keep .json files in correct order - related to those in Django Database.

# Section: Django setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bbz_project.settings")
django.setup()

from api.models import *
import api.json_worker as json_worker
from django.contrib.auth.models import User

u = User.objects.get(username = "root") # Default user for any bibliography

# Section: Get data from JSON
path_to_json = "../convert/database_json/" # Path to directory that have all .json files
json_files = os.listdir(path_to_json) # Get names of .json files to list

"""
convert_json_to_dict
Function open file, convert .json data to dict and return it
@Param: json_file: File - File that is .json
@Return: data: Dict - converted data from .json to dict
"""
def convert_json_to_dict(json_file):

    with open(path_to_json + json_file, "r+") as f:
        # if json_file != "Opis rekordu bibliograficznego PHC.json": # Prevent "Opis rekordu" to add when someone add it to database_json
        # print(json_file)
        data = json.load(f)
        return data

"""
dict_values_to_str
Convert values of dictionary to one string. Each value execpt the first is added with ", "
@Param: dict_data: Dict - dictionary to convert
@Return: string: Str - string that contain values of dictionary
"""
def dict_values_to_str(dict_data):
    string = ", ".join(dict_data.values())
    return string

"""
nest_dict_data
Function to convert all dictionary data to one pattern.
@Param: dict_data: Dict - raw model from .json file
@Return: models_list: List - list of models nested and reworked to one pattern
"""
def nest_dict_data(dict_data):

    models_list = list() # Empty list

    for id in dict_data:
        
        record = dict() # Record, that we're working on

        for field in dict_data[id]:

            """
            If type of any record is DICTIONARY it got converted to string, that handles VALUES of string
            Example:

            if there's field like that:
            "publication_date": {
                "1": 1920,
                "2": 1933
            }

            it will be converted to publication_date = "1920, 1933"
            """
            if type(dict_data[id][field]) == dict:
                converted_data = dict_values_to_str(dict_data[id][field])
                record[field] = converted_data

            elif type(dict_data[id][field]) == str:
                record[field] = dict_data[id][field]

        models_list.append(record)

    return models_list



# Section: Initializer 

if __name__ == "__main__":
    print("[INFO] Script is working.")

    models_django = list() # List handles all models loaded, and pass to admin.py
    models_script = list()
    models_from_json = json_worker.get_models("/data/models.json") # IMPORTANT: Function from json_worker.py

    for model in models_from_json["models"]:
        model = NewBibliographyDynamicModel(BibliographyTemplateModel, model) # Initialise new DynamicModel
        models_django.append(model)

    json_files = sorted(json_files, key = lambda x: pl_alphabet.index(x[0].lower())) # Sort json_files to polish correct order - related to Django Models in DB.


    for file in json_files:
        dict_data = convert_json_to_dict(file)
        models_from_dict_data = nest_dict_data(dict_data) 
        models_script.append(models_from_dict_data)

    models_django_len = len(models_django)

    # for index, model in enumerate(models_django):
        
    #     for data in models_script[index]:

    #         model.objects.create(
    #             author = u, 
    #             book_author = data['record_author'],
    #             co_authors = data['record_coauthor'],
    #             editor = data['record_editor'],
    #             title = data['record_title'],
    #             subtitle = data['record_subtitle'],
    #             original_edition = data['record_original_edition'],
    #             series = data['record_series'],
    #             publication_date = data['record_publication_date'],
    #             publication = data['record_edition'],
    #             publication_place = data['record_place_of_publication'],
    #             publisher = data['record_publisher'],
    #             source = data['record_source'],
    #             number = data['record_volume'],
    #             notebook = data['record_issue'],
    #             pages = data['record_pages'],
    #             language = data['record_language'],
    #             isbn_or_issn_number = data['record_issn'],
    #             doi_number = data['record_doi'],
    #             link = data['record_source_link'],
    #             keywords_and_content = data['record_keywords'],
    #             comments = data['record_additional_info']
    #         )
    #         print(f"Adding: {data['record_title']} to database.")
    #         time.sleep(0.1) # Sleep is necessary here, because if we don't assign delay, Django is going to add records too fast, and everything will collapse. IMPORATANT!!!
            