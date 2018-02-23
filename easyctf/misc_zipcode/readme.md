# Zipcode  

문제에 들어가보면 미국의 zipcode에 관한 문제를 준다.  
문제로 나오느 zipcode에 대한 위도가 몇인지 경도가 몇인지 30초이내에 50문제를 풀면된다.  
구글에서 zipcode 검색하면 2010년 기준의 zipcode 관련 데이터가 나온다.  
포맷이 다음과 같다.  

```text
GEOID	ALAND	AWATER	ALAND_SQMI	AWATER_SQMI	INTPTLAT	INTPTLONG                                                                                                                                  
00601	166659883	799293	      64.348	       0.309	 18.180555	 -66.749961                                                                                                                                 
00602	79287203	4448761	      30.613	       1.718	 18.361945	 -67.175597                                                                                                                                 
00603	81884524	184089	      31.616	       0.071	 18.455183	 -67.119887 
```


그래서 해당 텍스트를 받고 파이썬을 통해서 답을 찾아서 제출하는 방식으로 프로그래밍을 했다.  

```python
	zipcode=[input().split() for _ in range(33121)]


	ip="c1.easyctf.com"
	port=12483

	s=socket(AF_INET,SOCK_STREAM)  #서버와 소통할 소켓을 만드는 과정
	s.connect((ip,port))

	print (s.recv(1024))  #서버에서 데이터를 가져온다.(예를 들어 "1번답을 입력하세요: ")
```

s.recv(1024)를 통해 가져온 문제를 읽고 파싱을해서 다음과 같이 처리한다.    

```python
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
```  

이렇게 하면 정상적으로 플래그가 나오게 된다. 하지만 플래그 값을 저장안해놔서 적을 수가 없음!