# Subset Counting

그냥 인터넷에 떠도느 subset을 찾아서 sum만 구현했다.  
구현하기도 귀찮고 구글에는 없는게 없기 때문이다.  

```python
import itertools

def subsets(s):
    for cardinality in range(len(s) + 1):
        yield from itertools.combinations(s, cardinality)

a,b=[int(x) for x in input().split()]
perm_list=[int(x) for x in input().split()]
cnt=0
pp=subsets(perm_list)
for p in pp:
	if len(p)==0:
		continue
	if sum(p)==b:
		cnt+=1
print(cnt)
```
