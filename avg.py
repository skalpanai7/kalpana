num=int(raw_input())
list=[int(x) for x in raw_input().split()]
sum=0
for i in range(num):
	sum=sum+list[i]
print sum//num
