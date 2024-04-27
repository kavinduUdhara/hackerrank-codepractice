# Migratory Birds

[Hacker Rank link to the challange](https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true)

my solution:
```python
def migratoryBirds(arr):
    birds = {}
    for i in arr:
        if(i in birds):
            birds[i] += 1
        else:
            birds[i] = 1
    birds_by_val = {}
    for (key,val) in birds.items():
        if val in birds_by_val:
            birds_by_val[val].append(key)
        else:
            birds_by_val[val] = [key]
    
    sorted_dict_desc = dict(sorted(birds_by_val.items(), reverse= True))
    for j in sorted_dict_desc.values():
        sorted_array = sorted(j)
        return sorted_array[0]
```

others codes:
```python
from collections import Counter

n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
freq = Counter(types)
print(max(freq, key=freq.get))
```

```python
import sys
from collections import Counter

n = int(input().strip())
types = list(map(int, input().strip().split(' ')))

p = Counter(types)

m = max(p.values())
f = [k for k,v in p.items() if v == m]
print(min(f))
```

```python
n = int(input().strip())
types = list(map(int, input().strip().split(' ')))
counts = [0,0,0,0,0,0]
for bird in types:
    counts[bird] += 1
winner = 0
for x in range(6):
    if counts[x] > counts[winner]:
        winner = x
print(winner)
```

