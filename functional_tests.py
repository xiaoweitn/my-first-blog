from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_there_are_posts(self):
        self.browser.get('http://127.0.0.1:8000')

        # There is a title
        self.assertIn('Xiao Wei', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__' :
    unittest.main(warnings='ignore')