age = input("Enter Your Age ")
if int(age) >= 18 :
    print("Access granted - you receive a complimentary drink!")
elif int(age) == 16 and int(age) <= 17 :    
    print("Access granted - enjoy a juice pack!")
elif int(age) <= 15 :
    print("Access denied - you're too young!")

