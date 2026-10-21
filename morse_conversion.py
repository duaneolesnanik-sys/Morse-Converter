morse_code_dict = {"A": ".-", "B":"-...", "C":"-.-.",
                   "D": "-..", "E":".", "F":"..-.",
                   "G":"--.", "H":"....", "I":"..",
                   "J":".---", "K":"-.-", "L":".-..",
                   "M":"--", "N":"-.", "O":"---",
                   "P":".--.", "Q":"--.-", "R":".-.",
                   "S":"...", "T":"-", "U":"..-",
                   "V":"...-", "W":".--", "X":"-..-",
                   "Y":"-.--", "Z":"--..", "1":".----",
                   "2":"..---", "3":"...--", "4":"....-",
                   "5":".....", "6":"-....", "7":"--...",
                   "8":"---..", "9":"----.", "0":"-----",
                   " ":" "}

def encode(str1):
    """Coverts given string to morse code, skips unkown characters, and reports errors"""
    str2 = ""
    for i in str1.upper().strip():
        if morse_code_dict.get(i):
            str2 += morse_code_dict[i]+" "
        else:
            print(f"[Warning] Character '{i}' not recognized. Skipped.")
    return str2

def decode(str1):
    """Converts given morse code to letters(capital), skips incorrect sequences, and reports errors"""
    str2 = " "+str1.replace(" ","  ")+" "
    for let, morse in morse_code_dict.items():
        str2 = str2.replace(" "+morse+" ", let)
    str2,  str3 = (str2.replace("  "," ")[1: ] if str1[0] != " " and str2.replace("  "," ")[0] == " " else str2.replace("  "," ")), str2
    for i in morse_code_dict.keys():
        str3 = str3.replace(i,"")
    if len(str3) > 0:
        j, r = "", 0
        for i in range(len(str3)):
            j, p = str3[r:i], str3[r:i+1]
            if not (p in str2 and not i+1 == len(str3)):
                j, r = (p if i+1 == len(str3) else j), r+len(j)
                print(f"[Warning] Sequence '{j}' not recognized. Skipped.")
                str2 = str2.replace(j, "")
    return str2

def main():
    print(decode(", rt ..--- -... .-. -.- . . .   ---. rt"))
    print(decode(".--"))
    print(decode(encode("hello sir")))

if __name__ == "__main__":
    main()