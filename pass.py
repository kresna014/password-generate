import random
import string

def generate_password(lenght):
    # penggabungan semua karakter
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # penggabungan semua karakter
    all_chars = lowercase + uppercase + digits + symbols

    # panjang password
    if lenght < 8:
        print("Panjang password minimal 8 karakter")
        return None
    
    # password random
    password = ''.join(random.choice(all_chars) for _ in range(lenght))
    return password


def main():
    print("=== Password Generator ===")
    try:
        lenght = int(input("Masukkan panjang password: "))
        if lenght < 8:
            print("Panjang password minimal 8 karakter")
            return
        password = generate_password(lenght)
        print(f"Password Anda: {password}")
    except ValueError:
        print("Masukkan angka yang valid")

if __name__ == "__main__":
    main()
    