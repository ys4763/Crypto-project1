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
	#stat.sort(reverse=True)
	#print(stat)
	sum = 0
	for v, k in stat:
		sum += (v/len(string)) ** 2
	#print(sq_sum)
	return sum

# divide the list by key length and get frequencies of each substring
def divide(msg, l):
	divide = [""] * l # msg divided into l groups
	freqs = []
	for i in range(l):
		pointer = i
		#print(i)
		divide[i] += msg[i]
		while (pointer + l) < len(msg):
			pointer += l
			divide[i] += msg[pointer]
	return divide

def avg_ic(segments):
    # calculate the IC of each segment
    ics = []
    for segment in segments:
        segment_counts = {c: segment.count(c) for c in set(segment)}
        segment_length = len(segment)
        segment_ic = sum(count*(count-1) for count in segment_counts.values())/(segment_length*(segment_length-1))
        ics.append(segment_ic)
    
    # calculate the average IC
    avg_ic = sum(ics)/len(ics)
    
    return avg_ic

			
def delete_random(ct, diff):
	ct_list = []
	for k in range(1000):
		temp = ct
		list_of_numbers = list(range(0, 600 + diff))
		for i in range(diff):
			r = random.choice(list_of_numbers)
			temp = temp[:r] + '-' + temp[r + 1:]
			list_of_numbers.remove(r)
		
		temp = temp.replace("-", "")
		ct_list.append(temp)

	return ct_list

def guess_key_length(ct_list):
    best_length = 0
    best_ci = 0
    record = {}
    for ct in ct_list:
        ci_list = []
        for kl in range(1, 25):
            ct_dvd = divide(ct, kl)
            ci = avg_ic(ct_dvd)
            ci_list.append(ci)
            if ci > best_ci:
                best_ci = ci
                best_length = kl
        sorted_indices = sorted(range(len(ci_list)), key=lambda i: ci_list[i], reverse=True)
        #print(sorted_indices)
        top3 = sorted_indices[:3]
        for i in range(3):
            if top3[i]+1 in record:
                record[top3[i] + 1] += i + 1 
            else:
                record[top3[i] + 1] = i + 1
    #list = [(v,k) for k, v in record.items()]
    record = {k: v for k, v in sorted(record.items(), key=lambda item: item[1], reverse=True)}
    print(record)
    print(best_length, best_ci)
            # sum_freq = 0
            # for c in ct_dvd:
            #     sum_freq += freq(c)
            # print(kl, sum_freq / len(ct_dvd))


if __name__ == "__main__":
	start_time = time.time()
	ct = input("Enter the ciphertext: ")

	# Attack
	# first guess the key length
	#ct_600 = [ct]
	diff = len(ct) - 600
	if diff == 0:
		ct_600 = [ct]
	else:
		ct_600 = delete_random(ct, diff)
	#print(ct_600)

	kl = guess_key_length(ct_600)
	#comp = attack(ct_600)
	print("--- %s seconds ---" % (time.time() - start_time))
	#print("My guess is: " + comp)