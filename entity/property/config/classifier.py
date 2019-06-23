#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from core.factory import FactoryClassifier
from entity.property.property_float32 import PropertyFloat32
from entity.property.property_bool import PropertyBool
from entity.property.property_enum import PropertyEnum


class PropertyConfigClassifier(FactoryClassifier):
    def __init__(self):
        super(PropertyConfigClassifier, self).__init__()

    def classify(self, item):
        type_name = str(item['type']).lower()

        if type_name == 'enum':
            return PropertyEnum

        if type_name == 'bool':
            return PropertyBool

        if type_name == 'float32':
            return PropertyFloat32

        else:
            raise RuntimeError, "Unknown type"

