class Login:
  accounts = {}

  def Check(name:str, password: str):
    if (account[name] == password):
      #access the account
    else:
      return "wrong login info"

  def AddAccount():
    username = input("Please enter a username: ")
    while(username in accounts.keys()):
      username = input("\nUsername taken: please input a different username: ")
    password = input("Please enter a password: ")
    account[username] = password
    
      

  
