# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 16:31:23 2021

@author: shane
"""
from admin import read_json, decrypt,install
import ast
import os
from time import sleep



def main():
    passcode=input("Please enter your last name, as it appears on linkedin, to begin.\n")
    print(decrypt(ast.literal_eval(read_json(os.path.join(os.getcwd(),'begin.json')),passcode.upper()*3,16)))
    while True:
        if gameloop():
            break

def gameloop():
    print("Here find the incomplete progrm:")
    print(decrypt(ast.literal_eval(read_json(os.path.join(os.getcwd(),'program.json')),"What I thought I'd do was",16)))
    print('\n\n\n\n')
    sleep(5)
    solution=input("Type the line that is missing from this program to make it work.\n")
    if "i quit" in solution.strip().lower():
        print(decrypt(ast.literal_eval(read_json(os.path.join(os.getcwd(),'defeat.json')),solution.strip().lower()*3,16)))
        return(True)
    try:
        xyz=decrypt(ast.literal_eval(read_json(os.path.join(os.getcwd(),'message.json')),solution,16))
        if "Rubik" in xyz:
            print('Congratulations!')
            print(xyz)
            return(True)
    except:
        print("That doesn't look like it. Let's try again.")
        return(False)
        
if __name__=="__main__":
    install('pycryptodome')
    main()