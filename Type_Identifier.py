raw_input = input("Enter any value: ")


try:
    if isinstance(float(raw_input), float):
       
        if '.' in raw_input:
            print("Data Type: float")
            exit()
except ValueError:
    pass

try:
    if isinstance(int(raw_input), int):
        print("Data Type: int")
        exit()
except ValueError:
    pass

if isinstance(raw_input, str):
    print("Data Type: str")