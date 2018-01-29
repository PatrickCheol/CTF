from itertools import cycle

cipher=bytearray.fromhex("172d330d21283133037c65101220703c187a3b1033202f24092c33103021261721273821773b3e").decode()
flag_knwon="AceBear{"

key = ""
for a, b in zip(flag_known, cipher):
	key += chr(ord(a) ^ ord(b))
key = cycle(key)

flag = ""
for a, b in zip(key, cipher):
	flag += chr(ord(a) ^ ord(b))

print ("flag ==> " + flag)
