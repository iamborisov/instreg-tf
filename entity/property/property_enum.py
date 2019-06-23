#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from entity.property.property import Property


class PropertyEnum(Property):
    values = []

    def normalize(self, value):
        assert isinstance(value, float)

        return 1.0

    def denormalize(self, value):
        assert isinstance(value, float)

        return 0.0

