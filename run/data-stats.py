#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

"""

"""
import sys
import os
import numpy as np
from nlp_utils import fopen
#import matplotlib.pyplot as plt

input_file = sys.argv[1]
nbin = int(sys.argv[2]) # number of bins

def find_max_min():
    
    max_val = -1000
    min_val = 1000
    
    for line in fopen(input_file):
        line = line.split()
        probs = np.array([float(line[i+1]) \
                                    for i in xrange(1, len(line)-1, 2)])
        max_prob = probs.max()
        min_prob = probs.min()

        if max_val < max_prob:
            max_val = max_prob

        if min_val > min_prob:
            min_val = min_prob
    
    return max_val, min_val

def prepare_histogram_data():

    max_range, min_range = find_max_min() 
    print "{}\t{}\t{}".format(max_range, min_range, nbin) # max,min,#ofbins
    gcounts = np.zeros([1, nbin])
    for line in fopen(input_file):
        line = line.split()
        probs = np.array([float(line[i+1]) \
                                    for i in xrange(1, len(line)-1, 2)])
        counts, bins = np.histogram(probs, nbin, [min_range, max_range])
        gcounts += counts

    print gcounts.tolist()[0]
    print np.log(gcounts + 1).tolist()[0]
    print bins.tolist()

prepare_histogram_data()
