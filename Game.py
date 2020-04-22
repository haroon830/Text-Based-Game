import os
import time
import season_1


print('\n\n\n\n\n\t\t\t\t\tWelcome TO Death Behind the Back')
time.sleep(2)
os.system('cls')

#menubar function
print('Hello')
def menu():
    start = '\n\n\t\t1.play game\n\t\t2.exit\n'
    select = input(start)
    check (select,start)


def check(select,start):
    start = start
    select = select.replace(' ','')
    select = select.upper()
    start = start
    if select == '':
        print('Enter something.')
        select = input(start)
        return check(select,start)
    if select in ('PLAY','GAME','PLAYGAME','1'):
        play_game()
    elif select in ('EXIT','2'):
        exit()
    else:
        print('Enter correct option')
        select = input(start)
        check(select,start)


def play_game():
    print('First enter the name of your detective')
    name = input('Enter your name:')
    season_1.begin(name)


def exit():
    print('Game End')
    os.system('pause')
    return 0

menu()

