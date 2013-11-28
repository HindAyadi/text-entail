build: ngrams.txt
	nohup cat ngrams.txt | python build.py &

stem.lookup:
	cat celex/stemmer.out | awk '{if($3=="V" || $3=="xV")print $1,$2,$5;}' > stem.lookup

clean:
	rm scores.dat
