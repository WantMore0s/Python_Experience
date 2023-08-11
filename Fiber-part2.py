# Display a welcome message for the program. 
message = "Hello, welcome to Howard's fiber optic installation estimates."
print(message) 
# Get the company name from the user.
# Make the prompt loop back after answering. 
while True:
  prompt = "\nWhich company would you like to check for pricing? "
# Print the name the user chosen from the input in title form.  
  name = input(prompt)
  print(f"\nYou have chosen {name.title()}'s Fiber.")
# Get the number of feet to be installed from user.
# If user purchases more than 100 feet charge $.80 per foot.
# If user purchases more than 250 feet charge $.70 per foot.
# If user purchases more than 500 feet charge $.50 per foot.   
# Help user identify to enter whole numbers and postive digits only. 
  prompt = (f"\nUsing whole numbers 0-9 only, how many feet would you like from {name.title()}? ")
  company = name.title()
  amount = input(f"\nUsing whole numbers 0-9 only, how many feet would you like from {company}? ")
# Evaluate how many feet the user inputs so that the program charges the right price.   
# Convert the amount from user into interger form and multiply be $0.87.
# Use if statements to help program pick the right price.   
# Make price per foot a constant.  
  amount = int(amount)
  #PRICE_PER_FOOT = 0.87 
   
  if int(amount) > 500:
      price_per_foot = 0.50
      #cost = price_per_foot * int(amount) 
  elif int(amount) > 250:
      price_per_foot = 0.70
      #cost = price_per_foot * int(amount) 
  elif int(amount) > 100:
      price_per_foot = 0.80
      #cost = price_per_foot * int(amount) 
  elif int(amount) <= 100:
    price_per_foot = 0.87
  cost = price_per_foot * int(amount)
     
# Display the calculated information and company name. 
# Make the program end with the word "quit"  
  print(f"\n{company}'s Fiber will cost you {cost} for that amount of feet.")
  prompt = input("\nPress the 'enter' key to check another company or 'quit' to end program. ")
  message = "\nGoodbye"
  if prompt == 'quit':
    print(message)
    break
# Did not get elif statements to work, need to figure out why.
