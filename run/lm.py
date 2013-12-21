import gzip
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
