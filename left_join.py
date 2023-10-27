#left outer join

import pandas as pd

d1={
	"id":[1,2,3,4,5,6],
	"Name":["pradhan","venu","madhurima","nireekashn","shafi","veeru"],
	"subject":["english","java","html","pythoon","c","dot net"]

}

d2={
	"id":[11,12,13,14,15,16],
	"Name":["srinu","sumanth","neelima","daniel","arjun","veeru"],
	"subject":["java","html","cpp","python","c","dot net"]
}

df1=pd.DataFrame(d1)
df2=pd.DataFrame(d2)

left_join=pd.merge(df1,df2,on="subject",how="left")

print(df1)
print()
print(df2)
print()
print(left_join)