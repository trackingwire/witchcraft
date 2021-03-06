#!/usr/bin/env python
from setuptools import setup

setup(
    name="witchcraft",
    version="0.2",
    description='',
    author='Peter Facka',
    author_email='pfacka@trackingwire.com',
    url='https://github.com/trackingwire/witchcraft',
    packages=[
        'witchcraft',
    ],
    zip_safe=False,	
    install_requires=[
	'psycopg2>=2.6.1',
	'SQLAlchemy>=1.0.6',
        'hy>=0.11.1',
        'pyparsing>=2.1.1'
    ],
    provides=['witchcraft (0.2)'],
    include_package_data=True,
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Environment :: Web Environment',
      'Intended Audience :: Developers',
      'Operating System :: Microsoft :: Windows',
      'Operating System :: MacOS :: MacOS X',
      'Operating System :: POSIX',
      'Programming Language :: Python :: 2.7',
      'License :: OSI Approved :: MIT License',
      ],
)
