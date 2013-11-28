#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
def main():
    res = {}
    for f in args.score_file:
        base = os.path.basename(f)
        sname = base.split('.')[2]
        scores = get_scores(f)
        total_yesc = sum([1 if t[2] == 'Yes' else 0 for t in scores])
        res[sname] = evalu(scores, total_yesc)
    plot(res)

def plot(results,title='unk'):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    colors = ['r','g','b','k','m','c']
    i = 0
    for sname, res in results.iteritems():
        plt.plot(res[0], res[1], '%s-'%colors[i], label=sname)
        i+=1

    plt.axis([0,1.01,0,1])
    plt.xticks([x/float(10) for x in range(0,11,1)])
    plt.yticks([y/float(10) for y in range(3,9,1)])
    plt.xlabel('recall')
    plt.ylabel('precision')
    plt.title(title)
    plt.legend()
    plt.savefig(args.plot_file)


def evalu(scores, total_yesc):
    recalls, precisions = [], []
    N = 1
    yesc = float(0)
    for l in scores:
        if l[2] == 'Yes':
            yesc += 1
        recall = yesc / float(total_yesc)
        precision = yesc / float(N)
        print recall, precision

        N += 1
        recalls.append(recall)
        precisions.append(precision)
    return (recalls, precisions)


def get_scores(fname):
    tset = []
    with open(fname) as src:
        for l in src:
            t = l.strip().split()
            tset.append(t)
    return tset



if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-score_file", nargs='+')
    parser.add_argument("plot_file")
    #parser.add_argument("--title")
    args = parser.parse_args()
    main()
