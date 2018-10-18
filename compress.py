text = 'aaaaaaaaabbbccddddeee'
alphabet = []
weight = []
code = []
temp = []

for x in text:
	if x in alphabet:
		weight[alphabet.index(x)] += 1

	else:
		alphabet.append(x)
		weight.append(1)

while len(weight) > 1:
	y = min(weight) 
	if weight.index(y) < len(alphabet):
		temp.append(alphabet[weight.index(y)])
		alphabet.pop(weight.index(y))
	weight.pop(weight.index(y))
  

	l = min(weight) 
	if weight.index(l) < len(alphabet):
		temp.append(alphabet[weight.index(l)])
		alphabet.pop(weight.index(l))
	weight.pop(weight.index(l))

	weight.append(l+y)

	if len(code) == 0:
		code = temp
	elif len(temp) == 0:
		continue
	else:
		code = [code, temp]
	temp = []
print (code)

'''
Remaining steps:
Code a loop or function that codes in binary
'''


'''
Might be useful 
		if len(code)<2:
			code.append(alphabet[weight.index(y)])
	I erased this before
'''