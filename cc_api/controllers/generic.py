import logging

from cc.license import factory

from cc_api.lib.base import *

log = logging.getLogger(__name__)

class GenericController(BaseController):

    def index(self):

        return self.classes()

    def locales(self):
        return 'foo'

    def classes(self):

        c.classes = factory.LicenseFactory().license_classes()
        return render('/classes.xml')

    def details(self):
        pass

