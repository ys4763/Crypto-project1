#!/usr/bin/env python3
import random
import time

# This will be a quite brute-force approach that I just want to try

def bf(pt, ct, t, index):
	# The first character in both strings
	p = ord(pt[index])
	c = ord(ct[index])
	if c == 32:
		shift = 123 - p
	else:
		shift = (c - p) % 27
	p_pointer = index + t
	c_pointer = index + t
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
	index = 0
	for t in range(1, 25):
		# index = 0
		for i in range(len(pt)):
			if bf(pt[i], ct, t, index):
				print(t)
				return i + 1
				# I would like to try the first few characters in plaintext
				# To check if this could be the possible key length
				# for this specific plaintext
				#if index < 3:
				#	index += 1
				#else:
				#	return i + 1
			
if __name__ == "__main__":
	
	# Get the ciphertext
	ct = input("Enter the ciphertext: ")
	
	# Get the plaintext candidates
	plaintext = []
	with open("plaintext_dictionary_test1.txt", "r") as f:
		lines = list(line for line in (l.strip() for l in f) if line)
	for line in lines:
		if ord(line[0]) >= 97:
			plaintext.append(line)
	
	pointer = 1
	choice = attack(plaintext, ct)
	while choice == None and pointer <= len(ct) - len(plaintext[0]) :
		choice = attack(plaintext, ct[pointer:])
		#print(pointer)
		pointer += 1
	
	print("My plaintext guess is: " + str(choice))
