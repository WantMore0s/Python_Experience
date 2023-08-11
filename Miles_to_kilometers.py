# Program converts miles to kilometers. 
# Conversion is 1 mile = 1.609 kilometer. 

def miles_to_kilometers(miles):
  kilometer = miles * 1.609
  print(f"\n{miles} mile/miles converts to {kilometer} kilometers")

# Intro the will display at the beginning of the program. 
def intro():
  print("This program converts miles to kilometers.\n")
  print("For reference: 1 mile = 1.609 kilometer\n")

# This will accept the number of miles and display the equal number of kilometers.
def main():
#Display the intro to the program.
  intro() 
 
    
  try:
    # Get the number of miles from user.
    miles_needed = int(input("Enter the number of miles: "))
  
  # Convert miles to kilometers.
    miles_to_kilometers(miles_needed)

  except:
    print("\nError, please try again by entering a number only\n")
    main()
    
  # Call the main function.
main()
