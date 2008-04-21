from cc_api.tests import *
import lxml.etree

class TestGenericController(TestController):

    def test_index(self):
        """/ is a synonym for /classes; make sure they return the same 
        value."""

        root_response = self.app.get('/')
        classes_response = self.app.get('/classes')

        self.assertEqual(root_response.body, classes_response.body)
        self.assertEqual(root_response.status, classes_response.status)

    def test_classes(self):

        response = self.app.get('/classes')

        self.assert_(
            relax_validate('classes.relax.xml', response.body)
            )

    def test_locales(self):

        response = self.app.get('/locales')

        self.assert_(
            relax_validate('locales.relax.xml', response.body)
            )

    def test_details(self):

        response = self.app.get('/details?license-uri=http://creativecommons.org/licenses/by/3.0/')

        parsed = lxml.etree.fromstring(response.body)

        # assert the existence of specific elements
        self.assert_( parsed.xpath('/result/license-uri') )
        self.assert_( parsed.xpath('/result/license-name') )
        self.assert_( parsed.xpath('/result/rdf') )
        self.assert_( parsed.xpath('/result/licenserdf') )
        self.assert_( parsed.xpath('/result/html') )

    def test_details_no_uri(self):

        response = self.app.get('/details')

        self.assert_(
            relax_validate('error.relax.xml', response.body)
            )

    
