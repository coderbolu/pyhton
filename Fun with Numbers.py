import requests

# Create a variation for the number of attempts
num_attempts = 5
attempt = 0

# Use the while loop to make the attempts
while attempt < num_attempts:
  try:
    reply = input("Do you want trivia on a number or a year or date? Please enter 1 or 2: ")

# Use the if statement to give variable to the user input
    if reply == "1":
      number_hub = input("Enter any number for trivia response: ")

      try:
        # Validate that the input is a number
        int(number_hub)  # This will raise a ValueError if not a number


# Create a variable for the user input
        request_url = f"http://numbersapi.com/{number_hub}/trivia?json"

# Create a variable to store the response
        response = requests.get(request_url)

      except ValueError:
        print("Error: Please enter a valid number.")
        continue  # Skip to the next iteration of the loop

# Repeat the same steps for the second reply
    elif reply == "2":
      year_hub = input("Enter any year for trivia response: ")
      request_url = f"http://numbersapi.com/{year_hub}/year?json"
      response = requests.get(request_url)

# Use the else statement to give the user an error message
    else:
      print("Oooppssss...you entered the wrong number, please enter 1 or 2" +"......")
      continue  # Skip to the next iteration of the loop

    response.raise_for_status()  # Raise an exception for non-200 status codes

# Convert the data to a JSON format and print the data
    data = response.json()
    if "text" in data:
      print(data["text"])
    if "type" in data:
      print(data["type"])
      print(["...."])

  except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

  attempt += 1

# Use the if statement to control the attempts
if attempt == num_attempts:
  print("You have exhausted all attempts. Access denied!")