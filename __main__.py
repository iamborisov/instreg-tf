#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from core import *
from entity import *


def load_countries(filename):
    assert isinstance(filename, str)

    with open(filename, 'r') as ymlfile:
        return CountryFactory().create_dict(
            CountryConfigIterator(
                CountryConfig(
                    YamlDataSource(ymlfile)
                )
            ),
            'id'
        )


def load_institutions(filename):
    assert isinstance(filename, str)

    with open(filename, 'r') as ymlfile:
        return InstitutionFactory().create_dict(
            InstitutionConfigIterator(
                InstitutionConfig(
                    YamlDataSource(ymlfile)
                )
            ),
            'id'
        )


def load_properties(filename):
    assert isinstance(filename, str)

    with open(filename, 'r') as ymlfile:
        return PropertyFactory().create_dict(
            PropertyConfigIterator(
                PropertyConfig(
                    YamlDataSource(ymlfile)
                )
            ),
            'id'
        )


def main():
    countries = load_countries("./data/countries.yml")
    institutions = load_institutions("./data/institutions.yml")
    properties = load_properties("./data/properties.yml")
    print properties


if __name__ == "__main__":
    main()
