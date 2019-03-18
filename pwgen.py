from random import choice

def main():

    print("pass gen")
    length = input("length of password? ")

    try:
        length = int(length)
    except TypeError:
        print("Not a number")
        exit()

    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!"£$%^&*(){}[];:\'#~?<>,.\\=+-_*/|'

    rtn_pw = ''

    for i in range(length):
        rtn_pw = rtn_pw + choice(chars)

    pretty = 's' if length > 1 else ''

    print(f'your new password of {length} character{pretty}:')
    print(rtn_pw)
    exit()

if __name__ == "__main__":
    main()
