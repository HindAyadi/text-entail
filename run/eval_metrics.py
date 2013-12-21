#! /usr/bin/python
# -*- coding: utf-8 -*-
def ap1(scores):
    precisions = []
    yesc, N = 0, 0
    for l in scores:
        N += 1
        if l[2] == 'Yes':
            yesc += 1
            precisions.append(yesc / float(N))

    return sum(precisions) / len(precisions)

def ap0(scores):
    scores.reverse()
    precisions = []
    yesc, N = 0, 0
    for l in scores:
        N += 1
        if l[2] == 'No':
            yesc += 1
            precisions.append(yesc / float(N))

    return sum(precisions) / len(precisions)


