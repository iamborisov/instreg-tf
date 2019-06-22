#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from core.factory.iterator import Iterator
from core.factory.classifier import Classifier


class Factory(object):
    def __init__(self, classifier):
        assert isinstance(classifier, Classifier)

        self.__classifier = classifier

    def create(self, data):
        inst = object.__new__(self.__classifier.classify(data))

        for k, v in data.iteritems():
            inst.__setattr__(k, v)

        return inst

    def create_list(self, iterator):
        assert isinstance(iterator, Iterator)

        result = []
        for item in iter(iterator):
            result.append(self.create(item))

        return result

    def create_dict(self, iterator, key):
        assert isinstance(iterator, Iterator)

        result = {}
        for item in iter(iterator):
            result[item[key]] = self.create(item)

        return result