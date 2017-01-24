========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
        | |scrutinizer| |codacy| |codeclimate|
    * - package
      - | |version| |downloads| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-nameless/badge/?style=flat
    :target: https://readthedocs.org/projects/python-nameless
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/ionelmc/python-nameless.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ionelmc/python-nameless

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/ionelmc/python-nameless?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ionelmc/python-nameless

.. |requires| image:: https://requires.io/github/ionelmc/python-nameless/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/ionelmc/python-nameless/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/ionelmc/python-nameless/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/ionelmc/python-nameless

.. |codecov| image:: https://codecov.io/github/ionelmc/python-nameless/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/ionelmc/python-nameless

.. |codacy| image:: https://img.shields.io/codacy/REPLACE_WITH_PROJECT_ID.svg?style=flat
    :target: https://www.codacy.com/app/ionelmc/python-nameless
    :alt: Codacy Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/ionelmc/python-nameless/badges/gpa.svg
   :target: https://codeclimate.com/github/ionelmc/python-nameless
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/nameless.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/nameless

.. |commits-since| image:: https://img.shields.io/github/commits-since/ionelmc/nameless/0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/ionelmc/nameless/compare/0.1.0...master

.. |downloads| image:: https://img.shields.io/pypi/dm/nameless.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/nameless

.. |wheel| image:: https://img.shields.io/pypi/wheel/nameless.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/nameless

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/nameless.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/nameless

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/nameless.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/nameless

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/ionelmc/python-nameless/master.svg?style=flat
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/ionelmc/python-nameless/


.. end-badges

An example package. Generated with https://github.com/ionelmc/cookiecutter-pylibrary

* Free software: BSD license

Installation
============

::

    pip install nameless

Documentation
=============

https://python-nameless.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
