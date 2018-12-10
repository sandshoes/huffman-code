import time
t0= time.time()
t = 0
alphabet = {}
file = open('compression.txt','rb')
for i in file:
	x = i.decode('utf-8')
	if x == 'th\n':
		break
	if t == 1:
		y = x[0:-1]
		alphabet[y] = '\n'
		t = 0
		continue
	if x[0] == '\n':
		t = 1
		continue
	alphabet[x[1:-1]] = x[0]

bit_string = ""
byte = file.read(1)
while(len(byte) > 0):
	byte = ord(byte)
	bits = bin(byte)[2:].rjust(8, '0')
	bit_string += bits
	byte = file.read(1)

padded_info = bit_string[:8]
extra_padding = int(padded_info, 2)

bit_string = bit_string[8:] 
encoded_text = bit_string[:-1*extra_padding]
file.close()

file = open('decompressed.txt','w', encoding = 'utf-8')
string = ''

for x in encoded_text:
	string += x
	if string in alphabet:
		file.write(alphabet[string])
		string = ''
file.close()
t1 = time.time()
print(t1-t0)
