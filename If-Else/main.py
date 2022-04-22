# candidate validation for Interview Call based of Cut-off graduation percentage
graduationPercentage = float(input("Enter the graduation percentage"))
if graduationPercentage >= 75 :
 print("your interview is scheduled on next monday")
 print("please bring one gov id along with you")
else :
 print("sorry you are not elligbile.please try for a different position")


# Validate the rider based on age
height = float(input("Enter the height")) 
if height > 120 :
  print("can ride")
else :
  print("can't ride")
number = int(input("which no do you want to check"))
if (number % 2) == 1 :
  print("This is an odd number")
else : 
  print("This is an even number")


#Age validator to vote using If-Else
adharNumber = input("please enter  your adharnumber")
length = len(adharNumber)
if length == 12:
  print("we are trying fetch you details...")
  name = input("mean while please confirm your name:")
  year = input ("please confirm your birth year:")
  age = 2022-int(year)
  if age >= 18 :
   print(f"Hello {name},you can vote.")
   firstVote = input("Is this your first vote?")
   if firstVote == "yes" :
    print("please  collect your voter id at your neares e-scva center")
  else :
   print(f"Hello {name}, you are not allowed to vote,try after {18-age} years.")
else  : 
  print("please enter a valid Aadhar number and try again")
