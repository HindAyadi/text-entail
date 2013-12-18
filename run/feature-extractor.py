#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

"""
This module provides input data for Weka.
"""

import sys
from entail_utils import get_contexts_above_threshold, get_test_pairs
import gzip

if len(sys.argv) != 5:
    m = "Usage: {} test_words test_set threshold metric"
    print >> sys.stderr, m.format(sys.argv[0])
    exit(-1)

subs_file = gzip.open(sys.argv[1])
test_set = set(open(sys.argv[2]).read().split())
test_pairs = sys.argv[3]
THRESHOLD = float(sys.argv[4])

def print_features1_weka_format(data):
    print "@relation EntailmentFeatureSet1 "
    print "@attribute 'AintersectB' numeric"
    print "@attribute 'AdiffB' numeric"
    print "@attribute 'BdiffA' numeric"
    print "@attribute 'class' {'Yes', 'No'}"
    print "@data"
    print '\n'.join(data)

pairs = get_test_pairs(test_pairs)
words, total_line = get_contexts_above_threshold(test_set, subs_file, THRESHOLD)

data = []

def feature_set1():
    for w1, w2, tag in pairs:
        s1, s2 = words[w1], words[w2]
        num_inter = len(s1.intersection(s2))
        num_adiffb = len(s1.difference(s2))
        num_bdiffa = len(s2.difference(s1))
        sent = "{},{},{},'{}'".format(num_inter, num_adiffb, num_bdiffa, tag)
        data.append(sent)

    print_features1_weka_format(data)

feature_set1()
