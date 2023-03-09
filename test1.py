#!/usr/bin/env python3
import random

def delete_random(ct, diff):
	group_size = int((600 + diff) / diff) # delete 1 elements in each group
	for i in range(diff, 0, -1):
		ct = ct[:i * group_size] + ct[i * group_size + 1:]
	return ct
	
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
	sum_fq = 0
	for f in freqs:
		sum_fq += f
	avg = sum_fq / len(freqs)
	return avg
	
# compare the frequency of each plaintext and ciphertext
# doesn't matter what the key, just match the frequency
def attack(ct, plaintext):
	count = [0]*5
	for kl in range(1, 25):
		freq_ct = divide(ct, kl)
		print(kl)
		print(freq_ct)
		for i in range(5):
			freq_pt = divide(plaintext[i], kl)
			print(freq_pt)
			count[i] += abs(freq_ct-freq_pt)
		
	print(count)
	exit()
	
		
			
			
			
			
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
	
	# Randomly delete characters to make it of length 600
	ct = delete_random(ct, len(ct) - 600)
	choice = attack(ct, plaintext)
		
	
	
	
	print("My plaintext guess is: " + str(choice))
