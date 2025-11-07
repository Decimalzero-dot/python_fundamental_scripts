stored_email = "user@example.com"
stored_password = "12345"

user_email = input("Enter Your Email ")
user_password = input("Enter Your Password ")
if user_email == stored_email and user_password == stored_password :
    print("Login successfull")
else :
    print("Invalid credentials!")    