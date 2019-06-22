#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from core.factory import FactoryIterator
from entity.country.config.config import CountryConfig


class CountryConfigIterator(FactoryIterator):
    def __init__(self, config):
        assert isinstance(config, CountryConfig)

        super(CountryConfigIterator, self).__init__()

        self.__iter = iter(config.countries)

    def __iter__(self):
        return self.__iter

    def __next__(self):
        return next(self.__iter)