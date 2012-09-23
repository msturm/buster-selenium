from setuptools import setup, find_packages
import os

setup(name='buster-selenium',
      version='0.1',
      description="Manage buster.js slave browsers using selenium.",
      long_description=(
          open(os.path.join(os.path.dirname(__file__),
                            "README.rst")).read() + '\n\n' +
          open(os.path.join("CHANGES.rst")).read()),
      # Get more strings from
      # http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='buster selenium js javascript ecmascript',
      author='Ross Patterson',
      author_email='me@rpatterson.net',
      url='http://github.com/plone/buster-selenium',
      license='GPL',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      setup_requires=['setuptools-git'],
      install_requires=['selenium'],
      extras_require={'layer': ['zope.testrunner'],
                      'testrunner': ['zope.testrunner']},
      entry_points={'console_scripts': [
                    "testrunner = buster_selenium.runner:run"]},
      )
