import random
import string

def genpass(length, uppercase=False, lowercase=False, num=False, symbol=False):
    passch = ""

    if uppercase:
        passch += string.ascii_uppercase
    if lowercase:
        passch += string.ascii_lowercase
    if num:
        passch += string.digits
    if symbol:
        passch += string.punctuation

    if not passch:
        raise ValueError("You should specify a option (uppercase, lowercase, number or symbol).")

    return ''.join(random.choice(passch) for _ in range(length))

def main():
    print("Specify your password options:")
    length = int(input("Password length: "))
    uppercase = input("Uppercases? (y/n): ").lower() == 'y'
    lowercase = input("Lowercases? (y/n): ").lower() == 'y'
    num = input("Numbers? (y/n: ").lower() == 'y'
    symbol = input("Symbols? (y/n): ").lower() == 'y'

    try:
        password = genpass(length, uppercase, lowercase, num, symbol)
        print(f"Oluşturulan şifre: {password}")
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()
