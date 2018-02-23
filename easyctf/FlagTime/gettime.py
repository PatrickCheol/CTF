from socket import *
import time
import base64


def send(data):

	ip="c1.easyctf.com"
	port=12482

	s=socket(AF_INET,SOCK_STREAM)  #서버와 소통할 소켓을 만드는 과정
	s.connect((ip,port))
	s.recv(1024)
	s.send(data.encode()+"\n".encode()) #데이터 전송
	start = time.time()
	recv=s.recv(1024)
	reqtime = time.time() - start
	return reqtime
ip="c1.easyctf.com"
port=12482

#s=socket(AF_INET,SOCK_STREAM)  #서버와 소통할 소켓을 만드는 과정
flag="easyctf{ez_t1m1ng_4"
#recv=s.recv(1024)
while True:
	max=0
	for letter in range(30,127):
		start_cnt=0
		#s.connect((ip,port))
		cnt_time=send(flag+chr(letter))
		print(flag+chr(letter)+"   ",end="")
		print(cnt_time)
		if cnt_time>max:
			max=cnt_time
			add_flag=letter
	flag+=chr(add_flag)
	print(flag)
	if add_flag=='}':
		print("flag ============>",flag)
		break

#easyctf{ez_t1m1ng_





