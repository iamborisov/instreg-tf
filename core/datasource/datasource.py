#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from abc import ABCMeta, abstractmethod, abstractproperty


class DataSource(object):
    __metaclass__ = ABCMeta

    def __init__(self, data):
        self.__data = data

    def data(self):
        return self.__data
