# copyright © 2022 XuanMing
# CYIVS 114030 如有PYTHON愛好者 歡迎交流

import os
import sys

os.system("pip3 install pyperclip")
import pyperclip

if (platform := sys.platform).startswith("win32"):os.system("cls")
elif platform.startswith("aix") or platform.startswith("linux"):os.system("clear")

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
    string = ""
    if MORSE:
        for mrs in Input.split(" "):
            string += CODER.TEXT[CODER.MORSE.index(mrs)]
    else:
        for text in Input:
            if text == " ":pass
            else: string += (CODER.MORSE[CODER.TEXT.index(text.upper())] + " ")
    if (Input_ := input(string+"\n複製文字? (y/n)").casefold()) == "y":
        pyperclip.copy(string[:-1])
    elif Input_ == "n":
        pass
    else: raise Exception(f"輸入錯誤指令 > {Input_}")

if __name__ == "__main__":
    Input = input("text: ")
    MORSE = True if returnType(Input) else False
    string = main()
