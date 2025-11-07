age = input("Enter Your Age ")
name = input("Enter Your Name ")
if int(age) >= 18 :
    print(f"{name} pays 300KES for admission.")
elif  int(age) >= 12 and int(age) <= 17 :
    print(f"{name} pays 200KES for admission.")
elif int(age) <= 11 :
    print(f"{name} pays 100KES for admission.")
 