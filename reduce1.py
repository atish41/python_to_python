#reduce function(fun,iterable) is a predefined function existing in functools

#this function apply a function of two arguments 
#this function reduce the  sequence to a single value


from functools import reduce

sales=[100,200,300,400,500,600,700,800]
total_sales=reduce(lambda x,y :x+y,sales)

print("total sales :",total_sales)
