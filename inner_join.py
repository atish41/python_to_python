#inner join
import pandas as pd

d1={
	"id":[1,2,3,4,5,6],
	"Name":["Pradhan","Venu","Madhurima","Nireekshan","Shafi","Veeru"],
	"Subject":["english","java","html","python","c","dot net"]

}

d2={
	"Id":[11, 12, 13, 14, 15, 16], 
	"Name": ["Srinu", "Sumanth", "Neelima", "Daniel", "Arjun", 
	"Veeru"], 
     	"Subject":["Java", "Html", "Cpp", "Python", "C", "dot net"] 
 	
}

df1=pd.DataFrame(d1)
df2=pd.DataFrame(d2)

inn_join=pd.merge(df1,df2,on="Subject",how="inner")

print(df1)
print()
print(df2)
print()
print(inn_join)