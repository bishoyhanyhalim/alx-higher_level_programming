#!/usr/bin/python3

if __name__ == "__main__":

	"""this print value of book"""

	import hidden_4

	moon = dir(hidden_4)

	for book in moon:
		if book[:2] != "__":
			print(book)
