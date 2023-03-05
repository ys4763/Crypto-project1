#!/usr/bin/env python3

if __name__ == '__main__':
	with open("plaintext_dictionary_test1.txt") as f:
		lines = list(line for line in (l.strip() for l in f) if line)
	for line in lines:
		if ord(line[0]) >= 97:
			new_freq = {}
			for i in line:
				if i in new_freq:
					new_freq[i] += 1
				else:
					new_freq[i] = 1
			freq_view = [(v,k) for k, v in new_freq.items()]
			freq_view.sort(reverse=True)
			for v, k in freq_view:
				print(k, v)
		else:
			print(line)
			
