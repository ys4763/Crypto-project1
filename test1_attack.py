#!/usr/bin/env python3
import random
import time
import numpy as np

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
	freq_list = []
	for v, k in stat:
		freq_list.append(v/len(string)) #** 2
	#print(sq_sum)
	return freq_list

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
	return divide


def guess(ct, pt, kl):
    ct_dvd = divide(ct, kl)
    pt_dvd = divide(pt, kl)
    sum = 0
    for c, p in zip(ct_dvd, pt_dvd):
        freq_c = freq(c)
        freq_p = freq(p)
        diff_sum = 0
        for i in range(max(len(freq_c), len(freq_p))):
            if i < len(freq_c) and i < len(freq_p):
                diff_sum += (freq_c[i] - freq_p[i])** 2
            elif i >= len(freq_c):
                diff_sum += freq_p[i] ** 2
            else:
                diff_sum += freq_c[i] ** 2
            sum += diff_sum / max(len(freq_c), len(freq_p))
    #print(sum/kl)
    return sum / kl


# calculate the differences between square sums of frequency of each plaintext and ciphertext
# find the smallest difference
# doesn't matter what the key, just match the frequency
def attack(ct_list, plaintext):
	pt_guess = ""
	k = 0
	record_sum = [[0 for i in range(24)] for j in range(5)]
	for ct in ct_list:
		min_diff = 100
		for i in range(5):
			#print("plaintext " + str(i))
			for kl in range(1, 25):
				diff = guess(ct, plaintext[i], kl)
				record_sum[i][kl - 1] += diff
				#if diff < min_diff:
				#	min_diff = diff
				#	pt_num = i
				#	k = kl
		#record[pt_num] += 1
	record_sum = np.array(record_sum)
	for i in range(24):
		print(i + 1, record_sum[:, i])
	#print(k)p
	return
	
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
	ct_list = []
	for k in range(500):
		temp = ct
		list_of_numbers = list(range(0, 600 + diff))
		for i in range(diff):
			r = random.choice(list_of_numbers)
			temp = temp[:r] + '-' + temp[r + 1:]
			list_of_numbers.remove(r)
		
		temp = temp.replace("-", "")
		ct_list.append(temp)

	return ct_list


if __name__ == "__main__":
	start_time = time.time()
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
	if diff == 0:
		ct_600 = [ct]
	else:
		ct_600 = delete_random(ct, diff)
	#print(ct_600)

	comp = attack(ct_600, plaintext)
	print("--- %s seconds ---" % (time.time() - start_time))
	#print("My guess is: " + comp)