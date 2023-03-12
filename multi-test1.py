#!/usr/bin/env python3
import random

# Implement multiple test1 with multiple index check

def bf(pt, ct, t):
	# Get the ascii number of first character in both strings
	p = ord(pt[0])
	c = ord(ct[0])
	
	# Calculate the amount of shifting
	# Which is the key value
	if c == 32:
		shift = 123 - p
	else:
		shift = (c - p) % 27
		
	# Set the pointer of the next character that we would like to compare
	# We move to next with the length of t, our suggested key length
	p_pointer = t
	c_pointer = t
	
	# We then compare the ascii number of next pair of plaintext and ciphertext 
	# If the key length is correct, the next plaintext character
	# should be shifted by the exact same amount as the previous one
	
	# Since there could be random inserted ciphertext at our suggested position
	# If we do not get a match, we move to the next ciphertext
	# As long as there are at least as many character left in ciphertext as in the plaintext
	# We can keep looking at next ciphertext characters for a match
	while p_pointer < len(pt):
		if len(ct) - c_pointer < len(pt) - p_pointer:
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

# We run through all the plaintext at zero index
# and all possible key length (from 1 to 24)
# For each plaintext and key length pair
# we parse it into bf(pt, ct, t) for possible matches
# for all characters at index 0, t, 2*t ...
def attack(pt, ct):
	for t in range(1, 25):
		for i in range(len(pt)):
			if bf(pt[i], ct, t):
				# We return the likely choice of plaintext
				return i + 1

# This function is for controlling which index we start with in plaintext
# Since as we increase the probability of random inserted characters,
# We are going to get coincidental matches, and we try to eliminate coincidences
# As many as possible

def indexing(plaintext, ciphertext):
	index = 0
	choices = []
	candidates = []
	for pt in plaintext:
		candidates.append(pt)
	ct = ciphertext
	while len(choices) != 1:
		# If the value of index != 1
		# This means we start to check the second set of characters
		# Therefore our plaintext should start from the second character
		# Therefore we slightly modify the input plaintext variable
		# as well as the ciphertext value for function attack()
		if index != 0:
			for i in range(len(candidates)):
				if i+1 in choices:
					candidates[i] = plaintext[i][index:]
			print(choices)
			choices = []
			ct = ciphertext[index:]
		choice = attack(candidates, ct)
		pointer = 1
		
		# if the first character of our ciphertext is a random character
		# we may not get a match
		# therefore, we try start from the next character in ciphertext
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
		
	# return when there is only 1 choice left
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
	
