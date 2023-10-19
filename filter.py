#filter(fun,iterable)

items_cost=[999,500,1010,1200,799,1500]
gt_thousend=filter(lambda x:x>1000 ,items_cost)

x=list(gt_thousend)

print("cost of the items are :",items_cost)
print("eligeble for discounts items are :",x)