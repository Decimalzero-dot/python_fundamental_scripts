numbers_list = [3,2,54,32,8,1,6]
count = 0
print("Numbers greater than 10: ")
for num in numbers_list :
    if num <= 10 :
        continue
    print(num)
    count += 1

print(f"Total numbers greater than 10: {count}")
