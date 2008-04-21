from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
_magic_number = 2
_modified_time = 1205793752.8312399
_template_filename='/home/nathan/p/cc_api/cc_api/templates/classes.xml'
_template_uri='/classes.xml'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding=None
_exports = []


def render_body(context,**pageargs):
    context.caller_stack.push_frame()
    try:
        __M_locals = dict(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        # SOURCE LINE 1
        context.write(u'<licenses>\n')
        # SOURCE LINE 2
        for cl in c.classes:
            # SOURCE LINE 3
            context.write(u'  <license id="')
            context.write(unicode(cl.name))
            context.write(u'">')
            context.write(unicode(cl.name))
            context.write(u'</license>\n')
        # SOURCE LINE 5
        context.write(u'</licenses>\n')
        return ''
    finally:
        context.caller_stack.pop_frame()


