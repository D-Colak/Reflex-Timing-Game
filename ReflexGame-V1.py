import keyboard
import time
print('Hit "F" to stop. ')
print("If you land on 10, you win!")
time.sleep(2)
print("Start!")
i_dict = {1: 14, 2: 13, 4: 11}
dict_num = 0
i = 0
while True:
    if i != 21:
        print(i)
        time.sleep(0.07)
        i += 1
        if keyboard.is_pressed("f"):
            i_dict[dict_num + 1] = i
            if i == 10:
                print("\nYou Win! Nice Job!")
            if i != 10:
                print(f"\nYou landed on {i}!")
            i = 0
            restart = input("Would you like to try again? Answer with Yes or No: ")
            if restart.lower() == 'yes':
                time.sleep(3)
                i = 0
            elif restart.lower() == 'no':
                print("Thanks for playing")
                time.sleep(3)
                break
    if i >= 21:
        i = 0# Write your code here :-)
