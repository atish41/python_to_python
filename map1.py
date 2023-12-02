#map(fun,iterable) function in python

no_gst=[100,200,300,400]
with_gst_cost=map(lambda item:item+10,no_gst)

result=list(with_gst_cost)
print("without gst items costs :",no_gst)
print("with gst items cost1 :",result)
