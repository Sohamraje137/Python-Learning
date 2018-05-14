from functools import reduce

data=[2,3,5,7,11,13,17,19,23,29]
data1=[0,2,3,5,7,11,13,17,19,23,29]

multiplier= lambda x,y: x*y


print(reduce(multiplier,data))

prod=1
for i in data:
	prod=prod*i


print(prod)


import statistics

avg=statistics.mean(data)
print(avg)

filter(lambda x:x>avg, data)

print(filter)


print(list(filter(lambda x: x>avg, data)))



print(list(filter(None,data1)))

#none,"",0.0,0j,{},(),[],false

import math

def area(r):
	return r*r*3.1428

print(list(map(area,data1)))