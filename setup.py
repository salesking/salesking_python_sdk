import setuptools

CLASSIFIERS = [
    'Development Status :: 1 - Alpha',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: APACHE / MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]


setuptools.setup(
    name='salesking',
    version='0.0.1',
    description='SalesKing API Wrapper and SDK',
    author='Frank Bieniek',
    author_email='fb@saleking.de',
    url='http://github.com/salesking/salesking_python_sdk',
    packages=['salesking','warlock'],
    install_requires=[
        'requests',
        'requests-oauth',
        'certifi>=0.0.7',
        'oauthlib',
        'chardet>=1.0.0',
        'jsonpatch==0.10',
        'jsonpointer==0.5',
        'jsonschema>=0.7,<1',
        'validictory==0.8.3'
        
    ],
    dependency_links = [
        'git+git://github.com/robbrit/warlock.git#egg=warlock-0.9.3',
    ],             
    tests_require=[
        'mock==0.2.1',
    ],
    include_package_data=True,
    zip_safe = False,
    #test_suite = 'runtests.main',
    
)