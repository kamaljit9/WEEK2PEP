#q4
l=[34,893,256,876]
result=map(lambda x:(x*9/5)+32,l)
f=list(result)
print(f)

fresult=filter(lambda x:x>100,f)
print(list(fresult))
