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
