# Dictionary of 26 letters + the space character with their 2x3 grid representation.
Braille_dict = {'a': "100000", 'b': "110000", 'c': "100100", 'd': "100110", 'e': "100010",
                'f': "110100", 'g': "110110", 'h': "110010", 'i': "010100", 'j': "010110",
                'k': "101000", 'l': "111000", 'm': "101100", 'n': "101110", 'o': "101010",
                'p': "111100", 'q': "111110", 'r': "111010", 's': "011100", 't': "011110",
                'u': "101001", 'v': "111001", "w": "010111", 'x': "101101", 'y': "101111",
                'z': "101011", ' ': "000000"
                }


def solution(s):
    minions_sign = ""
    limit = 0 # the sign can hold less than 50 characters only
    for i in s:
        if i in Braille_dict.keys():
            if limit >= 50:
                break
            minions_sign += Braille_dict.get(i)
            # Next I'm gonna handle the uppercase letters
        elif i in str(Braille_dict.keys()).upper():
            if limit >= 50:
                break
            i = i.upper()
            # 000001 is how Braille indicates that the next letter is capital case
            minions_sign = minions_sign + "000001" + str(Braille_dict.get(i.lower()))
        limit += 1
    print(minions_sign)


def main():
    print("\t\tBraille's Printer\n")
    s = input("Please type what you'd like to print in Braille:\n")
    solution(s)


if __name__ == "__main__":
    main()
