import csv

with open("SOCR-HeightWeight.csv", newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)
new_data=[]

for i in range(len(file_data)):
    n=file_data[i][2]
    new_data.append(float(n))

m=len(new_data)
new_data.sort()

if m%2 == 0:
    #getting the first number 
    median1=float(new_data[m//2])
    #getting the second number
    median2=float(new_data[m//2-1])
    #finding the median
    median=(median1+median2)/2
else:
    median=new_data[m//2]

print("The median is: " + str(median))