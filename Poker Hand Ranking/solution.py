def poker_hand_ranking(deck):
	face = dict(zip('JKQA', range(11, 15)))
	vals = sorted(map(int, [face.get(x[0], x[:-1]) for x in deck]))
	straight = vals == list(range(min(vals), max(vals)+1)) 
	pairings = sorted(vals.count(x) for x in set(vals))
	
	if 4 in pairings:
		return "Four of a Kind"
	if pairings == [2, 3]:
		return "Full House"
	if 3 in pairings:
		return "Three of a Kind"
	if pairings == [1, 2, 2]:
		return "Two Pair"
	if 2 in pairings:
		return "Pair"
	
	if len(set(x[-1] for x in deck)) == 1:
		if straight and vals[0] == 10:
			return "Royal Flush"
		if straight:
			return "Straight Flush"
		return "Flush"
	
	if straight:
		return "Straight"
	
	return "High Card"
