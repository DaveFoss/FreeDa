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

.. |docs| image:: https://readthedocs.org/projects/freeda/badge/?version=latest
    :target: https://freeda.readthedocs.io/en/latest/?badge=latest
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
