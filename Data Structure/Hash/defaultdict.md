# Defaultdict in Python
Dictionary in Python is an unordered collection of data values that are used to store data values like a map. Unlike other Data Types that hold only single value as an element, the Dictionary holds key:value pair. In Dictionary, the key must be unique and immutable. 
**This means that a Python Tuple can be a key whereas a Python List can not.** 
A Dictionary can be created by placing a sequence of elements within curly {} braces, separated by ‘comma’.

## Using List as default_factory

### When the list class is passed as the default_factory argument, then a defaultdict is created with the values that are list.

```
from collections import defaultdict 


# Defining a dict 
d = defaultdict(list) 

for i in range(5): 
	d[i].append(i) 
	
print("Dictionary with values as list:") 
print(d)

Output:
Dictionary with values as list:
defaultdict(<class 'list'>, {0: [0], 1: [1], 2: [2], 3: [3], 4: [4]})
```