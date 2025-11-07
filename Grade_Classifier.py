score = input("Enter Test Score ")
if int(score) >= 80 and int(score) <= 100 :
    print("Execellent")
elif int(score) >= 50 and int(score) <= 79 :
    print("Good")
elif int(score) <= 49 :
    print("Needs to Improve!")
else :
    print("Invalid score entered")    