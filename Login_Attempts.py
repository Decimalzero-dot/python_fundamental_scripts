attempts = 0
correct_password = "pass123"

while attempts < 3 :
    user_input = input("Enter Your Password: ")
    if user_input == correct_password :
        print("Access granted")
        break
    else :
        print(f"Wrong password, try again.")

        attempts += 1
    if attempts == 3 :
        print("Account locked.")

