#!/usr/bin/env python3
import random

def test1(ct):

	l = len(ct)
	prob = (l-600) / 600
	
	
	
	return random.randint(1,5)
	
if __name__ == "__main__":
	
	ct = input("Enter the ciphertext: ")
	choice = test1(ct)
	print("My plaintext guess is: " + choice)
