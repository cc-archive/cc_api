"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from pylons import config
from routes import Mapper

def make_map():
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('error/:action/:id', controller='error')

    # CUSTOM ROUTES HERE

    map.connect('', controller='generic', action='classes')
    map.connect('license/:license_class',
                controller='license', action='index')
    map.connect('license/:license_class/:action',
                controller='license')

    map.connect('simple/chooser.js', controller='simple',
                action='chooser_js')
    map.connect('simple/:action', controller='simple')

    map.connect('support/jurisdictions.js', controller='support',
                action='jurisdictions_js')
    map.connect('support/:action', controller='support')

    map.connect(':action', controller='generic')
    map.connect(':controller/:action/:id')
    map.connect('*url', controller='template', action='view')

    return map
