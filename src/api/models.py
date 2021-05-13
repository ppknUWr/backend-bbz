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
    book_author = models.CharField(default = "Bez autora", max_length=512) #2.5 - Autor (autor książki) 
    co_authors = models.CharField(max_length=256, default = "Bez współtwórcy.") #3 - Współtwórca (string)
    editor = models.CharField(max_length = 256, default = "Bez redaktora.") #4 - Redaktor (string)
    title = models.TextField(default = "Brak Tytułu.") #5 - Tytuł (string)
    subtitle = models.TextField(default = "Bez podtytułu.") #6 - Podtytuł (string)
    original_edition = models.TextField(default = "Bez wydania oryginalnego.") #7 - Wydane oryginalne (string)
    series = models.TextField(default = "Bez numeru serii.") #8 - Numer serii (string?)
    publication_date = models.TextField(default = "Brak roku wydania.") #9 - Rok wydania (TextField, string)
    publication = models.TextField(default = "Bez wydania.") #10 - Wydanie (string)
    publication_place = models.TextField(default = "Bez miejsca wydania.") #11 - Miejsce wydania (string)
    publisher = models.TextField(default = "Bez wydawcy.") #12 - Wydawca (string)
    source = models.TextField(default = "Bez źródła.") #13 - Źródło (string)
    number = models.TextField(default = "Bez numeru.") #14 - Numer (string)
    notebook = models.TextField(default = "Bez zeszytu.") #15 - Zeszyt (string)
    pages = models.TextField(default = "0") #16 - Strony (Text Field (string))
    language = models.TextField(default = "Bez języka.") #17 - Język (string)
    isbn_or_issn_number = models.TextField(default = "Bez numeru ISBN/ISSN.") #18 - ISBN/ISSN numer (string)
    doi_number = models.TextField(default = "Bez numeru DOI.") #19 - Numer DOI (strng)
    link = models.URLField(max_length=200) #20 - Link (URLField)
    keywords_and_content = models.TextField(default = "Bez słów kluczowych/zawratości.") #21 - Słowa kluczowe, zawartość (string)
    comments = models.TextField(default = "Bez komentarzy.") #22 - Komentarze (string)

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

for model in models_from_json["models"]:
    model = NewBibliographyDynamicModel(BibliographyTemplateModel, model) # Initialise new DynamicModel
    model._meta.verbose_name_plural = model._meta.db_table # IMPORTANT: Set name of table in Django Admin Panel to table name - remove extra "s" from name.
    models.append(model) # Append new dynamc model to list, to pass it to admin.py

