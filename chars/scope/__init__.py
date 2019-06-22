#! /usr/bin/env python
# -*- coding: utf-8 -*-

import tensorflow
import prompt_toolkit

u"""
    Характеристика "функциональное измерение"
    Военная
    Экономическая
    Социальная
"""


def get_min_value():
    return 0.1


def get_max_value():
    return 0.7


def normalize(value):
    if value < get_min_value():
        value = get_min_value()

    if value > get_max_value():
        value = get_max_value()

    delta = get_max_value() - get_min_value()

    value -= get_min_value()

    return value / delta


def build_node(value):
    return tensorflow.constant(float(value))


def prompt():
    return float(prompt_toolkit.prompt(u"Сфера деятельности. Экономический (0.7) или Военно-политический (0.1): "))