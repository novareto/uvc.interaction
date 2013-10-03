# -*- coding: utf-8 -*-

from os.path import join
from setuptools import setup, find_packages


name = 'uvc.interaction'
version = '0.1'
readme = open('README.txt').read()
history = open(join('docs', 'HISTORY.txt')).read()

install_requires = [
    'setuptools',
    'zope.component',
    'zope.interface',
    'zope.security',
    ]

tests_require = [
    ]

setup(name=name,
      version=version,
      description='Security context components',
      long_description=readme[readme.find('\n\n'):] + '\n' + history,
      keywords='',
      author='',
      author_email='',
      url='',
      download_url='',
      license='ZPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['uvc'],
      include_package_data=True,
      platforms='Any',
      zip_safe=False,
      extras_require={'test': tests_require},
      install_requires=install_requires,
      tests_require=tests_require,
      classifiers=[
          'Programming Language :: Python',
          ],
      )
