# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 13:57:23 2022

@author: shabdar
"""

import datetime
def show_game_board():
    
    for i in range(3):
        for j in range(3):
            print(Fore.WHITE + game[i][j], end='\t')
        print()


def chek():
    if game[0][0]== 'X' and game[0][1] == 'X' and game[0][2] == 'X' :
        print("player 1 is wonner")
        exit()  
    if game[0][0]== 'O' and game[0][1] == 'O' and game[0][2] == 'O' :
        print("player 2 is wonner")
        exit()  
    if game[1][0]== 'X' and game[1][1] == 'X' and game[1][2] == 'X' :
        print("player 1 is wonner")
        exit()   
    if game[1][0]== 'O' and game[1][1] == 'O' and game[1][2] == 'O' :
        print("player 2 is wonner")
        exit()
    if game[2][0]== 'X' and game[2][1] == 'X' and game[2][2] == 'X' :
        print("player 1 is wonner")
        exit() 
    if game[2][0]== 'O' and game[2][1] == 'O' and game[2][2] == 'O' :
        print("player 2 is wonner")
        exit()
    if game[0][0]== 'X' and game[1][0] == 'X' and game[2][0] == 'X' :
        print("player 1 is wonner")
        exit()
    if game[0][0]== 'O' and game[1][0] == 'O' and game[2][0] == 'O' :
        print("player 2 is wonner")
        exit() 
    if game[0][1]== 'X' and game[1][1] == 'X' and game[2][1] == 'X' :
        print("player 1 is wonner")
        exit() 
    if game[0][1]== 'O' and game[1][1] == 'O' and game[2][1] == 'O' :
        print("player 2 is wonner")
        exit()
    if game[0][2]== 'X' and game[1][2] == 'X' and game[2][2] == 'X' :
        print("player 1 is wonner")
        exit()  
    if game[0][2]== 'O' and game[1][2] == 'O' and game[2][2] == 'O' :
        print("player 2 is wonner")
        exit()
    if game[0][0]== 'X' and game[1][1] == 'X' and game[2][2] == 'X' :
        print("player 1 is wonner")
        exit() 
    if game[0][0]== 'O' and game[1][1] == 'O' and game[2][2] == 'O' :
        print("player 2 is wonner")
        exit() 
    if game[0][2]== 'X' and game[1][1] == 'X' and game[2][0] == 'X' :
        print("player 1 is wonner")
        exit()
    if game[0][2]== 'O' and game[1][1] == 'O' and game[2][0] == 'O' :
        print("player 2 is wonner")
        exit()

import colorama 
from colorama import Fore, Back, Style                          
a = datetime.datetime.now()


game = [['-','-','-'],
        ['-','-','-'],
        ['-','-','-']]

show_game_board()
    
while True:
    print(Fore.WHITE + "player 1")
    while True:    
        row = int(input(Fore.WHITE + "سطر را وارد کنید:   "))    
        col = int(input(Fore.WHITE + "ستون را وارد کنید:   "))
        if 0<=row<=2 and 0<=col<=2 :
            if  game[row][col] == '-':
        
                game[row][col] = Fore.GREEN +'X'
                break
            else:
                print(Fore.WHITE + "این خانه پر است")
        else:
            print(Fore.WHITE + "شماره سطر و ستون درست نیست")
        
    show_game_board() 
    chek()
        
    print(Fore.WHITE + "player 2")    
    while True:    
        row = int(input(Fore.WHITE + "سطر را وارد کنید:   "))    
        col = int(input(Fore.WHITE + "ستون را وارد کنید:   "))
        if 0<=row<=2 and 0<=col<=2 :
            if  game[row][col] == '-':
        
                game[row][col] = Fore.RED +'O'
                break
            else:
                print(Fore.WHITE + "این خانه پر است")
        else:
            print(Fore.WHITE + "شماره سطر و ستون درست نیست")
    #chek()
    show_game_board()
    chek()
    
b = datetime.datetime.now()
c = b - a
print( int(c.total_seconds() * 1000))     