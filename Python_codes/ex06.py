from functools import lru_cache

@lru_cache(maxsize=1000)
def fib(n):
	if type(n)!= int :
		raise TypeError("n must be positive integer ")



	if n==1 :
		return 1
	elif n==2 :
		return 1
	elif n > 2:
		return fib(n-1)+fib(n-2)



for n in range(1,1001):
	print(n,":",fib(n))


for n in range(1,1001):
	print(fib(n+1)/fib(n))