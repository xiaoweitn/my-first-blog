from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from blog.views import post_list

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, post_list)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = post_list(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Xiao Wei Tan, Computer Science Student at the University of Birmingham</title>'
        , html)
        self.assertTrue(html.endswith('</html>'))
