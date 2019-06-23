#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from entity.property.property import Property


class PropertyBool(Property):
    def normalize(self, value):
        assert isinstance(value, bool)

        return 1.0 if value else 0.0

    def denormalize(self, value):
        assert isinstance(value, float)

        return value != 0.0
