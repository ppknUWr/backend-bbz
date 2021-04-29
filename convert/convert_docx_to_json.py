from docx import Document
import json
import glob
import os
import docx2txt

# known issues:
# 1
# it's hardcoded that the record values start after 18 line

# you can freely rename any of the dictionary value, not key, if you need to 
record_dictionary = {
    1 : "record_id",
    2 : "record_author",
    3 : "record_coauthor",
    4 : "record_editor",
    5 : "record_title",
    6 : "record_subtitle",
    7 : "record_original_edition",
    8 : "record_series",
    9 : "record_publication_date",
    10 : "record_edition",
    11 : "record_place_of_publication",
    12 : "record_publisher",
    13 : "record_source",
    14 : "record_volume",
    15 : "record_issue",
    16 : "record_pages",
    17 : "record_language",
    18 : "record_issn",
    19 : "record_doi",
    20 : "record_source_link",
    21 : "record_keywords",
    22 : "record_additional_info",
}

# creates new folder in current working directory
current_directory = os.getcwd()
new_directory = os.path.join(current_directory, r"database_json")
if not os.path.exists(new_directory):
    os.makedirs(new_directory)

# order of record values in input file
order = [2, 9, 5, 13, 20]
for database_file in glob.glob("*.docx"):
    print("Working on: ", database_file)
    
    # read data from file as txt
    text = docx2txt.process(database_file)

    # main dictionary of current file
    result_dictionary = {}

    # dictionary of singular record
    available_records_dict = {}
    # id that singular record recives
    local_id = 0
    # splits text into lines
    # skips 18 lines that are not important
    for lines in text.split("\n")[18:]:
        # resets singular record
        available_records_dict = {}
        record_index = 0
        # default values
        for record in record_dictionary:
            if(record != 1):
                available_records_dict[record_dictionary[record]] = "None"

        # splits given string to
        for value in lines.split("', '"):
            for z in value.split("'"):
                try:
                    if(z != "'" and z != ""):
                        available_records_dict[record_dictionary[order[record_index]]] = z
                        record_index += 1
                except:
                    continue

        # pass empty record
        pass_record = True
        for key in available_records_dict:
            if(available_records_dict[key] != "None" and available_records_dict[key] != None):
                pass_record = False

        # if not empty then add that to main record
        if(pass_record == False):
            result_dictionary[local_id] = available_records_dict
            local_id += 1
    # save to file
    
    with open("database_json/" + str(database_file.strip("docx") + "json"), 'w', encoding = "utf-8") as outfile:
            outfile.write(json.dumps(result_dictionary, sort_keys = False, indent = 6, ensure_ascii = False))





