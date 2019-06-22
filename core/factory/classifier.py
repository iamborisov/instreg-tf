#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from abc import ABCMeta, abstractmethod, abstractproperty


class Classifier(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def classify(self, item):
        """Get item class"""
