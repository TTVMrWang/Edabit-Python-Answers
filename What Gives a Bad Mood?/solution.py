def greatest_impact(lst):
	mood = {'Weather': sum(i[1]/10 for i in lst)/len(lst),
			'Meals': sum(i[2]/3 for i in lst)/len(lst),
			'Sleep': sum(i[3]/10 for i in lst)/len(lst)}
	
	if len(set(mood.values())) == 1: return 'Nothing'
	return min(mood, key=lambda x: mood.get(x))
