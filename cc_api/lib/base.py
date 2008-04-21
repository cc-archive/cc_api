"""The base Controller API

Provides the BaseController class for subclassing, and other objects
utilized by Controllers.
"""
import os

from pylons import c, cache, config, g, request, response, session
from pylons.controllers import WSGIController
from pylons.controllers.util import abort, etag_cache, redirect_to
from pylons.decorators import jsonify, validate
from pylons.i18n import _, ungettext, N_
from pylons.templating import render

from babel.messages.pofile import read_po

import cc_api.lib.helpers as h
import cc_api.model as model

class BaseController(WSGIController):

    def _load_locale(self, language):
        po_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               '..',
                               'i18n',
                               language,
                               'cc_org.po')

        if not(os.path.exists(po_file)):
            po_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   '..',
                                   'i18n',
                                   'en',
                                   'cc_org.po')

        result = read_po(file(po_file, 'r'))
                
        # XXX inject the right key for the generic jurisdiction
        #result.strings['country.-'] = unicode.encode(
        #    result.get('util.Generic', 'Generic'), 'utf8')
        
        return result


    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']
        return WSGIController.__call__(self, environ, start_response)

# Include the '_' function in the public names
__all__ = [__name for __name in locals().keys() if not __name.startswith('_') \
           or __name == '_']
