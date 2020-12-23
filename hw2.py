user = []
user.append(raw_input("Enter your name: "))
user.append(raw_input("Enter your last name: "))
user.append(int(raw_input("Enter your age: ")))
user.append(int(raw_input("Enter your birth(just year): ")))

print("User Informations: ")
for i in range(len(user)):
    print(user[i])

if user[2] < 18:
    print("You cant go out because it's too dangerous")
else:
    print("You can go out to the street")

