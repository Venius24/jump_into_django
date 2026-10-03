from django.apps import apps
from django.conf import settings
from django.test import SimpleTestCase
from django.urls import reverse


class SiteSmokeTests(SimpleTestCase):
    def test_pages_open(self):
        for url in ('/', reverse('catalog:product_list')):
            with self.subTest(url=url):
                self.assertEqual(self.client.get(url).status_code, 200)

    def test_static_url_is_a_url_and_directory_is_registered(self):
        self.assertEqual(settings.STATIC_URL, '/static/')
        self.assertIn(settings.BASE_DIR / 'static_dev', settings.STATICFILES_DIRS)

    def test_cinema_models_are_registered(self):
        self.assertIsNotNone(apps.get_model('cinema', 'OriginalTitle'))
        self.assertIsNotNone(apps.get_model('cinema', 'VideoProduct'))
