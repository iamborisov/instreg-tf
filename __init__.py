#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import tensorflow as tf

import chars.scope
import chars.commitment
import chars.lateralism
import chars.inheritance
import chars.inheritance_required
import chars.uniqueness
import chars.openness
import chars.advocacy
import chars.discrepancy


def build_probability(chars):
    """
        Посчитать конечную вероятность
    """
    char_sum = tf.add_n(chars)
    char_count = tf.constant(float(len(chars)))
    return tf.divide(char_sum, char_count)


# chars.commitment.test()

scope = chars.scope.prompt()
lateralism = chars.lateralism.prompt()
commitment = chars.commitment.prompt(scope, lateralism)

inheritance = chars.inheritance.prompt()
inheritance_required = chars.inheritance_required.prompt()
uniqueness = chars.uniqueness.prompt()
openness = chars.openness.prompt()
advocacy = chars.advocacy.prompt()
discrepancy = chars.discrepancy.prompt()

chars = [
    chars.scope.build_node(scope),
    chars.commitment.build_node(commitment),
    chars.inheritance.build_node(inheritance),
    chars.inheritance_required.build_node(inheritance_required),
    chars.uniqueness.build_node(uniqueness),
    chars.lateralism.build_node(lateralism),
    chars.openness.build_node(openness),
    chars.advocacy.build_node(advocacy),
    chars.discrepancy.build_node(discrepancy),
]

probability = build_probability(chars)

with tf.Session() as sess:
    result = sess.run(probability)
    print(result)
