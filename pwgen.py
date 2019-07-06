from random import choice

basic = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
basicUrlsafe = basic + "-_"
mediumUrlReserved = basicUrlsafe + ";/?:@=&"
mediumUtf8 = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~="
high = basic + "!\"#$%&'()*+,-./:;=?@[]^_`{}~|¬¦"
veryHigh = basic + "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüý"

def main():
    print('Password Generator v2')
    pLength = input('Length of password? ')
    pComplexity = input(
        '1) basic (alphanum)\n' +
        '2) basic url-safe\n' +
        '3) medium url-reserved\n' +
        '4) medium UTF-8\n' +
        '5) high\n' +
        '6) very high - ascii\n'
    )

    try:
        pLength = int(pLength)
        pComplexity = int(pComplexity)
    except:
        print('provide a number. exit.')
        exit()


    if (0 == pComplexity or 1 == pComplexity):
        charSet = basic
        charsetName = "basic (alphanum)"
    elif (2 == pComplexity):
        charSet = basicUrlsafe
        charsetName = "basic url-safe"
    elif (3 == pComplexity):
        charSet = mediumUrlReserved
        charsetName = "medium url-reserved"
    elif (4 == pComplexity):
        charSet = mediumUtf8
        charsetName = "medium UTF-8"
    elif (5 == pComplexity):
        charSet = high
        charsetName = "hgh"
    elif (6 == pComplexity):
        charSet = veryHigh
        charsetName = "very high - ascii"    
    
    loop = ''
    while (loop != 'q'):
        output = ''
        print(f'\n length = {pLength} choice = {charsetName}')
        for i in range(pLength):
            output = output + choice(charSet)
        print(output)
        loop = input('Any key to generate another. \'q\' to quit')

if __name__ == "__main__":
    main()
