#!/usr/bin/env python3
import random

# get the frequency of characters and then sort it into a list of tuples
# in the format of (freq, character)
def freq(string):
	dic = {}
	for s in string:
		if s in dic:
			dic[s] += 1
		else:
			dic[s] = 1
	stat = [(v,k) for k, v in dic.items()]
	stat.sort(reverse=True)
	#print(stat)
	sq_sum = 0
	for v, k in stat:
		sq_sum += (v/len(string)) ** 2
	#print(sq_sum)
	return sq_sum

# divide the list by key length and get frequencies of each substring
def divide(msg, l):
	divide = [""] * l
	freqs = []
	for i in range(l):
		pointer = i
		divide[i] += msg[i]
		while (pointer + l) < len(msg):
			pointer += l
			divide[i] += msg[pointer]
	for d in divide:
		freqs.append(freq(d))
	return freqs
	
# compare the frequency of each plaintext and ciphertext
# doesn't matter what the key, just match the frequency
def attack(ct, pt, kl):
	key = [None] * kl
	freq_ct = divide(ct, kl)
	freq_pt = divide(pt, kl)
	print(kl)
	print(freq_ct)
	print(freq_pt)
	for i in range(kl):
		if freq_ct[i] == freq_pt[i]:
			continue
		else:
			return ""
	return pt
	
# the normal encryption for vigenere algorithm
def encrypt(m, k):
 	
 	klen = len(k)
 	# encryption alg
 	ct = ""
 	pointer = 0
 	while pointer <= (len(m) - 1):
 		j = pointer % klen
 		if ord(m[pointer]) == 32:
 			prev = 0
 		else:
 			prev = ord(m[pointer]) - 96
 		now = (prev + k[j]) % 27
 		if now == 0:
 			ct += chr(32)
 		else:
 			ct += chr(96 + now)
 		pointer += 1
 	return ct
			

if __name__ == "__main__":
#	ct = input("Enter the ciphertext: ")
#	key = []
#	for i in range(1,25):
#		key.append(attack(ct, i))
		
	plaintext = []
	with open("plaintext_dictionary_test1.txt") as f:
		lines = list(line for line in (l.strip() for l in f) if line)
	for line in lines:
		if ord(line[0]) >= 97:
			plaintext.append(line)
	
	# Randonly choose one of them
	num = random.randint(0,len(plaintext)-1)
	m = plaintext[num]

	# Randomly generate key
	k = []
	klen = random.randint(1, 24)
	for i in range(klen):
		k.append(random.randint(0,26))
		
	# Encrypt message with regular vigenere cipher
	ct = encrypt(m, k)
	print(len(k), k)
	print(num, m)
	print(ct)
	
	# Attack
	# test by each key length
	for kl in range(1, 25):
		# compare the ciphertext with each plaintext option
		# under the certain key length guess
		for pt in plaintext:
		#pt = plaintext[0]
			comp = attack(ct, pt, kl)
			if comp == "":
				continue
			else:
				print(comp)
				exit()
			
		
	
