#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import tensorflow as tf


class Graph(object):
    def __init__(self):
        pass

    def run(self):
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            result = sess.run(self.endpoint)
            print(result)
