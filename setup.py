import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(name='kotti_twitter',
      version='0.3',
      description="Add twitter widgets to your Kotti site",
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: Repoze Public License",
        ],
      author='Daniel Nouri',
      author_email='daniel.nouri@gmail.com',
      url='http://pypi.python.org/pypi/kotti_twitter',
      keywords='twitter kotti cms pylons pyramid',
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=['Kotti'],
      tests_require=['nose', 'coverage'],
      )
