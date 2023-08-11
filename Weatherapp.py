import json, requests
#Import the use of json and requests.
#Define a main function.
def main():
  """Contains the website and api key information."""
  #Define base url and api key.
  base_url = "https://api.openweathermap.org/data/2.5/weather"
  appid = "20bcca3aa15d58ab4d96b64e511e6328"
  #Create a while loop for application to keep running.
  #Get the city name from the user. 
  while True:
    prompt = ("Enter a city name to check the weather: ")
    city = input(prompt)
    #Combine base url, city name and api key to create an url to try.
    url = f"{base_url}?q={city}&units=imperial&APPID={appid}"
    #Use a try block to requets the information.
    try:
      response = requests.get(url)
      response.raise_for_status()
      #Create the exception to print out a message if try fails.
    except requests.exceptions.RequestException:
      print("\nThat is not a valid city name please try again.\n")
      #Use an if statement to allow user to try again or quit.
      if response == requests.exceptions.RequestException:
        print(prompt)
      else:
        continue 
    #Assign the unformatted data to json response.
    unformatted_data = response.json()
    #Comment out the unformatted data can be used if wanted later. 
    #print(unformatted_data)
    temp = unformatted_data["main"]["temp"]
    print(f"The current temp is: {temp}")
    # Program gets current temperture from the response. 
    temp_max = unformatted_data["main"]["temp_max"]
    print(f"The max temp is: {temp_max}")
  # Program gets max temp from the response.
  # Program displays information to user.   
  # Ask the user if they want to check another city for weather.   
    prompt = input("\nEnter 'quit' to exit or press 'enter' to try another city: ")
  # If user enters 'quit' exit program otherwise allow user to check another city. 
  # Repeat until user enters 'quit.   
    message = "Have a nice day."
    if prompt == 'quit':
      print(message)
      break
  #End program.

#Call main function. 
main()
 
