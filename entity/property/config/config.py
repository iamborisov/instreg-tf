#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from core.config import Config


class PropertyConfig(Config):
    def __init__(self, data_source):
        super(PropertyConfig, self).__init__(data_source)

        assert isinstance(self.properties, list)
        for property in self.properties:
            assert 'id' in property.keys()
            assert 'name' in property.keys()
