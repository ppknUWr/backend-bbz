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

"""
Function to serializer given data to update record
@Param: db_id: Int -> ID of Table to update
@Param: record_id: Int -> ID of Record to update
@Param: data: Dict -> Dictionary that handles key, values of updateded record
@Return: response: Dict -> Updated record or response with error
"""
def serializer_update_record(db_id, record_id, data):
    record = models[db_id].objects.get(id = record_id)

    list_of_fields_in_record = [f.name for f in record._meta.get_fields() if f.name != "id" and f.name != "author"]
    list_of_fields_in_data = [key for key, value in data.items()]

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

        response = {
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
    
    else:
        response = {"message": "You provided wrong JSON to update record"}
    return response
        