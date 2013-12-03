#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

"""

"""

import sys
from itertools import izip
import matplotlib.pyplot as plt
import numpy as np

lines = open(sys.argv[1]).readlines()
threshold = float(sys.argv[2])
count_type = int(sys.argv[3]) # 0 for raw counts, 1 for normalized counts, 2 for log counts

C = map(float, lines[count_type][1:-2].replace(",", "").split())
#B = map(float, lines[3][1:-2].replace(",", '').split())
B = np.array(lines[2][1:-2].replace(",", '').split()[:-1], dtype="float")

print len(C), B.shape
#print B

#threshold = 3
#C = [6,2,3,5,1,1,5,7,1,1,1,15]
#B = np.array(range(len(C)))
#plt.figure(num=None, figsize=(100, 12), dpi=80, facecolor='w', edgecolor='k')

width= 0.0007
#fig, ax = plt.subplots()
ax = plt.axes()
ax.bar(B, C, width, color='r')
ax.set_xticks(B+0.0007/2)
plt.xticks(rotation='vertical')
#plt.xticks(np.linspace(0,0.1, 501))
plt.xlabel("Bins")
plt.ylabel("Log Probabilities")
plt.title("Histogram on Whole Verb Dataset (Log, Oren Scaling)")
plt.savefig("dummy.png")
#plt.show()


#plt.axis = [0, 2, 0, 12]
#a = np.linspace(0, 0.009, 10).tolist() + np.linspace(0.01, 0.09, 10).tolist() + np.linspace(0.1, 1, 2).tolist()

#counts = []
#bins = []
#ct = 0
#for c, b in izip(C,B):
    #ct += c
    #if ct >= threshold:
        #counts.append(ct)
        #bins.append(b)
        #ct = 0

#if ct > 0:
    #counts.append(ct)
    #bins.append(b)
    #ct = 0

#print counts
#print bins

#bar_width= 0.005
#plt.axis = [0, 2, 0, 12]
#plt.xticks(np.linspace(0,2,41))
#plt.bar(bins, counts, bar_width)
#plt.show()

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
