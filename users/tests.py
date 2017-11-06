from django.test import TestCase, Client


class TestTwitterAuthView(TestCase):
    def setUpTestData(cls):
        cls.client = Client()

    def test_details(self):
        pass
