#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

"""
This module calculates entailment scores for each pair in the test set globally.
Global approach considers all contexts (and their substitute vectors
for a,b pair that we find the score (not just those contexts where a or b occur).
"""

import sys
#import os

THRESHOLD = float(sys.argv[1])

for line in sys.stdin:
    line = line.split()
    tw = line[0]
    subs_probs = [[line[i], 10 ** float(line[i+1])] \
                                for i in xrange(1, len(line)-1, 2)]
