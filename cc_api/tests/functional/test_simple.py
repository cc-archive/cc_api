from cc_api.tests import *

class TestSimpleController(TestController):

    def test_chooser(self):

        response = self.app.get('/simple/chooser')
        self.assertEqual(response.status, 200)

    def test_chooser_js(self):

        response = self.app.get('/simple/chooser.js')
        self.assertEqual(response.status, 200)

