try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='cc_api',
    version="",
    #description='',
    #author='',
    #author_email='',
    #url='',
    install_requires=['setuptools',
                      'zope.interface',
                      'zope.component',
                      'lxml',
                      "Pylons>=0.9.6.1",
                      ],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'cc_api': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors = {'cc_api': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', None),
    #        ('public/**', 'ignore', None)]},
    entry_points="""
    [paste.app_factory]
    main = cc_api.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller
    """,
)
