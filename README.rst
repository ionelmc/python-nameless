========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
        | |landscape| |scrutinizer| |codacy| |codeclimate|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |travis| image:: https://api.travis-ci.org/ionelmc/python-nameless.svg?branch=master
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

.. |codecov| image:: https://codecov.io/gh/ionelmc/python-nameless/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/ionelmc/python-nameless

.. |landscape| image:: https://landscape.io/github/ionelmc/python-nameless/master/landscape.svg?style=flat
    :target: https://landscape.io/github/ionelmc/python-nameless/master
    :alt: Code Quality Status

.. |codacy| image:: https://img.shields.io/codacy/grade/inf.svg
    :target: https://www.codacy.com/app/ionelmc/python-nameless
    :alt: Codacy Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/ionelmc/python-nameless/badges/gpa.svg
   :target: https://codeclimate.com/github/ionelmc/python-nameless
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/nameless.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/nameless

.. |wheel| image:: https://img.shields.io/pypi/wheel/nameless.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/nameless

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/nameless.svg
    :alt: Supported versions
    :target: https://pypi.org/project/nameless

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/nameless.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/nameless

.. |commits-since| image:: https://img.shields.io/github/commits-since/ionelmc/python-nameless/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/ionelmc/python-nameless/compare/v0.0.0...master


.. |scrutinizer| image:: https://img.shields.io/scrutinizer/quality/g/ionelmc/python-nameless/master.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/ionelmc/python-nameless/


.. end-badges

An example package. Generated with cookiecutter-pylibrary.

* Free software: BSD 2-Clause License

Installation
============

::

    pip install nameless

You can also install the in-development version with::

    pip install https://github.com/ionelmc/python-nameless/archive/master.zip


Documentation
=============


To use the project:

.. code-block:: python

    import nameless
    nameless.longest()


Development
===========

To run all the tests run::

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
