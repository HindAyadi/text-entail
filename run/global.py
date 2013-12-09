#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

"""
This module calculates entailment scores for each pair in the test set globally.
Global approach considers all contexts (and their substitute vectors
for a,b pair that we find the score (not just those contexts where a or b occur).
"""

import sys
from collections import defaultdict as dd
#import os

test_set = set(open(sys.argv[1]).read().split())
test_pairs = sys.argv[2]
THRESHOLD = float(sys.argv[3])

def get_test_pairs():
    pairs = []
    for line in open(test_pairs):
        w1, w2, tag = line.split()
        pairs.append((w1, w2, tag))
    return pairs

def get_contexts_above_threshold(threshold=THRESHOLD):
    words = dd(set)
    for line_num, line in enumerate(sys.stdin):
        line = line.split()
        #tw = line[0]
        for i in xrange(1, len(line)-1, 2):
            word = line[i]
            if word in test_set:
                prob = float(line[i+1])
                if prob >= threshold:
                    words[word].add(line_num)
    return words, line_num + 1


pairs = get_test_pairs()
words, total_line = get_contexts_above_threshold()

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

def print_sorted_scores(scores):
    scores.sort(key=lambda x: x[-1], reverse=True)
    for s in scores:
        for e in s:
            print e,
        print

scores = []
for w1, w2, tag in pairs:
    c1, c2 = words[w1], words[w2]
    scores.append((w1, w2, tag, entail_score1(c1, c2)))
print_sorted_scores(scores)
