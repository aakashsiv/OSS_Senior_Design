from django.test import TestCase

class ApiTests(TestCase):
    def setUp(self):
        pass

    def test_api_exists(self):
        """Animals that can speak are correctly identified"""
        self.assertEqual(False, True)