# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Sedrick Howard
# Creation Date: July 28, 2023
# Below is a simple program with several.  You need to identify the issues and correct them.

import random
import time
#This funtion should be all lower case letters with a underscore between each word.
#def displayIntro():
def display_intro():
  #This print function does not have proper quotations.
  #There should be a discription here telling what this function does such as the following: """This function will display the intro to the program"""
  #This statement should be checked for proper grammar. 
  #print('''You are in a land full of dragons. In front of you,
	#you see two caves. In one cave, the dragon is friendly
	#and will share his treasure with you. The other dragon
	#is greedy and hungry, and will eat you on sight.''')
  #Assign a variable to this statement such as intro or message.
  #Use \n before each sentence to start each sentence on another line.
  intro ="You are in a land full of dragons. \nIn front of you, you see two caves. \nIn one cave, the dragon is friendly and will share his treasuse with you. \nThe other dragon is greedy, hungry, and will eat you on sight."
  #Use the print function to print the intro variable. 
  #print()
  print(intro)
#This funtion should be all lower case letters with a underscore between each word.
#def chooseCave():
def choose_cave():
  #There should be a description of what this function does with three double quotes on each side ("""""")
  #Example: """This function lets user choose the cave."""
 #Cave does not have proper indention should only be two spaces. 
    #cave = ''
  #This while loop is not indented correctly. 
        #while cave != '1' and cave != '2':
            #print('Which cave will you go into? (1 or 2)')
            #cave = input()
  #while cave != '1' and cave != '2':
    #There should be user input function here or a prompt, not a print statement.
    #If using intergers for input then convert the input into an interger for program to acknowledge.
    #print('Which cave will you go into? (1 or 2)')
  cave = ''
  while cave != '1' and cave != '2':
    #Convert input into intergers for later in the program.
    #Store the user input into the cave varaible.
    cave = int(input("Which cave will you go into? (1 or 2) "))
    #The word caves is mispelled compared to the variable cave. 
    #return caves
    return cave 
#This funtion should be all lower case letters with a underscore between each word.
#def checkCave(chosenCave):
def check_cave(choose_cave):
  #There should be a description of what this function does with three double quotes on each side ("""""")
  #Example: """This function checks for the chosen the cave."""
    #The rest of this funtion is not indented properly should only be 2 spaces.
    #print('You approach the cave...')
    #sleep for 2 seconds
    #time.sleep(2)
    #print('It is dark and spooky...')
    #sleep for 2 seconds
    #time.sleep(3)
    #print('A large dragon jumps out in front of you! He opens his jaws and...')
    #print()  
    #sleep for 2 seconds
    #time.sleep(2)
    #friendlyCave = random.randint(1, 2)
    print("You approach the cave...")
    #sleep for 2 seconds
    time.sleep(2)
    print("It is dark and spooky...")
    #sleep for 2 seconds
    #This sleep function should be 2 secs not 3.
    #time.sleep(3)
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his jaws and...")
  #This print statement is not necessary.
  #print()
  #sleep for 2 seconds
    time.sleep(2)
  #This variable should be equal to 2
  #This variable should be all lower case letters with a underscore between each words.
  #friendlyCave = random.randint(1, 2)
    friendly_cave = random.randint(1, 2)
  #This if statement is not properly indented.
  #This if statement is not worded correctly.
      #if chosenCave == str(friendlyCave): 
    
    if choose_cave == friendly_cave:
      #print('Gives you his treasure!')
      print("Gives you his treasure!")
    #else:
    
    else:
        #print 'Gobbles you down in one bite!'
        #This print function does not have proper syntax.
      print("Gobbles you down in one bite!")
     
      
      
  
#Have to change the rest of the program to the proper words used in the def functions.
#displayIntro()
#caveNumber = choosecave()
#checkCave(caveNumber)
display_intro()
#caveNumber should be all lower case letters with a underscore between each word.
#choose_cave()
cave_number = choose_cave()
check_cave(cave_number)
#Check print statement for proper spelling and punctuation.
#print("Thanks for planing")
print("Thanks for playing.")
#All throughout the program quotations were inconsistent. Try to use double quotes so that you can use single quotes when you need to inside statements.
#There is also a while loop used but no way to get back to that loop, the program just exits after one try. Are we creating a loop in case the user wants to try again? If that is the intention find a way to incorporate that and the last print statement inside the loop when user wants to quit.
#I did not change the loop as I did not know the intentions but we can discuss it farther if needed. 
