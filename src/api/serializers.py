from django import db
from django.db.models import query
import api.json_worker as json_worker
from api.models import models, MetaDBInfo
from bbz_project.settings import DEBUG
import datetime
import json

"""
Function to serialize dynamic models into JSON format
@Param:
@Return: data: Dict -> Dictionary with names of models & information code
"""

def serializer_prepare_model_names():
    data = list()
    meta_db_info = MetaDBInfo.objects.values()
    for x in meta_db_info:
        data.append(x)
    return data

"""
Function to serialize data from database model into JSON format
@Param: db_id: int
@Return: data: Dict -> Dictionary with all data from a model database
"""
def serializer_get_db_data(db_id):
    selected_db = int(db_id) 
    raw_db_data = models[selected_db]

    #get all fields available in the model in a form of list
    db_fields = [field.name for field in raw_db_data._meta.get_fields()]
    #check how many records are in the selected database
    querylength = len(list(raw_db_data.objects.values_list(db_fields[0], flat=True)))
    #initialise JSON object to be retrieved
    db_data = {key : {} for key in range(0, querylength)}

    #get all data from db into db_data
    for field in db_fields:
        #get fields for selected param, e.g. all author fields
        fieldset = list(raw_db_data.objects.values_list(field, flat=True))
        index = 0
        #put the field to corresponding dictionary
        for value in fieldset:
            db_data[index].update({field : value})
            index += 1

    return db_data

"""
Function to serializer given data to update record
@Param: db_id: Int -> ID of Table to update
@Param: record_id: Int -> ID of Record to update
@Param: data: Dict -> Dictionary that handles key, values of updateded record
@Return: response: Dict -> Updated record or response with error
"""
def serializer_update_record(db_id, record_id, data):
    record = models[db_id].objects.get(id = record_id)

    list_of_fields_in_record = [f.name for f in record._meta.get_fields() if f.name != "id"]
    list_of_fields_in_data = [key for key, value in data.items()]
    response = dict()

    def validate_data():
        # Check, if fields in JSON data are the same like in model.
        if(list_of_fields_in_data == list_of_fields_in_record):
            return True
        else:
            return False

    def change_record_to_data_in_patch():
        record.book_author = data['book_author']
        record.co_authors = data['co_authors']
        record.editor = data['editor']
        record.title = data['title']
        record.subtitle = data['subtitle']
        record.original_edition = data['original_edition']
        record.series = data['series']
        record.publication_date = data['publication_date']
        record.publication = data['publication']
        record.publication_place = data['publication_place']
        record.publisher = data['publisher']
        record.source = data['source']
        record.number = data['number']
        record.notebook = data['notebook']
        record.pages = data['pages']
        record.language = data['language']
        record.isbn_or_issn_number = data['isbn_or_issn_number']
        record.doi_number = data['doi_number']
        record.link = data['link']
        record.keywords_and_content = data['keywords_and_content']
        record.comments = data['comments']
        record.save()

    # If validate data is true, then return response and update record
    if validate_data():

        change_record_to_data_in_patch()

        response["code"] = 1
        response["message"] = {
            "book_author": record.book_author,
            "co_authors": record.co_authors,
            "editor": record.editor,
            "title": record.title,
            "subtitle": record.subtitle,
            "original_edition": record.original_edition,
            "series": record.series,
            "publication_date": record.publication_date, 
            "publication": record.publication,
            "publication_place": record.publication_place,
            "publisher": record.publisher,
            "source": record.source,
            "number": record.number,
            "notebook": record.notebook,
            "pages": record.pages,
            "language": record.language,
            "isbn_or_issn_number": record.isbn_or_issn_number,
            "doi_number": record.doi_number,
            "link": record.link,
            "keywords_and_content": record.keywords_and_content,
            "comments": record.comments
        }

        response["timestamp"] = int(datetime.datetime.now().timestamp())
    
    else:

        missed_keys = set(list_of_fields_in_record) - set(list_of_fields_in_data)
        missed_keys_str = [str(key) for key in missed_keys]

        response["code"] = 2
        response["message"] = "Error, you probably missed one of keys, needed to update record (%s)" % missed_keys_str
        response["timestamp"] = int(datetime.datetime.now().timestamp())

    return response

def serializer_add_new_record(db_id, data):
    print(data)
    selected_db = models[db_id]
    #need to get the rules of a record being valid and apply it to the logic of the function
    def check_if_record_valid(x):
        return True
    
    selected_db.objects.create(book_author=data.get('book_author', 'None'),
        co_authors=data.get('co_authors', 'None'), editor=data.get('editor', 'None'), title=data.get('title'), subtitle=data.get('subtitle', 'None'),
        original_edition=data.get('original_edition', 'None'), series=data.get('series', 'None'), publication_date=data.get('publication_date', 'None'),
        publication=data.get('publication', 'None'), publication_place=data.get('publication_place', 'None'), publisher=data.get('publisher', 'None'),
        source=data.get('source', 'None'), number=data.get('number', 'None'), notebook=data.get('notebook', 'None'), pages=data.get('pages', 'None'), language=data.get('language', 'None'),
        isbn_or_issn_number=data.get('isbn_or_issn_number', 'None'), doi_number=data.get('doi_number', 'None'), link=data.get('link', 'None'),
        keywords_and_content=data.get('keywords_and_content', 'None'), comments=data.get('comments', 'None'))
    
    return True

def serializer_remove_record(db_id, record_id):
    print(f"Current db id is: {db_id} and record id is: {record_id}")
    return {}