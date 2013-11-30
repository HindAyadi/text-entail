#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

"""

"""

import sys
from itertools import izip
import matplotlib.pyplot as plt

#lines = open(sys.argv[1]).readlines()
#threshold = sys.argv[2]
#count_type = int(sys.argv[3]) # 0 for raw counts, 1 for normalized counts, 2 for log counts

#C = map(float, lines[count_type][1:-1].split())
#B = map(float, lines[3][1:-1].split())

threshold = 3
C = [6,2,3,5,1,1,5,7,1,1,1,15]
B = range(len(C))

print C
print B

counts = []
bins = []
ct = 0
for c, b in izip(C,B):
    ct += c
    if ct >= threshold:
        counts.append(ct)
        bins.append(b)
        ct = 0

print counts
print bins

plt.bar(bins, counts)
plt.show()

# Method 1; threshold each count individually.
#for c, b in izip(C,B):
    #if c >= threshold:
        #if ct == 0:
            #counts.append(c)
            #bins.append(b)
        #else:
            #counts.append(ct)
            #bins.append(bt)
            #counts.append(c)
            #bins.append(b)
            #ct = 0
            #bt = 0
    #else:
        #ct += c
        #bt = b
