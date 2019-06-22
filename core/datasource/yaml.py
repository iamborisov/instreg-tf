#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import yaml

from core.datasource import DataSource


class YamlDataSource(DataSource):
    def __init__(self, source):
        super(YamlDataSource, self).__init__(yaml.load(source))
