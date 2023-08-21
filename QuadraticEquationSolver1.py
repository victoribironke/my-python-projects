import math

def calculation():
    while True:
        try:
            a = int(input("a = "))
            b = int(input("b = "))
            c = int(input("c = "))
            first_step = (b * b) - (4 * a * c)
            second_step = math.sqrt(first_step)
            third_step = second_step - b
            fourth_step = (-1 * second_step) - b
            first_ans = third_step / (2 * a)
            second_ans = fourth_step / (2 * a)
            if first_ans == second_ans:
                print(f"The answers are {first_ans} twice.")
            else:
                print(f"The roots are {first_ans} and {second_ans}.")
            response = input("Do You Have Another Question? ")
            if response == "yes" or response == "Yes":
                continue
            else:
                break
        except ValueError:
            print("This quadratic equation is unsolvable.")
            response = input("Do You Have Another Question? ")
            if response == "yes" or response == "Yes":
                continue
            else:
                break

calculation()