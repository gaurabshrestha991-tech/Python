class LoginSystem:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def login(self, username, password):
        if self.username == username and self.password == password:
            print("Login Successful!")
        elif self.username == username and self.password != password:
            print("Invalid password!")
        elif self.username != username and self.password == password:
            print("Invalid username!")
        else:
            print("Invalid Username and password!")
      
user = LoginSystem("password", "1234")     
username = input("Enter Username: ")
password = input("Enter Your Password: ")


user.login(username, password)
