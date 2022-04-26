# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='progress_sa',
      version=version,
      description=u"Minimal SQLAlchemy dialect for Progress OpenEdge 11.",
      long_description="""\
      An SQLAlchemy dialect that can be used to read Progress OpenEdge 11
      databases over ODBC.
      """,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Topic :: Database :: Database Engines/Servers',
          ],
      keywords='sqlalchemy database dialect odbc',
      url='http://github.com/dominikpegler/progress_sa',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "SQLAlchemy >= 1.1.2",
      ],
      entry_points={
        'sqlalchemy.dialects': ['progress.pyodbc = progress_sa:base.dialect']
      }


         )



    #       entry_points = {
    #  'sqlalchemy.databases': ['progress = progress_sa:base.dialect',]}


    # """
    #   [sqlalchemy.dialects]
    #   progress = progress_sa:base.dialect
    #   """