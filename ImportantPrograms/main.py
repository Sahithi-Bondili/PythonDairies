# Prime
num = int(input("Enter the number"))
for i in range(2,num+1):
    if (num % i) == 0 and num != i:
        print(str(num) + "is not a prime number")
        break
    elif num == i:
        print(str(num) + "is a prime number")
        
# Prime Advanced
num = int(input("Enter a number:"))
if num == 2:
  print("2 is Prime number")
elif num%2==0:
  print(str(num) + " is not prime")
else:
  for i in range(3, num+1, 2):
    if num % i == 0 and num != i:
      print(str(num) + " is not prime")
      break
    elif num == i:
      print(str(num) + " is prime")

# Least Frequent character 
s1 = input("Enter the test:")
for i in s1:
  cnt = s1.count(i)
  if cnt == 1:
    print(i)
    
# Factorial- using for
num = int(input("Enter one number:"))
fac = 1
for i in range(1,num + 1):
 fac = fac*i
print("factorial of", num, "is", fac )

# Factorial- using while
num = int(input("enter a number: "))
fac = 1
i = 1
while i <= num:
  fac = fac * i
  i = i + 1
print("factorial of ", num, " is ", fac)




