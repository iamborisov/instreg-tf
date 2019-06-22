#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from core.factory import FactoryClassifier
from entity.institution.institution import Institution


class InstitutionConfigClassifier(FactoryClassifier):
    def __init__(self):
        super(InstitutionConfigClassifier, self).__init__()

    def classify(self, item):
        return Institution
