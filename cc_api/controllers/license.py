import logging

from cc_api.lib.base import *

log = logging.getLogger(__name__)

class LicenseController(BaseController):

    def index(self, license_class):
        # Return a rendered template
        #   return render('/some/template.mako')
        # or, Return a response
        return 'Hello World'

    def issue(self, license_class):
        pass

    def get(self, license_class):
        pass
