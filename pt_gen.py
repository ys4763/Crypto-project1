#!/usr/bin/env python3
import random

if __name__ == '__main__':
	with open("plaintext_dictionary_test2.txt") as f:
		lines = list(line for line in (l.strip() for l in f) if line)
	lines = lines[1:]
	L = 600 # set it to 600 first
	pt = ""
	while len(pt) < L:
		add = random.randint(0, len(lines)-1)
		pt += lines[add]
		pt += " "
	print(pt[:600])
