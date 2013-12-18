#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

"""
This module calculates entailment scores for each pair in the test set globally.
Global approach considers all contexts (and their substitute vectors
for a,b pair that we find the score (not just those contexts where a or b occur).
"""

import sys
from entail_utils import get_eval_metric, get_contexts_above_threshold, get_test_pairs
import gzip
#import os

if len(sys.argv) != 6:
    m = "Usage: {} test_words test_set threshold metric"
    print >> sys.stderr, m.format(sys.argv[0])
    exit(-1)

subs_file = gzip.open(sys.argv[1])
test_set = set(open(sys.argv[2]).read().split())
test_pairs = sys.argv[3]
THRESHOLD = float(sys.argv[4])
metric_name = sys.argv[5]

def print_sorted_scores(scores):
    scores.sort(key=lambda x: x[-1], reverse=True)
    for s in scores:
        for e in s:
            print e,
        print

eval_metric = get_eval_metric(metric_name)
print >> sys.stderr, "Score metric is {}".format(eval_metric.func_name)
pairs = get_test_pairs(test_pairs)
words, total_line = get_contexts_above_threshold(test_set, subs_file, THRESHOLD)

scores = []
for w1, w2, tag in pairs:
    s1, s2 = words[w1], words[w2]
    scores.append((w1, w2, tag, eval_metric(s1, s2)))

print_sorted_scores(scores)
