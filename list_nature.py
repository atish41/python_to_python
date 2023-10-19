#list having ,mutable natuer

def get_data(d):
	print("before modifying :",d)
	d[1]=999
	print("after modifying :",d)

a=[10,20,30,50]
get_data(a)