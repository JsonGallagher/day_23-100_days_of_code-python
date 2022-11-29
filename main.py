def login_prompt():
  while True:
    username = input("What is your username? ")
    password = input("What is your password? ")
    
    if username == 'david' and password == 'baldies4life':
      print()
      print("Login Success. Welcome to Replit!")
      break
    else:
      print("That is not the correct username or password. Try again!")
      print()
      
print("Replit Login System")
print()
login_prompt()