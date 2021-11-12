#Rock,Paper and Scissors
import random
print("\n Hello ,\nThis is a game of ROCK,PAPER and SCISSORS")
print("Developed by Pranjal Sinha\n")
list=['St','Pa','Sc']
print("1 for Stone\n 2 for Paper\n 3 for Scissors")
chance=10
win_P=0
win_C=0
current_chance=0

while(current_chance<10): 
    p_num=int(input("\nEnter your choice: "))
    c_num=random.choice(list)

    if((p_num==1 and c_num== "St") or (p_num==2 and c_num== "Pa") or (p_num==3 and c_num== "Sc")):
        print(f"\nYour choice:{p_num} and Computer's choice:{c_num}")
        print("Both have zero points as it same and the chance done is elapsed")

    elif(p_num==1 and c_num=="Pa"): 
        current_chance+=1
        win_C+=1
        print("\nYour guess: Stone\nComputer's guess: Paper\n\nComputer wins 1 point.\n")
        print(f"Your points: {win_P}\nComputer's points: {win_C}\n")
    
    elif (p_num==1 and c_num=="Sc"):
        win_P += 1
        current_chance += 1
        print("\nYour guess: Stone\nComputer's guess: Scissors\n\nCongratulation, you wins 1 point.\n")
        print(f"Your points: {win_P}\nComputer's points: {win_C}\n")

    elif (p_num==2 and c_num=="St"):
        win_P += 1
        current_chance += 1
        print("\nYour guess: Paper\nComputer's guess: Stone\n\nCongratulation, you wins 1 point.\n")
        print(f"Your points: {win_P}\nComputer's points: {win_C}\n")

    elif (p_num==2 and c_num=="Sc"):
        win_C += 1
        current_chance += 1
        print("\nYour guess: Paper\nComputer's guess: Scissors\n\nComputer wins 1 point.\n")
        print(f"Your points: {win_P}\nComputer's points: {win_C}\n")

    elif (p_num==3 and c_num=="St"):
        win_C += 1
        current_chance += 1
        print("\nYour guess: Scissors\nComputer's guess: Stone\n\nComputer wins 1 point.\n")
        print(f"Your points: {win_P}\nComputer's points: {win_C}\n")

    elif (p_num==3 and c_num=="Pa"):
        win_P += 1
        current_chance += 1
        print("\nYour guess: Scissors\nComputer's guess: Paper\n\nCongratulation, you wins 1 point.\n")
        print(f"Your points: {win_P}\nComputer's points: {win_C} \n")

    else:
        print("\nInvalid input!!!")
        print("Please, enter 1 for Stone, 2 for Paper and 3 for Scissors.")

while (current_chance==10):

    if (win_P>win_C):
        print(f"\nCongratulation, you win with {win_P} points.")

    elif (win_P<win_C):
        print(f"\nOh my, Computer is win with {win_C} points.")

    else:
        print("\nMatch is Draw.\n")
        print(f"Your points: {win_P}\nComputer's points: {win_C}\n")

    break
