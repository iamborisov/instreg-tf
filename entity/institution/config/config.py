#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from core.config import Config


class InstitutionConfig(Config):
    def __init__(self, data_source):
        super(InstitutionConfig, self).__init__(data_source)

        assert isinstance(self.institutions, list)
        for institution in self.institutions:
            assert 'id' in institution.keys()
            assert 'code' in institution.keys()
            assert 'name' in institution.keys()
            assert 'countries' in institution.keys()
            assert isinstance(institution['countries'], list)
