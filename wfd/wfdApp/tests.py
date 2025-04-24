from django.test import TestCase
from wfdApp.models import Item, Request
# Create your tests here.


class ModelTestCase(TestCase):
    def testObjectCreation(self):
        Item.objects.create()
