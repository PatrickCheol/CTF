# Welcome 100
문제를 클릭하면 다음과 같이 Cipher만 덩그러니 놓여있다.  
자세히 살펴보면 숫자와 f까지의 문자로만 이루어져 있음을 확인할 수 있고, hex값을 디코딩해 보았다.  

```python
	cipher=bytearray.fromhex("172d330d21283133037c65101220703c187a3b1033202f24092c33103021261721273821773b3e").decode()
```

> 값은 다음과 같이 나온다
> -3
> !(13|e p<z;3 /$	,30!&!'8!w;>  

해당 값을 우리가 이미 알고 있는 플래그 형식 Acebear{과 xor 시켜서 키를 만들어 본다.  

```python
	flag_knwon="AceBear{"

	key = ""
	for a, b in zip(flag_known, cipher):
		key += chr(ord(a) ^ ord(b))
	key = cycle(key)
```  
그리고 해당 값을 cycle를 통해서 반복 시킨다.  

이후 해당 키와 전체 주어진 cipher를 xor 시키면 다음과같은 플래그가 나오게 된다.  

```python
	flag = ""
	for a, b in zip(key, cipher):
		flag += chr(ord(a) ^ ord(b))

	print ("flag ==> " + flag)
```  

> flag ==> AceBear{U23_Vi3tN4m_will_be_the_winn3r}