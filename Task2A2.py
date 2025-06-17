n=int(input('enter a range'))

#initilise a sum variable as 0
sum=0

for i in range(1,n+1):
    sum=sum+i

print('final sum',sum)



#program from 1 to 50
sum=0

for i in range(1,51):
    sum=sum+i

print('final sum',sum)

#we take 51 instead of 50 because range iterates for n-1