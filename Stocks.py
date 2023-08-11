#Define stocks dictionary 
stocks_dict = {
  "AAPL": "150.35",
  "IBM": "125.87",
  "META": "129.47",
  "MSFT": "133.32",
  "AMD": "143.98",
  "TXN": "117.67",
  "ACN": "145.55",
  "VZ": "153.75",
  "GE": "148.23",
  "RNLX": "119.68"
}
#Try to create a while loop for user to try again. 
while True:
  #Greet user and get user_request with input statement. 
  user_request = input("Hello, please enter your a stock symbol to check: ")
  #Take user input and make it a get request from dictionary. 
  #Take user input and make it all upper case to avoid error. 
  #Create a default message if the request is not in dictionary. 
  user_response = stocks_dict.get(user_request.upper(), "\nSorry, that stock symbol is not on the list.")
  print(user_response)
  #Print a the user_response and create a prompt for user to try again. 
  prompt = input("\nPress any key to try again or 'q' to quit: ")
  #Use is statements to determine what happens next. 
  #If the user_request is not in the stocks_dict then print prompt statement. 
  if user_request.upper() not in stocks_dict:
    print(prompt)
  #Create an if statement for user to quit. 
  if prompt == "q":
    #If user enters "q" the program will stop and print "Goodbye."
    print("Goodbye")
    break 
#Program ends. 
