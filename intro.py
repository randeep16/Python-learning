
import os


os.system ("cls")

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    CBOLD     = '\33[1m'

print (style.RED + '\n')

def header():
    print ("*************************************************************************")
    print ("*   Author Name     : Randeep Raj Pant                                  *")
    print ("*   Submission Date : 24 Jul 2021                                       *")
    print ("*               Python session 1                                        *")
    print ("*   Copyright (c) NIP . All rights reserved                             *")
    print ("*************************************************************************")
    print (style.WHITE + '\n')

header();    