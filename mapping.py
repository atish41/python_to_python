#using map function here

without_gst_cost=[100,200,300,400]
with_gst_cost=map(lambda x:x+10,without_gst_cost)

x=list(with_gst_cost)

print("without gst cost items is :",without_gst_cost)
print("with gst cost will be :",x)
