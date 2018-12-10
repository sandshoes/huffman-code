alphabet = {}
weight = {}

text = open('quijote.txt','r', encoding = 'utf-8')
for line in text:
	for x in line:
		if x in alphabet:
			weight[x] +=1
		else:
			alphabet[x] = ''
			weight[x] = 1

while len(weight) > 1:
	a = min(weight, key=weight.get)
	v1 = weight[a]
	del weight[a]
	for i in a:
		alphabet[i] = '0' + alphabet[i]
	b = min(weight, key=weight.get)
	v2 = weight[b]
	del weight[b]
	for y in b:
		alphabet[y] = '1' + alphabet[y]
	weight[a+b] = v1 + v2
conversion = ''
text.seek(0)
for line in text:
	for i in line:
		if i in alphabet:
			conversion += alphabet[i]


extra_padding = 8 - len(conversion) % 8
for i in range(extra_padding):
	conversion += "0"

padded_info = "{0:08b}".format(extra_padding)
conversion = padded_info + conversion

byte_array = bytearray()
for i in range(0, len(conversion), 8):
    byte_array.append(int(conversion[i:i + 8], 2))

file = open('compression.txt','wb')
for w in sorted(alphabet, key=alphabet.get, reverse=True):
	string = bytes(w + alphabet[w]+'\n', encoding= 'utf-8')
	file.write(string)
file.write(b'th\n')
file.write(bytes(byte_array))
file.close()


