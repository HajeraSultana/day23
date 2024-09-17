print("REPLIT LOGIN SYSTEM")
print()
def logincreds():
  while True:
    username = input("What is your username?: ")
    password = input("What is your password?: ")
    print()
    if username == "sam" and password == "samr":
      print("Welcome to REPLIT!")
      break
    else:
      print("Whoops! I don't recognize that username or password. Try again!")
      print()
      continue
logincreds()