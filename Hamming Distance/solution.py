def hamming_distance(txt1, txt2):
	diffs = 0
	for ch1, ch2 in zip(txt1, txt2):
		if ch1 != ch2:
			diffs += 1
	return diffs
