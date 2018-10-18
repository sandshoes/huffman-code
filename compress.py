text = 'aaaaaaaaabbbcddddee'
alphabet = []
weight = []
code = []

for x in text:
	if x in alphabet:
		weight[alphabet.index(x)] += 1

	else:
		alphabet.append(x)
		weight.append(1)

while len(weight) > 2:
	y = min(weight) 
	if weight.index(y) < len(alphabet):
		if len(code)<2:
			code.append(alphabet[weight.index(y)])
		alphabet.pop(weight.index(y))
	weight.pop(weight.index(y))
  

	l = min(weight) 
	if weight.index(l) < len(alphabet):
		if len(code)<2:
			code.append(alphabet[weight.index(l)])
		alphabet.pop(weight.index(l))
	weight.pop(weight.index(l))

	weight.append(l+y)

print(code)


'''
print(alphabet[weight.index(y)])

'''
'''
print(alphabet)
print(weight)
'''




'''
function to create alphabet, code and shit
function to calculate huffman tree
rollo factorial
'''