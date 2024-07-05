# Daniel Schager
# Dice Game
# 4/15/2022


import random
import math


def roll_dice():
    randomlist = []
    n = 2
    for i in range(n):
        randomlist.append(random.randint(1,6))
    value1 = int(randomlist[0])
    value2 = int(randomlist[1])
    return value1,value2

def print_dice(value):
    x = "             "
    b = "     "
    c = "       "
    if value == 1:
        print(" _______________\n|",x,"|\n|",x,"|\n|",x,"|\n|",b,"o",b,"|\n|",x,"|\n|",x,"|\n|",x,"|\n'---------------'")
    elif value == 2:
        print(" _______________\n|",x,"|\n|",b*2,"o ","|\n|",x,"|\n|",x,"|\n|",x,"|\n|"," o",b*2,"|\n|",x,"|\n'---------------'")
    elif value == 3:
        print(" _______________\n|",x,"|\n|",b*2,"o ","|\n|",x,"|\n|",b,"o",b,"|\n|",x,"|\n|"," o",b*2,"|\n|",x,"|\n'---------------'")
    elif value == 4:
        print(" _______________\n|",x,"|\n|"," o",c,"o ","|\n|",x,"|\n|",x,"|\n|",x,"|\n|"," o",c,"o ","|\n|",x,"|\n'---------------'")
    elif value == 5:
        print(" _______________\n|",x,"|\n|"," o",c,"o ","|\n|",x,"|\n|",b,"o",b,"|\n|",x,"|\n|"," o",c,"o ","|\n|",x,"|\n'---------------'")
    elif value == 6:
        print(" _______________\n|",x,"|\n|"," o",c,"o ","|\n|",x,"|\n|"," o",c,"o ","|\n|",x,"|\n|"," o",c,"o ","|\n|",x,"|\n'---------------'")

    return " "

def situational(total,balance,transaction):
    if total == 7 or total == 11:
        print("You Win!\n")
        balance += transaction
        
    elif total == 12 or total == 2 or total == 3:
        print("CRAPS!\n\nYou Lose\n")
        balance = balance - transaction
        
    elif total == 4:
        print("Your point is 4")
        srandom = input("\nPress ENTER to roll the dice\n")
        dice1,dice2 = roll_dice()
        total = dice1 + dice2
        print(print_dice(dice1))
        print(print_dice(dice2))
        while total != 7 and total != 4:
            print("\nNothing...")
            srandom = input("\nPress ENTER to roll the dice\n")
            print("\nRolling dice...\n")
            dice1,dice2 = roll_dice()
            total = dice1 + dice2
            print(print_dice(dice1))
            print(print_dice(dice2))
        if total == 7:
            print("You Lose\n")
            balance = balance - transaction
        elif total == 4:
            print("You Win!\n")
            balance += transaction
            
    elif total == 5:
        print("Your point is 5")
        srandom = input("\nPress ENTER to roll the dice\n")
        dice1,dice2 = roll_dice()
        total = dice1 + dice2
        print(print_dice(dice1))
        print(print_dice(dice2))
        while total != 7 and total != 5:
            print("\nNothing...")
            srandom = input("\nPress ENTER to roll the dice\n")
            print("\nRolling dice...\n")
            dice1,dice2 = roll_dice()
            total = dice1 + dice2
            print(print_dice(dice1))
            print(print_dice(dice2))
        if total == 7:
            print("You Lose\n")
            balance = balance - transaction
        elif total == 5:
            print("You Win!\n")
            balance += transaction

    elif total == 6:
        print("Your point is 6")
        srandom = input("\nPress ENTER to roll the dice\n")
        dice1,dice2 = roll_dice()
        total = dice1 + dice2
        print(print_dice(dice1))
        print(print_dice(dice2))
        while total != 7 and total != 6:
            print("\nNothing...")
            srandom = input("\nPress ENTER to roll the dice\n")
            print("\nRolling dice...\n")
            dice1,dice2 = roll_dice()
            total = dice1 + dice2
            print(print_dice(dice1))
            print(print_dice(dice2))
        if total == 7:
            print("You Lose\n")
            balance = balance - transaction
        elif total == 6:
            print("You Win!\n")
            balance += transaction

    elif total == 8:
        print("Your point is 8")
        srandom = input("\nPress ENTER to roll the dice\n")
        dice1,dice2 = roll_dice()
        total = dice1 + dice2
        print(print_dice(dice1))
        print(print_dice(dice2))
        while total != 7 and total != 8:
            print("\nNothing...")
            srandom = input("\nPress ENTER to roll the dice\n")
            print("\nRolling dice...\n")
            dice1,dice2 = roll_dice()
            total = dice1 + dice2
            print(print_dice(dice1))
            print(print_dice(dice2))
        if total == 7:
            print("You Lose\n")
            balance = balance - transaction
        elif total == 8:
            print("You Win!\n")
            balance += transaction

    elif total == 9:
        print("Your point is 9")
        srandom = input("\nPress ENTER to roll the dice\n")
        dice1,dice2 = roll_dice()
        total = dice1 + dice2
        print(print_dice(dice1))
        print(print_dice(dice2))
        while total != 7 and total != 9:
            print("\nNothing...")
            srandom = input("\nPress ENTER to roll the dice\n")
            print("\nRolling dice...\n")
            dice1,dice2 = roll_dice()
            total = dice1 + dice2
            print(print_dice(dice1))
            print(print_dice(dice2))
        if total == 7:
            print("You Lose\n")
            balance = balance - transaction
        elif total == 9:
            print("You Win!\n")
            balance += transaction

    elif total == 10:
        print("Your point is 10")
        srandom = input("\nPress ENTER to roll the dice\n")
        dice1,dice2 = roll_dice()
        total = dice1 + dice2
        print(print_dice(dice1))
        print(print_dice(dice2))
        while total != 7 and total != 10:
            print("\nNothing...")
            srandom = input("\nPress ENTER to roll the dice\n")
            print("\nRolling dice...\n")
            dice1,dice2 = roll_dice()
            total = dice1 + dice2
            print(print_dice(dice1))
            print(print_dice(dice2))
        if total == 7:
            print("You Lose\n")
            balance = balance - transaction
        elif total == 10:
            print("You Win!\n")
            balance += transaction

    return balance


def integer_check(string):
    try:
        string = int(string)
        return string
    except:
        string = "Q"
        return string


print("Hello, welcome to the dice game")
starting_up = input("Enter 'i' for information regarding odds and code of the program, else press ENTER to continue\n")
if starting_up == "i":
    print("The code for this program was created by Daniel Schager, a student at Indiana Wesleyan. The numbers generated from the random number function use the 'random' input to choose a un-prepdictable number from 1-6. The code for this program is primarily readable considering the repeated use of 'if' statements - determining whether or not the total of the two dice results in a win or loss.") 
balance = input("\nEnter starting balance: ")
while balance != "Q":
    print("You have", "$" + str(balance))
    balance = integer_check(balance)
    transaction = input("Place bet size: ")
    transaction = integer_check(transaction)
    if transaction == "Q":
        print("Incorrect format")
    elif transaction <= balance:
        if transaction == balance:
            print("\nRisking it all now?\n\n FOOLISH")
        srandom = input("\nPress ENTER to roll the dice\n")
        print("\nRolling dice...\n")
        dice1,dice2 = roll_dice()
        print(print_dice(dice1))
        print(print_dice(dice2))
        total = dice1 + dice2
        balance = situational(total,balance,transaction)
        while balance == 0:
            question = input("Would you like to add money (Y/N)? ")
            if question == "Y" or question == "y":
                balance = input("Enter amount: ")
            elif question == "N" or question == "n":
                print("\nGoodbye young one")
                balance = "Q"
                
    else:
        print("Insufficient funds")



#NOTES:
        #Can create validity check proof for false input
        #Can create more efficient printing system (horizontal dice)
        


