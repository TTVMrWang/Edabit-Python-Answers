def replace_vowels(txt, ch):
	return ''.join([i if i not in 'aeoui' else ch for i in txt])
