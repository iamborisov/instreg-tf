#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from core.factory import FactoryIterator
from entity.institution.config.config import InstitutionConfig


class InstitutionConfigIterator(FactoryIterator):
    def __init__(self, config):
        assert isinstance(config, InstitutionConfig)

        super(InstitutionConfigIterator, self).__init__()

        self.__iter = iter(config.institutions)

    def __iter__(self):
        return self.__iter

    def __next__(self):
        return next(self.__iter)
