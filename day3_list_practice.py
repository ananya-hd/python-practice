#Print all elements in a list
list = [10,20,30,40,50,60,70]

for i in list:
    print(i)


#Find sum of list elements
list = [44,82,67,22,97,94,16,35]

sum = 0

for i in list:
    sum = sum+i

print("Total:",sum)


#Find maximum number
list = [44,82,67,22,97,94,16,35]
max = list[0]
for i in list:
    if max < i:
        max = i 
print("Maximun number is:",max)


#Find minimum number
list = [44,82,67,22,97,94,16,35]
min = list[0]
for i in list:
    if min > i:
        min = i 
print("Minimun number is:",min)


#Count even numbers in a list
num = [22,84,35,24,61,50]
count = 0
for i in num:
    if i % 2==0:
        count+= 1
print("Even number count is :",count)

#Search a number in a list
n = [10, 20, 30, 40, 50]

num = int(input("Enter the number to search: "))
found = False
for i in n:
    if i==num:
        found = True
if found == True:
    print("Number Found")
else:
    print("Number not found")