#! /usr/bin/env python
# -*- coding: utf-8 -*-

import tensorflow
import prompt_toolkit

import chars.hegemony

u"""
    Характеристика "уникальность института"
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
    return chars.hegemony.build_node(value)  # + .... + .... + ....


def prompt():
    return chars.hegemony.prompt()
    # return float(prompt_toolkit.prompt(u"Уникальность института (Да - 1.0, нет - 0.0): "))