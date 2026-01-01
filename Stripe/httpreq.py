request=input().split(", ")
accepted=input().split()

s=set(accepted)
res=[]

for i in request:
	cur=i
	cur.strip()
	if cur in s:
		res.append(cur)
print(res)