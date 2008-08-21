from cc_api.tests import *

class TestSupportController(TestController):

    def test_jurisdictions(self):

        response = self.app.get('/support/jurisdictions')
        self.assertEqual(response.status, 200)

    # Make sure that passing the ?locale= arg works
    def test_jurisdictions(self):

        response = self.app.get('/support/jurisdictions?locale=hr')
        self.assertEqual(response.status, 200)

    def test_jurisdictions_js(self):

        response = self.app.get('/support/jurisdictions.js')
        self.assertEqual(response.status, 200)
