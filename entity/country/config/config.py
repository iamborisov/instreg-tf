#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from core.config import Config


class CountryConfig(Config):
    def __init__(self, data_source):
        super(CountryConfig, self).__init__(data_source)

        assert isinstance(self.countries, list)
        for country in self.countries:
            assert 'id' in country.keys()
            assert 'code' in country.keys()
            assert 'name' in country.keys()
