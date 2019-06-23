#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from abc import ABCMeta, abstractmethod, abstractproperty


class Node(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_graph_node(self):
        """Get TensorFlow node"""
