#!/usr/bin/env python3
import random

# Implement multiple test1 with multiple index check

def bf(pt, ct, t):
	# The first character in both strings
	p = ord(pt[0])
	c = ord(ct[0])
	if c == 32:
		shift = 123 - p
	else:
		shift = (c - p) % 27
	p_pointer = t
	c_pointer = t
	while p_pointer < len(pt):
		# print(p_pointer)
		if len(ct) - c_pointer < len(pt) - p_pointer:
			#print(p_pointer, c_pointer)
			return False
		cp = ord(ct[c_pointer])
		pp = ord(pt[p_pointer])
		if cp == 32:
			if shift == (123 - pp):
				p_pointer += t
				c_pointer += t
			elif shift == 0 and pp == 32:
				p_pointer += t
				c_pointer += t
			else:
				c_pointer += 1
		else:
			if ((cp - pp) % 27) == shift:
				p_pointer += t
				c_pointer += t
			elif pp == 32 and cp == (shift + 96):
				p_pointer += t
				c_pointer += t
			else:
				c_pointer += 1
	return True

def attack(pt, ct):
	for t in range(1, 25):
		for i in range(len(pt)):
			if bf(pt[i], ct, t):
				print(t)
				return i + 1


def indexing(plaintext, ciphertext):
	index = 0
	choices = []
	candidates = []
	for pt in plaintext:
		candidates.append(pt)
	ct = ciphertext
	while len(choices) != 1:
		if index != 0:
			for i in range(len(candidates)):
				if i+1 in choices:
					candidates[i] = plaintext[i][index:]
			print(choices)
			choices = []
			ct = ciphertext[index:]
		choice = attack(candidates, ct)
		pointer = 1
		while pointer <=len(ciphertext) - len(plaintext[0]):
			#print(pointer)
			if choice == None:
				choice = attack(candidates, ct[pointer:])
				pointer += 1
			else:
				if choice not in choices:
					choices.append(choice)
			pointer += 1
		index += 1
	return choices[0]

if __name__ == "__main__":
	
	# Get the ciphertext from stdin
	ct = input("Enter the ciphertext: ")
	
	# Get the plaintext candidates from dictionary_1
	plaintext = []
	with open("plaintext_dictionary_test1.txt", "r") as f:
		lines = list(line for line in (l.strip() for l in f) if line)
	for line in lines:
		if ord(line[0]) >= 97:
			plaintext.append(line)
		
	choice = indexing(plaintext, ct)
	
	print("My plaintext guess is: " + str(choice))
