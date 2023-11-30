#!/usr/bin/python3

if __name__ == "__main__":
	"""now this is print collection of value"""

	import sys

	collection = 0
	for i in range(len(sys.argv) - 1):
		collection += int(sys.argv[i + 1])

	print("{}".format(collection))
