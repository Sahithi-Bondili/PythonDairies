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
