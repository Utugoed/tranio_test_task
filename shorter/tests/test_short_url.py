from django.test import TestCase

from shorter.models import ShortUrl

class ShortUrlTest(TestCase):

    def test_short_url_with_wrong_url(self):
        url = "http://url.com"
        short_url = ShortUrl.create_code(url=url)

        self.assertEqual(short_url.pk, 3)
        self.assertEqual(short_url.url, url)
        self.assertEqual(short_url.usage_counter, 0)
        self.assertEqual(len(short_url.code), 6)