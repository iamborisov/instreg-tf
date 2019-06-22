#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from abc import ABCMeta, abstractmethod


class Iterator(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass
