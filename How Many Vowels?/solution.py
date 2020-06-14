def count_vowels(txt):
  return sum([1 for x in txt.lower() if x in 'aeiou'])
