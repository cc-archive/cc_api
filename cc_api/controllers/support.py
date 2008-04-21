import logging
import pylons

from cc_api.lib.base import *

import cc.license

log = logging.getLogger(__name__)

class SupportController(BaseController):

    def jurisdictions(self):
        """Return a sequence of options for a jurisdiction drop-down."""

        # determine the local to render the result in
        locale = request.params.get('language', 
                                    request.params.get('locale', 'en')
                                    )
        locale = cc.license.support.actual_locale(locale)

        # load the .po file for translating country names;
        # English is also loaded for use if the language doesn't have the 
        # string translated
        # XXX when Tower generates .po files they should include fallback
        locale = self._load_locale(locale)
        en = self._load_locale('en')

        select = request.params.get('select')

        if select:
            print '<select name="%s">\n' % select 

        # get a list of available jurisdictions
        jurisdictions = {}
        for j in cc.license.jurisdictions.launched():

            j_url = 'http://creativecommons.org/international/%s/' % j.id
            
            # we don't care about Unported here
            if j.id == '-':
                continue
            
            country_id = 'country.%s' % j.id

            if country_id in locale:
                country = locale[country_id].string
            elif country_id in en:
                country = en[country_id].string
            else:
                country = country_id
            
            jurisdictions[country] = u'<option value="%s">%s</option>\n' % (
                j_url, country)

        # sort the list and yield each item
        keys = jurisdictions.keys()
        keys.sort()
        for j in keys:
            print jurisdictions[j]

        if select:
            print '</select>\n' 

    def jurisdictions_js(self):

        pylons.response.headers['Content-Type'] = 'text/javascript'
        
        for result in self.jurisdictions():
            print "document.write('%s');\n" % result 
