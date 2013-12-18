#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

"""

"""

def jaccard_index(s1, s2):
    try:
        score = len(s1.intersection(s2)) / float(len(s1.union(s2)))
    except ZeroDivisionError:
        score = 0
    return score

def entail_score1(s1, s2):
    try:
        score = len(s1.intersection(s2)) / float(len(s1))
    except ZeroDivisionError:
        score = 0
    return score

def entail_score2(s1, s2):
    try:
        score = len(s2.intersection(s1)) / float(len(s2))
    except ZeroDivisionError:
        score = 0
    return score

def entail_score3(s1, s2):
    try:
        score = len(s2.difference(s1)) / float(len(s1.union(s2)))
    except ZeroDivisionError:
        score = 0
    return score
