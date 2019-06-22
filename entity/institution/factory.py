#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from core.factory import Factory
from entity.institution.config import InstitutionConfigClassifier


class InstitutionFactory(Factory):
    def __init__(self):
        super(InstitutionFactory, self).__init__(InstitutionConfigClassifier())
