print("I will tell you if you are a child, teen or adult")
print()
while True:
    age = input("Write your age: ")

    if age.isdigit():
        age = int(age)
        if 1 <= age <= 114:
            if 1 <= age <= 11:
                print("So you are a child.")
            elif 12 <= age <= 17:
                print("So you are a teenager.")
            else: 
                print("So you are an adult.")
            break
        else:
            print("Please write a real age.")
    else:
        print("Please write a number.")