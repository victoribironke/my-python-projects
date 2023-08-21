from random import choice, shuffle

shirt_list = ["Brown", "Purple", "Pink", "Grey", "White-S", "White-L", "White-and-Grey"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Sunday"]
shuffle(shirt_list)

with open("C:\\Users\\Tola Ibironke\\Desktop\\Shirts.txt", "w") as f:
    for i in range(6):
        shirt = choice(shirt_list)
        index = shirt_list.index(shirt)
        shirt_list.pop(index)
        print(f"{days[i]} - {shirt}")
        f.write(f"{days[i]} - {shirt}\n")
