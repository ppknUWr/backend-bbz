from django.db import models
import api.json_worker as json_worker

"""
ABSTRACT MODEL
Class BibliographyTemplateModel
Handles all fields that are in our bibliography databases.
"""
class BibliographyTemplateModel(models.Model):


    # FIELDS GO HERE
    id = models.IntegerField(primary_key=True) #1 - ID rekordu (integer)
    book_author = models.CharField(default = "Bez autora", max_length=512, verbose_name = "Autor książki") #2.5 - Autor (autor książki) 
    co_authors = models.CharField(max_length=256, default = "Bez współtwórcy.", verbose_name = "Współtwórca") #3 - Współtwórca (string)
    editor = models.CharField(max_length = 256, default = "Bez redaktora.", verbose_name = "Redaktor") #4 - Redaktor (string)
    title = models.TextField(default = "Brak Tytułu.", verbose_name = "Tytuł") #5 - Tytuł (string)
    subtitle = models.TextField(default = "Bez podtytułu", verbose_name = "Podtytuł") #6 - Podtytuł (string)
    original_edition = models.TextField(default = "Bez wydania oryginalnego.", verbose_name = "Wydanie oryginalne") #7 - Wydane oryginalne (string)
    series = models.TextField(default = "Bez numeru serii.", verbose_name = "Numer serii") #8 - Numer serii (string?)
    publication_date = models.TextField(default = "Brak roku wydania.", verbose_name = "Rok wydania") #9 - Rok wydania (TextField, string)
    publication = models.TextField(default = "Bez wydania.", verbose_name = "Wydanie") #10 - Wydanie (string)
    publication_place = models.TextField(default = "Bez miejsca wydania.", verbose_name = "Miejsce wydania") #11 - Miejsce wydania (string)
    publisher = models.TextField(default = "Bez wydawcy.", verbose_name = "Wydawca") #12 - Wydawca (string)
    source = models.TextField(default = "Bez źródła.", verbose_name = "Źródło") #13 - Źródło (string)
    number = models.TextField(default = "Bez numeru.", verbose_name = "Numer") #14 - Numer (string)
    notebook = models.TextField(default = "Bez zeszytu.", verbose_name = "Zeszyt") #15 - Zeszyt (string)
    pages = models.TextField(default = "0", verbose_name = "Ilość stron") #16 - Strony (Text Field (string))
    language = models.TextField(default = "Bez języka.", verbose_name = "Język") #17 - Język (string)
    isbn_or_issn_number = models.TextField(default = "Bez numeru ISBN/ISSN.", verbose_name = "Numer ISBN/ISSN") #18 - ISBN/ISSN numer (string)
    doi_number = models.TextField(default = "Bez numeru DOI.", verbose_name = "Numer DOI") #19 - Numer DOI (strng)
    link = models.URLField(max_length=1024, verbose_name = "Link/Załącznik") #20 - Link (URLField)
    keywords_and_content = models.TextField(default = "Bez słów kluczowych/zawratości.", verbose_name = "Słowa kluczowe") #21 - Słowa kluczowe, zawartość (string)
    comments = models.TextField(default = "Bez komentarzy.", verbose_name = "Komentarze") #22 - Komentarze (string)

    def __str__(self):
        return self.title
 
    class Meta:
        abstract = True
        verbose_name_plural = "Test"

"""
Class NewBibliographyDynamicModel
Class handle method to CREATE new dynamic model from BibliographyTemplateModel
"""
class NewBibliographyDynamicModel(object):
    _instance = dict()
 
    def __new__(cls, base_cls, tb_name):
        """
        Create Class
                 :param base_cls: class name
                 :param tb_name: table name
        :return: 
        """
        new_cls_name = tb_name
 
        if new_cls_name not in cls._instance:
            new_meta_cls = base_cls.Meta
            new_meta_cls.db_table = tb_name
            model_cls = type(str(new_cls_name), (base_cls,),
                {'__tablename__': tb_name, 'Meta': new_meta_cls, '__module__': cls.__module__})
            cls._instance[new_cls_name] = model_cls
        return cls._instance[new_cls_name]


"""
Initialise all models - initialise dynamic models
"""
models = list() # List handles all models loaded, and pass to admin.py & serializers.py, it's really important list
models_from_json = json_worker.get_models() # IMPORTANT: Function from json_worker.py

# models_from_json["models"] = sorted(models_from_json["models"]) # Keep the correct order in models, even when someone mades a typo and create a new model at the end of models.json with "a" on start

for model in models_from_json["models"]:
    model = NewBibliographyDynamicModel(BibliographyTemplateModel, model) # Initialise new DynamicModel
    model._meta.verbose_name_plural = model._meta.db_table # IMPORTANT: Set name of table in Django Admin Panel to table name - remove extra "s" from name.
    models.append(model) # Append new dynamc model to list, to pass it to admin.py



