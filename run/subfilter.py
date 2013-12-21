#!/usr/bin/env python
"""
# stemmer.pl outputs every wordform spelling in celex and each
# associated analysis with its lemma, suffix, and count.
print "$word $stem $pos $wfmor $frq $wf $lm";

print "$word[$i] $stem[$i] x$pos $wfmor $frq $wf $lm";
"""

from collections import OrderedDict
import gzip, math
from lm import LM

stem_lookup = {}

"""
def read_lookup():
    global stem_lookup
    d = {}
    with open(args.stemfile) as f:
        for l in f:
            fields = l.strip().split()
            v, stem, freq = fields[0], fields[1], int(fields[2])
            if not v in d:
                d[v] = (stem,freq)
            else:
                d[v] = max([d[v],(stem,freq)],key=lambda x:x[1])
    for v, t in d.iteritems():
        stem_lookup[v] = t[0]
"""
def read_lookup():
    global stem_lookup
    with open(args.stemfile) as f:
        for l in f:
            fields = l.strip().split()
            stem_lookup[fields[0]] = fields[1]

def get_filter_words(vfile):
    words = []
    with open(vfile) as f:
        words = [l.strip() for l in f]
    return set(words)

def main():
    read_lookup()
    words = get_filter_words(args.filter_words_file)
    if args.lm_file:
        lm = LM(args.lm_file)
    with gzip.GzipFile(args.sub_gz_file) as src, gzip.GzipFile(args.out_sub_gz_file, 'w') as out:
        for l in src:
            fields = l.strip().split()
            w = fields[0]
            if w in stem_lookup and stem_lookup[w] in words:
                vec = get_vec(fields)
                if args.lm_file:
                    scale(vec, lm)
                if args.stemfile:
                    vec = stem(vec)

                nfields = []
                if args.stemfile:
                    nfields.append(stem_lookup[w])
                else:
                    nfields.append(w)
                for w,p in vec.iteritems():
                    nfields.append(w)
                    nfields.append(str(math.log(p,10)))
                out.write('%s\n'%' '.join(nfields))


def get_vec(fields):
    vec = OrderedDict()
    for i in range(1,len(fields)-1,2):
        w, logp = fields[i], float(fields[i+1])
        p = math.pow(10,logp)
        vec[w] = p
    return vec

def scale(vec, lm):
    for w, p in vec.iteritems():
        vec[w] = p / lm.q[w]

def stem(vec):
    d = {}
    for w, p in vec.iteritems():
        if w in stem_lookup:
            w_lemma = stem_lookup[w]
            if not w_lemma in d:
                d[w_lemma] = 0
            d[w_lemma] += p
        else:
            d[w] = p
    return d

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('filter_words_file', help='consider only the words in file')
    parser.add_argument('sub_gz_file', help='sub.gz file to filter')
    parser.add_argument('out_sub_gz_file', help='sub.gz file to make output')
    parser.add_argument('--scale', dest='lm_file', help='scale words with unigram prob')
    parser.add_argument('--stemfile', help='stemfile')
    args = parser.parse_args()
    if args.lm_file or args.stemfile:
        main()
    else:
        print 'at least use --scale or --stem'
