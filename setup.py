from setuptools import setup

import runipy

setup(name = 'runipy',
    version = runipy.__version__,
    description = 'Run IPython notebooks from the command line',
    url = 'https://github.com/paulgb/runipy',
    author = 'Paul Butler',
    author_email = 'paulgb@gmail.com',
    packages = ['runipy'],
    entry_points = {
        'console_scripts': [
            'runipy = runipy.main:main'
        ]
    },
)