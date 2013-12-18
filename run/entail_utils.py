#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

"""
Some utility functions for entailment project
"""
from collections import defaultdict as dd
from metrics import *

def get_eval_metric(metric_name):
    if metric_name == "jaccard":
        return jaccard_index
    elif metric_name == "1":
        return entail_score1
    elif metric_name == "2":
        return entail_score2
    elif metric_name == "3":
        return entail_score3

def get_test_pairs(test_pairs):
    pairs = []
    for line in open(test_pairs):
        w1, w2, tag = line.split()
        pairs.append((w1, w2, tag))
    return pairs

def get_contexts_above_threshold(test_set, subs_file, threshold):
    words = dd(set)
    for line_num, line in enumerate(subs_file):
        line = line.split()
        #tw = line[0]
        for i in xrange(1, len(line)-1, 2):
            word = line[i]
            if word in test_set:
                prob = float(line[i+1])
                if prob >= threshold:
                    words[word].add(line_num)
    return words, line_num + 1
