========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |github-actions| |codecov|
    * - package
      - |version| |wheel| |supported-versions| |supported-implementations| |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-nameless/badge/?style=flat
    :target: https://readthedocs.org/projects/python-nameless/
    :alt: Documentation Status
.. |github-actions| image:: https://github.com/ionelmc/python-nameless/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/ionelmc/python-nameless/actions
.. |codecov| image:: https://codecov.io/gh/ionelmc/python-nameless/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://app.codecov.io/github/ionelmc/python-nameless
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
    :target: https://github.com/ionelmc/python-nameless/compare/v0.0.0...main

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
