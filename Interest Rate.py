# Write a program that determines how long it takes an investment to double.
# Use a while loop to determine this.
# Allow user to input the initial investment and interest rate.
# Program will stop after the initial investment doubles. 
# Compund interest rate = initial investment multiplied by interest rate, then add results to the initial investment to get the answer.  

interest_rate = int(input("Please enter the interest rate using whole numbers 1-9 only. (Example if interest rate is 5% then enter the number 5:) "))

initial_investment = int(input("\nPlease enter the initial investment using whole numbers. (Example if investment is $100 then enter 100:) "))

# Allow program to capture user input and use it to calculate the compound interest.
# Create compound interest rate equation
compound_interest = initial_investment * (interest_rate/100) + initial_investment
# Assign the Year to a variable 

Year = 1
# Assign the results of the equation to a variable 
result = compound_interest

# Print results along with the first year. 
print(f"\nYear Number {Year}: Investment Amount: {result}")
# Create a while loop to continue until the investment doubles. 
while True:
  # Add each year inside the while loop
  Year = Year + 1
  # Calculate the amount until it doubles inside the while loop. 
  result = result * (interest_rate/100) + result 
  # Print the year number and the amount of that year. 
  print(f"\nYear Number {Year}: Investment Amount: ${result}")
  # Create an if statement to stop program once twice the amount is reached. 
  if result > (2 * initial_investment):
    break 
# End program 
