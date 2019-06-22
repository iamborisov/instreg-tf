#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from core.factory import FactoryIterator
from entity.property.config.config import PropertyConfig


class PropertyConfigIterator(FactoryIterator):
    def __init__(self, config):
        assert isinstance(config, PropertyConfig)

        super(PropertyConfigIterator, self).__init__()

        self.__iter = iter(config.properties)

    def __iter__(self):
        return self.__iter

    def __next__(self):
        return next(self.__iter)
