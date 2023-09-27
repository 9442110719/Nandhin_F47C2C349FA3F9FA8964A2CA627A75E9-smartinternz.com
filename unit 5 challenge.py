# Program to transpose a matrix using a nested loop


X = [[12,7],
    [4 ,5],
    [3 ,8]]


result = [[0,0,0],
         [0,0,0]]


# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]


for r in result:
   print(r)
  # Python program to find the largest number among the three input numbers


# change the values of num1, num2 and num3
# for a different result
num1 = 10
num2 = 14
num3 = 12


# uncomment following lines to take three numbers from user
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))


if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3


print("The largest number is", largest)