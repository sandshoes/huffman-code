
text = 'aaaaaaaaabbbcdeee'
alphabet = []
weight = []
comb_weight = []

for x in text:
	if x in alphabet:
		weight[alphabet.index(x)][0] += 1
		comb_weight[alphabet.index(x)][0] += 1

	else:
		alphabet.append(x)
		weight.append([1,str(x),''])
		comb_weight.append([1,str(x)])

comb_weight = sorted(comb_weight)

while len(comb_weight) > 1:

	for i in range(len(weight)):
		for k in comb_weight[0][1]:
			if k == weight[i][1]:
				weight[i][2] += '0'
		for k in comb_weight[1][1]:
			if k == weight[i][1]:
				weight[i][2] += '1'

	comb_weight[0][0] = comb_weight[0][0] + comb_weight[1][0]
	comb_weight[0][1] = comb_weight[0][1] + comb_weight[1][1]


	comb_weight.pop(1)
	comb_weight = sorted(comb_weight)

for i in range(len(weight)):
	weight[i].pop(0)
	weight[i][1] = weight[i][1][::-1]

conversion = ''
for i in text: 
	for k in range(len(weight)):
		if i == weight[k][0]:
			conversion += weight[k][1] 

