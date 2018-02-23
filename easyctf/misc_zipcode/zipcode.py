from socket import *
import time
import base64


zipcode=[input().split() for _ in range(33121)]
#for zipco,b,area,d,e,logi,ladi in zipcode:


ip="c1.easyctf.com"
port=12483

s=socket(AF_INET,SOCK_STREAM)  #서버와 소통할 소켓을 만드는 과정
s.connect((ip,port))

print (s.recv(1024))  #서버에서 데이터를 가져온다.(예를 들어 "1번답을 입력하세요: ")
time.sleep(4)
while True:
	a=s.recv(1024)
	print(a)
	matter_zip=a.split()[-1][0:-1]
	for zipco,q,r,area,water,d,e,lati,logi in zipcode:
		if zipco.encode()==matter_zip:
			if 'longitude'.encode() in a:
				s.send(logi.encode()+'\n'.encode())
			elif 'latitude'.encode() in a:
				s.send(lati.encode()+'\n'.encode())
			elif 'water'.encode() in a:
				s.send(water.encode()+'\n'.encode())
			else:
				s.send(area.encode()+'\n'.encode())
s.close()

