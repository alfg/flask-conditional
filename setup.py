"""
Flask-conditional
------------------
Conditional decorators for Flask routes.
"""
from setuptools import setup

setup(
    name='flask-conditional',
    version='0.1',
    url='http://github.com/alfg/flask-conditional',
    license='MIT',
    author='Alfred Gutierrez',
    author_email='alf.g.jr@gmail.com',
    description='Conditional decorators for Flask routes',
    platforms='any',
    py_modules=['flask_conditional'],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
