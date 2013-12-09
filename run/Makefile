SHELL := /bin/bash
### PATH
export PATH := .:${PATH}:/work/_upos_new/bin:.:${SRILM_PATH}

SEED=1

build: ngrams.txt
	nohup cat ngrams.txt | python build.py &

stem.lookup:
	cat celex/stemmer.out | awk '{if($3=="V" || $3=="xV")print $1,$2,$5;}' > stem.lookup

wsj.verb.scaled.sub.gz: wsj.lm.gz wsj.sub.gz celex.verbs
	subfilter.py --scale $^ $@

test-words.txt: test.set
	cat test.set | cut -f1-2 | tr '\t' '\n' | sort | uniq > $@

global-T%.ans: wsj.verb.scaled.sub.gz test-words.txt test_set.txt
	zcat $< | global.py test-words.txt test_set.txt $* > $@

%.plot:
	python evaluate.py $*.scaled.png -score_file scores/$*.scaled.* --title $*.scaled

clean:
	rm scores.dat

.SECONDARY:
