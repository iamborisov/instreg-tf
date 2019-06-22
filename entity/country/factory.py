#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from core.factory import Factory
from entity.country import CountryConfigClassifier


class CountryFactory(Factory):
    def __init__(self):
        super(CountryFactory, self).__init__(CountryConfigClassifier())
