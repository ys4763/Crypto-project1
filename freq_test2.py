#!/usr/bin/env python3

if __name__ == '__main__':
	with open("plaintext_dictionary_test2.txt") as f:
		lines = list(line for line in (l.strip() for l in f) if line)
	lines = lines[1:]
	new_freq = {}
	sum_of_chars = sum(len(line) for line in lines)
	for line in lines:
		for i in line:
			if i in new_freq:
				new_freq[i] += 1
			else:
				new_freq[i] = 1
	freq_view = [(v,k) for k, v in new_freq.items()]
	freq_view.sort(reverse=True)

	sum_of_freq = 0
	for v, k in freq_view:
		print(k, ":", v)
		sum_of_freq += (v / sum_of_chars) ** 2
	print(sum_of_freq)
			
