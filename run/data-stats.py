#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

"""

"""
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

nbin = int(sys.argv[1]) # number of bins

min_range = 0
max_range = 1

gcounts = np.zeros([1,nbin])
for line in sys.stdin:
    line = line.split()
    tw = line[0]
    probs = np.array([10**float(line[i+1]) \
                                for i in xrange(1, len(line)-1, 2)])
    probs = probs / probs.sum()
    counts, bin_range = np.histogram(probs, nbin, [min_range, max_range])
    gcounts += counts

print gcounts.tolist()
print bin_range
plt.plot([gcounts, bin_range])
plt.savefig("dummy.png")
