#tuple having immutable nature

def get(d):
	print("before modifing :",d)
	d[1]=225
	print("after modifing :",d)


data=(10,20,30,40)
get(data)