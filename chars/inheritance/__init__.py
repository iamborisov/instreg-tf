#! /usr/bin/env python
# -*- coding: utf-8 -*-

import tensorflow
import prompt_toolkit

u"""
    Характеристика "преемственность института"
    Имеет ли в своей основе другой институт
"""


def get_min_value():
    return 0.0


def get_max_value():
    return 1.0


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
    return float(prompt_toolkit.prompt(u"Преемственность института. Имеет ли в своей основе другой институт (Да - 1.0, нет - 0.0): "))