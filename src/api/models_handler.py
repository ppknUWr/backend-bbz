from api.models import models, MetaDBInfo, BibliographyTemplateModel, NewBibliographyDynamicModel

class ModelHandler():
    
    def __init__(self):
        self.current_models = models
    
    def __str__(self):
        print("Class for handling template models")
    
    def add_new_model(self, db_name):
        model = NewBibliographyDynamicModel(BibliographyTemplateModel, db_name)
        model._meta.verbose_name_plural = model._meta.db_table
        models.append(model)
        
        self.current_models = models
    
    def list_models(self):
        return(str(self.current_models))
