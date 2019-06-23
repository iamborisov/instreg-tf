#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from entity.property.property import Property


class PropertyFloat32(Property):
    min = None
    max = None

    def normalize(self, value):
        assert isinstance(value, float)

        value = value if value >= self.min else self.min
        value = value if value <= self.max else self.max
        value = value - self.min

        delta = self.max - self.min

        if delta == 0.0:
            return 1.0 if value == 0.0 else 0.0

        return value / delta

    def denormalize(self, value):
        assert isinstance(value, float)

        return 0.0
