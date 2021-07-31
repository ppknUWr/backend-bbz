from django.test import TestCase

from api.models import models
from rest_framework.test import APITestCase
from django.urls import reverse
import api.json_worker as json_worker
import os
import json

# Create your tests here.

class APITestDynamicModels(APITestCase):

    def test_if_ammount_of_dynamic_models_are_equal_to_json(self):
        data_json = json_worker.get_models()
        self.assertTrue(len(models) == len(data_json["models"]))

    def test_if_names_are_equal_to_json_names(self):
        data_json = json_worker.get_models()
        models_names = list()
        for model in models:
            models_names.append(model._meta.object_name)
        self.assertEqual(models_names, data_json["models"])


class APITestEndpoints(APITestCase):

    def test_if_db_names_return_data(self):
        response = self.client.get('/api/db_names')
        self.assertEqual(200, response.status_code)
        
    def test_if_db_names_return_data_correctly(self):
        response = self.client.get('/api/db_names')
        data_json = json_worker.get_models()
        response_json = json.loads(response.content)
        response_json_names = list()

        for item in response_json['result']['names']:
            response_json_names.append(item['name'])

        self.assertEqual(response_json_names, data_json["models"])


