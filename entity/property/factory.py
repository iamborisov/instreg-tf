#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from core.factory import Factory
from entity.property.config import PropertyConfigClassifier


class PropertyFactory(Factory):
    def __init__(self):
        super(PropertyFactory, self).__init__(PropertyConfigClassifier())
