from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='islay.hardercaptcha',
      version=version,
      description='',
      long_description=open(os.path.join('src', 'islay', 'hardercaptcha', 'README.txt')).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      package_dir = {'':'src'},
      packages=find_packages('src', exclude=['ez_setup']),
      namespace_packages=['islay'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'WebOb',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
[paste.filter_factory]
captcha = islay.hardercaptcha.captcha:CaptchaFactory
      """,
      )
