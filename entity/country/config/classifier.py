#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from core.factory import FactoryClassifier
from entity.country.country import Country


class CountryConfigClassifier(FactoryClassifier):
    def __init__(self):
        super(CountryConfigClassifier, self).__init__()

    def classify(self, item):
        return Country
