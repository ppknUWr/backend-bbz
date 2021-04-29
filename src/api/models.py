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
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE) #2 - Autor (Powiązanie jeden-do-wielu z użytkownikiem.)
    co_authors = models.CharField(max_length=256, default = "Bez współtwórcy.") #3 - Współtwórca (string)
    editor = models.CharField(max_length = 256, default = "Bez redaktora.") #4 - Redaktor (string)
    title = models.TextField(default = "Brak Tytułu.") #5 - Tytuł (string)
    subtitle = models.TextField(default = "Bez podtytułu.") #6 - Podtytuł (string)
    original_edition = models.TextField(default = "Bez wydania oryginalnego.") #7 - Wydane oryginalne (string)
    series = models.TextField(default = "Bez numeru serii.") #8 - Numer serii (string?)
    publication_date = models.SmallIntegerField(default = 1900) #9 - Rok wydania (SmallIntegerField (zakres: -32768 do 32767))
    publication = models.TextField(default = "Bez wydania.") #10 - Wydanie (string)
    publication_place = models.TextField(default = "Bez miejsca wydania.") #11 - Miejsce wydania (string)
    publisher = models.TextField(default = "Bez wydawcy.") #12 - Wydawca (string)
    source = models.TextField(default = "Bez źródła.") #13 - Źródło (string)
    number = models.TextField(default = "Bez numeru.") #14 - Numer (string)
    notebook = models.TextField(default = "Bez zeszytu.") #15 - Zeszyt (string)
    pages = models.SmallIntegerField(default = 0) #16 - Strony (SmallIntegerField (zakres: -32768 do 32767))
    language = models.TextField(default = "Bez języka.") #17 - Język (string)
    isbn_or_issn_number = models.TextField(default = "Bez numeru ISBN/ISSN.") #18 - ISBN/ISSN numer (string)
    doi_number = models.TextField(default = "Bez numeru DOI.") #19 - Numer DOI (strng)
    link = models.URLField(max_length=200) #20 - Link (URLField)
    keywords_and_content = models.TextField(default = "Bez słów kluczowych/zawratości.") #21 - Słowa kluczowe, zawartość (string)
    comments = models.TextField(default = "Bez komentarzy.") #22 - Komentarze (string)

    def __str__(self):
        return self.name
 
    class Meta:
        abstract = True

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
models = list() # List handles all models loaded, and pass to admin.py
models_from_json = json_worker.get_models() # IMPORTANT: Function from json_worker.py

for model in models_from_json["models"]:
    model = NewBibliographyDynamicModel(BibliographyTemplateModel, model) # Initialise new DynamicModel
    models.append(model) # Append new dynamc model to list, to pass it to admin.py

