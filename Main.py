# copyright © 2022 XuanMing
# CYIVS 114030 如有PYTHON愛好者 歡迎交流

class CODER(object):
    TEXT = [
        "A", "B", "C", "D", "E",
        "F", "G", "H", "I", "J",
        "K", "L", "M", "N", "O",
        "P", "Q", "R", "S", "T",
        "U", "V", "W", "X", "Y",
        "Z", "0", "1", "2", "3",
        "4", "5", "6", "7", "8",
        "9"
    ]

    MORSE = [
        ".-",    "-...",  "-.-.",  "-..",   ".",
        "..-.",  "--.",   "....",  "..",    ".---",
        "-.-",   ".-..",  "--",    "-.",    "---",
        ".--.",  "--.-",  ".-.",   "...",   "-",
        "..-",   "...-",  ".--",   "-..-",  "-.--",
        "--..",  "-----", ".----", "..---", "...--",
        "....-", ".....", "-....", "--...", "---.."
        "----."
    ]


def returnType(Input):
    return ("." in Input or "-" in Input)

def main():
    string = str()
    if MORSE:
        for mrs in Input.split(" "):
            string += CODER.TEXT[CODER.MORSE.index(mrs)]
    else:
        for text in Input:
            if text == " ":pass
            else: string += (CODER.MORSE[CODER.TEXT.index(text.upper())] + " ")
    input(string)

if __name__ == "__main__":
    Input = input("text: ")
    MORSE = True if returnType(Input) else False
    main()
