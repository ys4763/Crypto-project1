#!/usr/bin/env python3
import random

# get the frequency of characters and then sort it into a list of tuples
# in the format of (freq, character)
# return the sqr sum of freq of the string
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
	divide = [""] * l # msg divided into l groups
	freqs = []
	for i in range(l):
		pointer = i
		divide[i] += msg[i]
		while (pointer + l) < len(msg):
			pointer += l
			divide[i] += msg[pointer]
	for d in divide:
		freqs.append(freq(d))
	return freqs # l groups of freq
	
# calculate the differences between square sums of frequency of each plaintext and ciphertext
# find the smallest difference
# doesn't matter what the key, just match the frequency
def attack(ct, plaintext):
	min_diff = 100 # initiate with a big number
	pt_guess = ""
	k = 0
	for kl in range(1, 25):
		for pt in plaintext:
            # get the square sum of ct & pt in ley length kl
			sqr_sum_ct = divide(ct, kl)
			sqr_sum_pt = divide(pt, kl)
			#print(sqr_sum_ct)
			#print(sqr_sum_pt)
			diff_sum = 0
			for i in range(kl):
				diff_sum += abs(sqr_sum_ct[i] - sqr_sum_pt[i])
			diff = diff_sum / kl
			print(kl, diff_sum, diff)
			if diff < min_diff:
				min_diff = diff
				pt_guess = pt
				k = kl
	print(min_diff, k)
	return pt_guess
	
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
			
def delete_random(ct, diff):
    group_size = int((600 + diff) / diff) # delete 1 elements in each group
    for i in range(diff, 0, -1):
        ct = ct[:i * group_size] + ct[i * group_size + 1:]
    return ct


if __name__ == "__main__":
	ct = input("Enter the ciphertext: ")
#	key = []
#	for i in range(1,25):
#		key.append(attack(ct, i))
		
	plaintext = []
	with open("plaintext_dictionary_test1.txt", "r") as f:
		lines = list(line for line in (l.strip() for l in f) if line)
	for line in lines:
		if ord(line[0]) >= 97:
			plaintext.append(line)

	# Attack
	# test by each key length
	diff = len(ct) - 600
	ct_600 = delete_random(ct, diff)
	#print(len(ct), len(ct_600))
	print(ct_600)

	comp = attack(ct_600, plaintext)
	print("My guess is: " + comp)