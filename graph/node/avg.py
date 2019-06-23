#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import tensorflow as tf

from graph.node.node import Node


class NodeAvg(Node):
    def __init__(self, input_nodes):
        assert isinstance(input_nodes, list)
        for node in input_nodes:
            assert isinstance(node, Node)

        graph_nodes = []
        for node in input_nodes:
            graph_nodes.append(node.get_graph_node())

        nodes_sum = tf.add_n(graph_nodes)
        nodes_count = tf.constant(float(len(graph_nodes)))
        self.__node = tf.divide(nodes_sum, nodes_count)

    def get_graph_node(self):
        return self.__node
