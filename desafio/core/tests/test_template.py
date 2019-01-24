from django.test import TestCase
import requests

class test_index(TestCase):
    def setUp(self):
        self.response = self.client.get('')

    def test_status_code(self):
        self.assertEqual(200, self.response.status_code)

    def test_min_info_home(self):
        '''Must have at least Title and banner '''
        texts = (
            ('id="id_title"'),
            ('id="id_banner"')
        )
        for text in texts:
            with self.subTest():
                self.assertContains(self.response, text)


class test_view_detail(TestCase):
    def setUp(self):
        self.response = self.client.get('/curso/1086/')

    def test_status_cod(self):
        self.assertEqual(200, self.response.status_code)

    def test_min_info_detail(self):
        '''Must have at least Title and banner '''
        texts = (
            ('id="id_title"'),
            ('id="id_banner"')
        )
        for text in texts:
            with self.subTest():
                self.assertContains(self.response, text)
