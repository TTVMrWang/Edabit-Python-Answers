def should_serve_drinks(age, on_break):
	if age >= 18 and on_break == False:
		return True
	else:
		return False
