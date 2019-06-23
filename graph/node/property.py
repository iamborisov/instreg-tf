#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import tensorflow as tf

from graph.node.node import Node
from entity import Property


class NodeProperty(Node):
    def __init__(self, property):
        assert isinstance(property, Property)

        self.__property = property
        self.__node = tf.Variable(property.normalize(property.default), dtype=tf.float32)

    def get_graph_node(self):
        return self.__node
