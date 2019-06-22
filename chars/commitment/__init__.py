#! /usr/bin/env python
# -*- coding: utf-8 -*-

import tensorflow
import prompt_toolkit
import chars.scope
import chars.lateralism

u"""
    Характеристика "степень обязательства"
    Рекомендательная
    Обязательная
"""


def get_min_value():
    return 0.1


def get_max_value():
    return 0.6


def denormalize(value):
    if value < 0:
        value = 0
    if value > 1:
        value = 1

    delta = get_max_value() - get_min_value()

    return float(delta * value + get_min_value())


def get_recommended_value(scope_value, lateralism_value):
    scope_value = chars.scope.normalize(scope_value)
    lateralism_value = chars.lateralism.normalize(lateralism_value)
    return denormalize(scope_value*lateralism_value)


def get_obligatory_value(lateralism_value):
    lateralism_value = chars.lateralism.normalize(lateralism_value)
    return denormalize(lateralism_value)


def build_node(value):
    return tensorflow.constant(float(value))


def prompt(scope_value, lateralism_value):
    recommended = get_recommended_value(scope_value, lateralism_value)
    obligatory = get_obligatory_value(lateralism_value)

    # scope == 0.7
    #     lateralism == 0.8
    #         recommended = 0.4
    #         obligatory = 0.6
    #     lateralism == 0.5
    #         recommended = 0.3
    #         obligatory = 0.5
    # scope == 0.1
    #     lateralism == 0.8
    #         recommended = 0.4
    #         obligatory = 0.2
    #     lateralism == 0.5
    #         recommended = 0.3
    #         obligatory = 0.1
    return float(prompt_toolkit.prompt(u"Степень обязательства. Рекомендательная ({}) или Обязывающая ({}): ".format(recommended, obligatory) ))


def test():
    data = [
        [[0.7, 0.8], [0.4, 0.6]],
        [[0.7, 0.5], [0.3, 0.5]],
        [[0.1, 0.8], [0.4, 0.2]],
        [[0.1, 0.5], [0.3, 0.1]],
    ]

    for tc in data:
        print(u"scope = {}, later = {}: rec = {} (exp: {}), obl = {} (exp: {})".format(tc[0][0], tc[0][1], get_recommended_value(tc[0][0], tc[0][1]), tc[1][0], get_obligatory_value(tc[0][1]), tc[1][1]))
