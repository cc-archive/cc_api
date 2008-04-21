from cc_api.tests import *

class TestLicenseController(TestController):

    def test_class_info(self):

        response = self.app.get('/license/standard')

        self.assert_(
            relax_validate('licenseclass.relax.xml', response.body)
            )

    def test_issue(self):

        response = self.app.post('/license/standard/issue')

    def test_get(self):

        response = self.app.get('/license/standard/get')
