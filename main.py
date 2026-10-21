import morse_conversion as morse
import os

def get_int():
    """Gets a valid input of 1, 2, or 3"""
    print("1. Encode text\n2. Decode morse code\n3. Exit")
    while True:
        choice = input(":").strip()
        if choice.isdigit()  and 0 < int(choice) < 4:
            return int(choice)
        print("Invalid")

    

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        choice = get_int()
        os.system('cls' if os.name == 'nt' else 'clear')
        if choice == 1:
            print(f"Morse: {morse.encode(input("Text: "))}")
        elif choice == 2:
            print(f"Text: {morse.decode(input("Morse: "))}")
        else:
            print("Have a good day")
            break
        input("\n\n\nEnter to Continue: ")

if __name__ == "__main__":
    main() 