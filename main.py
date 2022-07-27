'''
#1 Ним игра
print(" Перед вами ним-игра. Всего 2021 камушек")
counter=0
summ=2021
while summ>0:
    counter+=1
    if counter%2==0:
        try:
            print("Игрок 2, ход:")
            player2=int(input())
        except TypeError:
            print("Некорректный ввод")
            counter-=1
            continue
        if player2 > 0 and player2 <= 28 and player2 < summ:
            summ=summ-player2
            print("Игрок 2 зарбрал ",player2," камней, осталось ",summ,"камней")
            if summ<=0:
                print("Игрок 2 выйграл")
                break
        else:
            print("Некорректный ввод")
            counter -= 1
            continue
    else:
        try:
            print("Игрок 1, ход:")
            player1 = int(input())
        except TypeError:
            print("Некорректный ввод")
            counter-=1
        if player1 > 0 and player1 <= 28 and player1 < summ:
            summ = summ - player1
            print("Игрок 1 зарбрал ", player1, " камней, осталось ", summ, "камней")
            if summ <= 0:
                print("Игрок 1 выйграл")
                break
        else:
            print("Некорректный ввод")
            counter -= 1
            continue
'''
'''
#1(а,б)Ним игра с ботом
import random
def userMenuChoiceInput():
    while True:
        try:
            print("Введите данные")
            choice = int(input())
        except TypeError:
            print("Некорректный ввод")
            continue
        if choice==1 or choice==2:
            return choice
        elif choice==3:
            choice=random.randint(1, 2)
            return choice
        else:
            print("Некорректный ввод")
            continue
def userChoiceInput(summ):
    while True:
        try:
            print("Введите данные")
            choice = int(input())
        except TypeError:
            print("Некорректный ввод")
            continue
        if choice > 0 and choice <= 28 and choice < summ:
            return choice
        else:
            print("Некорректный ввод")
            continue
print(" Перед вами ним-игра. Всего 2021 камушек")
counter=0
summ=201
print("Кто должен сделать 1 ход "
          "1-Игрок "
          "2-Бот "
          "3-Случайный выбор")
userChoice=userMenuChoiceInput()
while summ>0:
    counter+=1
    if userChoice==1 or counter%2==0:
        print("Игрок, ход:")
        player1 = userChoiceInput(summ)
        summ = summ - player1
        print("Остаток ",summ)
        if summ <= 0:
           print("Игрок выйграл")
           break
    if userChoice==1 or counter%2!=0:
        bot1=0
        if(summ<=28):
            bot1=summ
            summ=summ-
            print("Бот забрал 28 камней")
            print("Бот выйграл")
            break
        elif(summ-28>0):
            if(summ-28>28):
                bot1=random.randint(1,28)
                summ = summ - bot1
            elif(summ-28<28):
                bot1 = random.randint(1, (summ-28))
                summ = summ - bot1
        print("Бот забрал ",bot1," камней. Остаток- ",summ)
'''
''''
#Крестики-Нолики
#-*- coding: utf-8 -*-
def drawPlayField(play_field):
    print ("-------------")
    for i in range(3):
        print ("|", play_field[0+i*3], "|", play_field[1+i*3], "|", play_field[2+i*3], "|")
        print ("-------------")
def inputChoice(player_token):
    while True:
        user_choice=input("Куда поставим " + player_token+"? ")
        try:
            user_choice=int(user_choice)
        except TypeError:
            print("Некорректный ввод")
            continue
        if user_choice>=1 and user_choice<=9:
            if (str(play_field[user_choice - 1]) not in "XO"):
                play_field[user_choice - 1]=player_token
                break
            else:
                print("Не возможно сделать ход на данную позицию, повторите ввод")
                continue
        else:
            print("Некорректный ввод позиции,повторите ввод")
            continue

def checkWin(play_field):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win_coord:
            if play_field[i[0]] == play_field[i[1]] and play_field[i[1]] == play_field[i[2]]:
                return play_field[i[0]]
    return False
def mainGame(play_field):
    counter=0
    while True:
        drawPlayField(play_field)
        if(counter%2==0):
            inputChoice("X")
        else:
            inputChoice("O")
        counter+=1
        if(counter>=5):
            bool_win=checkWin(play_field)
            if(bool_win):
                print(bool_win,"-Выйграл")
                break
        if(counter==9):
            print("Ничья")
            break
    drawPlayField(play_field)

play_field=list(range(1,10))
mainGame(play_field)
'''
'''
#3 RLE-алгоритм для строки
def rleAlg(input_string):
    encoding = ''
    count = 1
    for i in range(len(input_string)):
        if i < len(input_string)-1:
            if input_string[i] == input_string[i + 1]:
                count += 1
            else:
                encoding+=str(count)+input_string[i]
                count = 1
        else:
            encoding += str(count) + input_string[i]
            count = 1
    return encoding
print("Введите строку для RLE- сжатия")
input_string=input()
result=rleAlg(input_string)
print(result)
'''