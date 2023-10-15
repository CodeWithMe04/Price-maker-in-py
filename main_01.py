import random
from colorama import Fore

dict = {
    "name": "Arin",
    "age": 8,
    "verified": True,
}

pin = random.randint(1, 10)

if dict["age"] == 25 or dict["age"] >= 18:
    print("Generating your lucky pin...")
    if pin <= 3:
        print(f"{Fore.RED}You are fail...")
        print(f"{Fore.WHITE}Bye...")
    else:
        print(f"You have win $10,000 with your pin {pin}")
else:
    print("We have a trick you to win this game yes(y) or no(n): ")
    condition = str(input())
    if condition == "y" or condition == "Y":
        try:
            print("You have to change your age: ")
            newage = int(input())
            dict["age"] = newage*2
            if dict["age"] == 25 or dict["age"] >= 18:
                print("Generating your lucky pin...")
                if pin <= 3:
                    print(f"{Fore.RED}You are fail...")
                    print(f"{Fore.WHITE}Bye...")
                else:
                    print(f"You have win $10,000 with your pin {pin}")
        except Exception as err:
            print(f"{Fore.RED}Some problem occurred...")
    elif condition == "n" or condition == "N":
        print(f"{Fore.WHITE}So Bye and try again also...")
    else:
        print("Try again...")