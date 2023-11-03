#generator

def gen(n):
	yield n
	yield n+1

g=gen(6)
print(next(g))
print(next(g))