#!/usr/bin/env python3
import random

if __name__ == '__main__':
	
	# Read in 5 (or more) plaintext options
	plaintext = []
	with open("plaintext_dictionary_test1.txt") as f:
		lines = list(line for line in (l.strip() for l in f) if line)
	for line in lines:
		if ord(line[0]) >= 97:
			plaintext.append(line)
	
	# Randonly choose one of them
	num = random.randint(0,len(plaintext)-1)
	m = plaintext[num]
	
	# Randomly determine the key as a list of integers range 0-26 (a-z+space)
	k = []
	klen = 5 # make it 5 first...
	#klen = random.randint(1, 24)
	for i in range(klen):
		k.append(random.randint(0,26))
	
	# encryption alg
	ct = ""
	ciphertext_pointer = 0
	message_pointer = 0
	num_rand_characters = 0
	prob_of_random_ciphertext = 0.05
	while ciphertext_pointer <= (len(m) + num_rand_characters - 1):
		coin_value = random.random()
		if prob_of_random_ciphertext <= coin_value <= 1:
			j = message_pointer % klen
			if ord(m[message_pointer]) == 32:
				prev = 0
			else:
				prev = ord(m[message_pointer]) - 96
			now = (prev + j) % 27
			if now == 0:
				ct += chr(32)
			else:
				ct += chr(96 + now)
			message_pointer += 1
		else:
			rand_char = random.randint(0, 26)
			if rand_char == 0:
				ct += chr(32)
			else:
				ct += chr(96 + rand_char)
			num_rand_characters += 1
		ciphertext_pointer += 1
	
	print(ct)
