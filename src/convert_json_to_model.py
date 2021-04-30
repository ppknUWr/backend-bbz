# TODO: Create Script to add data. :)

# Section: Import modules
import django
import os
import json

# Section: Django setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bbz_project.settings")
django.setup()

# Section: Get data from JSON
path_to_json = "../convert/database_json/" # Path to directory that have all .json files
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')] # Get names of .json files to list

"""
convert_json_to_dict
Function open file, convert .json data to dict and return it
@Param: json_file: File - File that is .json
@Return: data: Dict - converted data from .json to dict
"""
def convert_json_to_dict(json_file):
    
    with open(path_to_json + json_file, "r") as f:
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

    for file in json_files:
        dict_data = convert_json_to_dict(file)
        models_from_dict_data = nest_dict_data(dict_data)

        for model in models_from_dict_data:
            print(model)
        