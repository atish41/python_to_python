#variable length arguments

#*args

def total_sales(*items):
	total=sum(items)
	return total

item1=250
item2=200
item3=300
item4=100

result=total_sales(item1,item2,item3,item4,)
print("total cosst of the items :",result)