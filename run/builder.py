
"""
# stemmer.pl outputs every wordform spelling in celex and each
# associated analysis with its lemma, suffix, and count.
print "$word $stem $pos $wfmor $frq $wf $lm";

print "$word[$i] $stem[$i] x$pos $wfmor $frq $wf $lm";
"""

from collections import Counter
import gzip

stem_lookup = {}

def main():
    import subvector
    builder = SubsVectorBuilder()
    vectors = builder.build()
    subvector.dump(vectors, args.vec_file)


class LM:
    def __init__(self, lm_file):
        self.q = {}
        with gzip.GzipFile(lm_file) as src:
            for l in src:
                if l.strip() == '\\1-grams:':
                    break
            for l in src:
                if not l.strip():
                    break
                fields = l.strip().split()
                logp, w = float(fields[0]), fields[1]
                self.q[w] = pow(10,logp)

class SubsVectorBuilder:

    def __init__(self):
        self.verbs = get_verbs()

    def get_vector(self,fields):
        vec = {}
        for i in range(1,len(fields),2):
            w,logp = fields[i], float(fields[i+1])
            if w in vec:
                vec[w] += pow(10,logp)
            else:
                vec[w] = pow(10,logp)
        return vec

    def build(self):
        wvectors = {}
        with open('wsj.verb.sub') as src:
            for l in src:
                fields = l.strip().split()
                v = fields[0]
                s_vec = self.max_normalize(self.get_vector(fields))
                self.increment(wvectors, v, s_vec, 1)
        vectors = self.average(wvectors)
        for w, vec in vectors.iteritems():
            vectors[w] = self.max_normalize(self.truncate(vec))
        return vectors

    def truncate(self, vec, n=100):
        v ={}
        items = sorted(vec.iteritems(),key=lambda x:x[1],reverse=True)[:n]
        for w, p in items:
            v[w] = p
        return v


    def max_normalize(self, vec):
        if len(vec) == 0:
            return vec
        v = {}
        m = float(max(vec.iteritems(), key=lambda x:x[1])[1])

        for w, p in vec.iteritems():
            v[w] = p / m
        return v


    def normalize(self,vec):
        v = {}
        total = float(0)
        for p in vec.values():
            total += p
        for w, p in vec.iteritems():
            v[w] = p / total
        return v


    def average(self, wvectors):
        vectors = {}
        for v, val in wvectors.iteritems():
            vectors[v] = {}
            cvec = val[0]
            total = val[1]
            for w, p in cvec.iteritems():
                vectors[v][w] = p/total
        return vectors

    def increment(self, wvectors, v, vec, n):
        if not wvectors.has_key(v):
            wvectors[v] = [{},0]

        wvec = wvectors[v][0]
        for w, p in vec.iteritems():
            if wvec.has_key(w):
                wvec[w] += p*n
            else:
                wvec[w] = p*n
        wvectors[v][1] += n

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('vec_file', help='vec_file to make output')
    args = parser.parse_args()
    main()
