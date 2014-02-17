"""
Flask-conditional
------------------
Conditional decorators for Flask routes.
"""
from setuptools import setup

setup(
    name='flask-conditional',
    version='0.1',
    packages=[''],
    url='http://github.com/alfg/flask-conditional',
    license='MIT',
    author='Alfred Gutierrez',
    author_email='alf.g.jr@gmail.com',
    description='Conditional decorators for Flask routes',
    platforms='any',
    long_description=__doc__,
    py_modules=['flask_conditional'],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
