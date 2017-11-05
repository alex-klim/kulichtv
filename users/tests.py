from django.test import TestCase, Client
import unittest

class TestTwitterAuthView(unittest.TestCase):
    def setup(self):
        self.client = Client()

    def test_details(self):
        pass
