#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from core.factory import FactoryClassifier
from entity.property.property import Property


class PropertyConfigClassifier(FactoryClassifier):
    def __init__(self):
        super(PropertyConfigClassifier, self).__init__()

    def classify(self, item):
        return Property
