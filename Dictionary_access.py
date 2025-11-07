user_profile = {
    "name" : "Jane Doe",
    "email" : "jane@example.com",
    "verified" : False
}

verification = input("Has the user verified their account? (yes/no): ")
if verification == "yes" :
    user_profile ["verified"] = True
    # print("updated profile")
    print(f"{user_profile}")
else :
    print("Verification pending.")    