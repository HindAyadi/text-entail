#! /usr/bin/python
# -*- coding: utf-8 -*-
import eval_metrics as metrics

def get_scores(fname):
    tset = []
    with open(fname) as src:
        return [l.strip().split() for l in src]

def main():
    metric = getattr(metrics,args.m)
    print metric(get_scores(args.score_file))




if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", choices=['ap0','ap1'])
    parser.add_argument("score_file")
    args = parser.parse_args()
    main()
