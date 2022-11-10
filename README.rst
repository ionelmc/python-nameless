========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions| |requires|
        | |coveralls| |codecov|
        | |scrutinizer| |codacy| |codeclimate|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-nameless/badge/?style=flat
    :target: https://python-nameless.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/ionelmc/python-nameless/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/ionelmc/python-nameless/actions

.. |requires| image:: https://requires.io/github/ionelmc/python-nameless/requirements.svg?branch=main
    :alt: Requirements Status
    :target: https://requires.io/github/ionelmc/python-nameless/requirements/?branch=main

.. |coveralls| image:: https://coveralls.io/repos/ionelmc/python-nameless/badge.svg?branch=main&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/ionelmc/python-nameless

.. |codecov| image:: https://codecov.io/gh/ionelmc/python-nameless/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/ionelmc/python-nameless

.. |codacy| image:: https://img.shields.io/codacy/grade/862e7946eabb4112be6503a667381b71.svg
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

.. |commits-since| image:: https://img.shields.io/github/commits-since/ionelmc/python-nameless/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/ionelmc/python-nameless/compare/v0.1.0...main


.. |scrutinizer| image:: https://img.shields.io/scrutinizer/quality/g/ionelmc/python-nameless/main.svg
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

    pip install https://github.com/ionelmc/python-nameless/archive/main.zip


Documentation
=============


https://python-nameless.readthedocs.io/


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
