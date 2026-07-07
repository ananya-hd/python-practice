#Program 1: Print numbers from 1 to 10
for i in range(1,11):
    print(i)

#Program 2: Print even numbers from 1 to 20
for i in range(1,21):
    if i % 2 == 0:
        print(i)
        

#Program 3: List basics
marks = [85,90,95,96,97,99]

print("Marks List:", marks)
print("First Mark:",marks[0])
print("Last Mark:",marks[5])


#Program 4: Find total marks using loop
marks = [85,90,95,96,97,99]

total = 0
for i in marks:
    total = total+i
print("Total Marks:",total)


#Program 5: Find average marks
marks = [85,90,95,96,97,99]

total = 0
for i in marks:
    total = total+i

average = total / len(marks)
print("Total Marks:",total)
print("Average marks:", average)

#Find maximum number in a list
num = [89,90,100,90,109,121]
max = num[0]
for i in num:
    if max < i:
        max = i
print("Maximum number :",max)
