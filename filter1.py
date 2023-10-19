#filter function takes iterable and apply filtering liogic on every item and returns new object

sales=[100,200,300,400,500,600,700,800]
ls=filter(lambda sale:sale>600 ,sales)

result=list(ls)
print("filter function result is:",result)

