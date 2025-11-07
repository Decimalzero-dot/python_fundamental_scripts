myFamily = {
    "father" : {"name": "John", "year": 1985},
    "mother" : {"name": "Jane", "year": 1990}
}

user_input = input("Enter either 'father' or 'mother': ")
if user_input in myFamily :
    member_data = myFamily [user_input]

    name = member_data["name"]
    year = member_data["year"]

    print(f"Selected member: {user_input.capitalize()}")
    print(f"Name: {name}")
    print(f"birth Year: {year}")
    
else :
    print("Family member not found")    
