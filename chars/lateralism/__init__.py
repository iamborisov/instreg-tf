#! /usr/bin/env python
# -*- coding: utf-8 -*-

import tensorflow
import prompt_toolkit

u"""
    Характеристика "сторонность"
    2-ух сторонний
    Многосторонний
"""


def get_min_value():
    return 0.5


def get_max_value():
    return 0.8


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
    return float(prompt_toolkit.prompt(u"Латеральность. Двухсторонний (0.8) или Многосторонний (0.5): "))