text = 'aaaaaaaaabbbcdeee'
alphabet = []
weight = []
comb_weight = []
for x in text:
	if x in alphabet:
		weight[alphabet.index(x)][0] += 1

	else:
		alphabet.append(x)
		weight.append([1,str(x)])




print (alphabet)
print (weight)