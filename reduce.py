from functools import reduce

item_cost=[111,222,333,455]
total_cost=reduce(lambda a,b :a+b,item_cost)
print(total_cost)