#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from abc import ABCMeta
from core.datasource import DataSource


class Config(object):
    __metaclass__ = ABCMeta

    def __init__(self, data_source):
        assert isinstance(data_source, DataSource)

        self.__data = data_source.data()

    def __getattr__(self, attribute):
        if attribute in self.__data:
            return self.__data[attribute]
        else:
            raise AttributeError, attribute

    def __getitem__(self, item):
        if item in self.__data:
            return self.__data[item]
        else:
            raise IndexError, item