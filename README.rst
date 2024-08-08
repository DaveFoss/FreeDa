========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - |github-actions| |coveralls| |codecov|
    * - package
      - |version| |wheel| |supported-versions| |supported-implementations| |commits-since|
.. |docs| image:: https://readthedocs.org/projects/FreeDa/badge/?style=flat
    :target: https://readthedocs.org/projects/FreeDa/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/DaveFoss/FreeDa/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/DaveFoss/FreeDa/actions

.. |coveralls| image:: https://coveralls.io/repos/github/DaveFoss/FreeDa/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://coveralls.io/github/DaveFoss/FreeDa?branch=main

.. |codecov| image:: https://codecov.io/gh/DaveFoss/FreeDa/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://app.codecov.io/github/DaveFoss/FreeDa

.. |version| image:: https://img.shields.io/pypi/v/freeda.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/freeda

.. |wheel| image:: https://img.shields.io/pypi/wheel/freeda.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/freeda

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/freeda.svg
    :alt: Supported versions
    :target: https://pypi.org/project/freeda

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/freeda.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/freeda

.. |commits-since| image:: https://img.shields.io/github/commits-since/DaveFoss/FreeDa/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/DaveFoss/FreeDa/compare/v0.0.0...main



.. end-badges

Short Discription

* Free software: MIT license

Installation
============

::

    pip install freeda

You can also install the in-development version with::

    pip install https://github.com/DaveFoss/FreeDa/archive/main.zip


Documentation
=============


https://freeda.readthedocs.io


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
