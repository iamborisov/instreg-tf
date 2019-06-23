#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from abc import ABCMeta, abstractmethod, abstractproperty


class Property(object):
    __metaclass__ = ABCMeta

    id = None
    name = None
    default = None

    @abstractmethod
    def normalize(self, value):
        """Normalize"""

    @abstractmethod
    def denormalize(self, value):
        """Denormalize"""
