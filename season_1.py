import time


def begin(name):
    file = open('season_1', 'r', 1)            #File Handling
    line = 1
    while line<= 9:
        text = file.__next__()
        print(text)                            #print text from the file(season_1.txt)
        time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Now there are two possibilities of searching her!!!')
    out = 'What\'s you want to do?\n\t1.meet and investigate her uncle\n\t2.talk to her university friends\n'
    option = input(out)
    check(option,out)


def check(option,out):                             #check the options
    out = out                                      #store the options
    option = option.upper()
    option = option.replace(' ','')                #remove the spaces
    if option == '':
        print ('please enter something')
        option =input(out)
        return check(option,out)
    if option in ('MEET','AND','INVESTIGATE','HER','UNCLE','MEETANDINVESTIGATEHERUNCLE','1'):
        uncle()
    elif option in ('TALK','TO','HER','UNIVERSITY','FRIENDS','TALKTOHERUNIVERSITYFRIENDS','2'):
        university()
    else:
        print('Enter from the given option')
        option = input(out)
        check(option,out)

#meet the uncle
def uncle():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 13:
        text = file.__next__()
        if line >= 10:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Do you want to torture him?\nReply with yes/no')
    out = '\t1.yes\n\t2.no\n'
    option = input(out)
    checker(option,out)


def checker(option,out):                 # checking the option from function(uncle)
    out = out
    option = option.upper()
    option = option.replace(' ','')
    if option == '':
        print ('please enter something')
        option = input(out)
        return checker(option,out)
    if option in ('YES','1'):
        info()
    elif option in ('NO','2'):
        activity()
    else:
        print('Enter from the given option')
        option = input(out)
        checker(option,out)


def info():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 15:
        text = file.__next__()
        if line >= 14:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print ('Do you want to arrest the uncle?(Reply with yes/no)')
    out = '\t1.YES\n\t2.NO\n'
    option = input(out)
    checking(option,out)


def checking(option,out):                       # checking the option from function(info)
    out = out
    option = option.upper()
    option = option.replace(' ','')
    if option == '':
        print ('please enter something')
        option =input(out)
        return checking(option,out)
    if option in ('YES','1'):
        print('You cannot arrest him without any evidence')
    elif option in ('NO','2'):
        print("you investigate about uncle manner with Rosie."
               "People said that uncle love Rosie so much that you realize the innocence of the uncle so the uncle is inclupable.")
    else:
        print('Enter from the given option')
        option = input(out)
        checking(option,out)
    time.sleep(2)
    police_station()


def activity():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 21:
        text = file.__next__()
        if line >= 16:
            print(text)
            time.sleep(1)
        line = line + 1
    print ('You:ok,if you remembered anything about Rosie you can share it.')
    time.sleep(2)
    police_station()

# talk with university friends
def university():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 25:
        text = file.__next__()
        if line >= 22:
            print(text)
            time.sleep(1)
        line = line + 1
    print("Do you want to talk with the Rosie's friends?(Reply in yes/no)")
    out = '\t1.Yes\n\t2.No\n'
    option = input(out)                               # taking input from user
    check_option(option,out)


def check_option(option, out):                        # checking option from function(university)
    out = out
    option = option.upper()
    option = option.replace(' ','')
    if option == '':
        print ('please enter something')
        option =input(out)
        return check_option(option,out)
    if option in ('YES','1'):
        talk()
    elif option in ('NO','2'):
        teacher_talk()
    else:
        print('Enter from the given option')
        option = input(out)
        check_option(option,out)


def talk():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 29:
        text = file.__next__()
        if line >= 26:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    police_station()


def teacher_talk():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 32:
        text = file.__next__()
        if line >= 30:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Do you want to meet Bennet Ahmad?(Reply in Yes/No)')
    out = '\t1.YES\n\t2.NO\n'
    option = input(out)
    option_check(option,out)


def option_check(option,out):                            # checking option from function(teacher_talk)
    out = out
    option = option.upper()
    option =option.replace(' ','')
    if option == '':
        print ('please enter something')
        option =input(out)
        return option_check(option,out)
    if option in ('YES','1'):
        meet_bennet()
    elif option in ('NO','2'):
        police_station()
    else:
        print('Enter from the given option')
        option = input(out)
        option_check(option,out)


def meet_bennet():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 34:
        text = file.__next__()
        if line >=33:
            print(text)
            time.sleep(1)
        line = line + 1
    print ('Do you to investigate more about Bennet?\n(Reply with Yes/No)')
    out = '\t1.yes\n\t2.no\n'
    option = input(out)
    select(option,out)


def select(option,out):                                 # checking the option from function(meet_beent)
    out = out
    option =option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return option_check(option,out)
    if option in ('YES','1'):
        investigate()
    elif option in ('NO','2'):
        police_station()
    else:
        print('Enter from the given option')
        option = input(out)
        select(option, out)


def investigate():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 37:
        text = file.__next__()
        if line >= 35:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    police_station()
#universityfunction ends

#Main story starts
def police_station():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 41:
        text = file.__next__()
        if line >=38:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print ('Now there are two possibilities!!')
    out = '\t1.investigate about the car.\n\t2.meet her family again.\n'
    option = input(out)
    choose_option(option, out)


def choose_option(option, out):                             # checking the option from function(police station)
    out = out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option =input(out)
        return choose_option(option,out)
    if option in ('INVESTIGATE','ABOUT','THE','CAR','INVESTIGATEABOUTTHECAR','1'):
        car()
    elif option in ('MEET','HER','FAMILY','AGAIN','MEETHERFAMILYAGAIN','2'):
        family()
    else:
        print('Enter from the given option')
        option = input(out)
        choose_option(option, out)

#Found Body
def car():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 44:
        text = file.__next__()
        if line >=42:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    family()                                     # function call


def family():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 49:
        text = file.__next__()
        if line >=45:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print ('Do you want to meet Jasper?')
    out = '\t1.yes\n\t2.no\n'
    option = input(out)                                # input from user
    choosing(option, out)


def choosing(option,out):                              # checking the option from function(family)
    out = out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option =input(out)
        return choosing(option,out)
    if option in ('YES','1'):
        meet_jasper()
    elif option in ('NO','2'):
        meet_darren()
    else:
        print('Enter from the given option')
        option = input(out)
        choosing(option, out)


def meet_jasper():                                    # function inside the function(family)
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 56:
        text = file.__next__()
        if line >= 50:
            print(text)
            time.sleep(1)
        line = line + 1                                # printing line by line
    time.sleep(2)
    print ('Do you want to visit the club?')
    out = '\t1.yes\n\t2.no\n'
    option = input(out)
    choice(option, out)


def choice(option, out):                                     # checking the option from function(meet_jasper)
    out = out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option =input(out)
        return choice(option,out)
    if option in ('YES','1'):
        club()
    elif option in ('NO','2'):
        meet_darren()
    else:
        print('Enter from the given option')
        option = input(out)
        choice(option, out)


def club():                                                # function inside the function (meet_jasper)
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 58:
        text = file.__next__()
        if line >=57:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print ('Now what you want?')
    out = '\t1.See cameras recording\n\t2.Investigate the Darren Richmond\n'
    option = input(out)
    selection(option, out)


def selection(option, out):                                      #checking option from function(club)
    out = out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option =input(out)
        return selection(option,out)
    if option in ('SEE','CAMERAS','RECORDING','SEECAMERASRECORDING','1'):
        cameras()
    elif option in ('INVESTIGATE','THE','DARREN','RICHMOND','2'):
        meet_darren()
    else:
        print('Enter from the given option')
        option = input(out)
        selection(option, out)


def cameras():                                              # function inside the function(club)
    file = open('season_1', 'r', 1)                         # read and write the lines from the file
    line = 1
    while line <= 62:
        text = file.__next__()
        if line >=59:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print ('Do you want to meet kris?')
    out = '\t1.yes\n\t2.no\n'
    option = input(out)
    pick(option, out)


def pick(option,out):                                      # checking the option from the function(cameras)
    out = out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option =input(out)
        return pick(option,out)
    if option in ('YES','1'):
        meet_kris()
    elif option in ('NO','2'):
        meet_darren()
    else:
        print('Enter from the given option')
        option = input(out)
        pick(option, out)


def meet_kris():                                       # function inside the function
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 74:
        text = file.__next__()
        if line >= 63:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(3)
    meet_darren()                            # function call

#main suspect
def meet_darren():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 85:
        text = file.__next__()
        if line >=75:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Now What you want?')
    out = '\t1.meet jamie\n\t2.meet gwen\n'
    option = input(out)
    check_1(option,out)


def check_1(option,out):                           # checking the option from the (meet_darren)
    out = out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option =input(out)
        return check_1(option,out)
    if option in ('MEET','JAMIE','MEETJAMIE','1'):
        jamie()
    elif option in ('MEET','GWEN','MEETGWEN','2'):
        gwen()
    else:
        print('Enter from the given option')
        option = input(out)
        check_1(option, out)


def jamie():                                        # function inside the function (meet_darren)
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 93:
        text = file.__next__()
        if line >=86:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(3)
    neighbour()                                       # function call


def gwen():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 102:
        text = file.__next__()
        if line >=94:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(3)
    neighbour()


def neighbour():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 104:
        text = file.__next__()
        if line >=103:
            print(text)
            time.sleep(1)
        line = line + 1
    print('Do you want to meet Belko?')
    out = '\t1.yes\n\t2.no\n'
    option = input(out)
    check_2(option,out)


def check_2(option,out):                             # checking option from the function(neighbour)
   out = out
   option = option.replace(' ','')
   option = option.upper()
   if option == '':
       print ('please enter something')
       option = input(out)
       return check_2(option,out)
   if option in ('YES','1'):
       meet_belko()
   elif option in ('NO','2'):
       meet_aunt()
   else:
        print('Enter from the given option')
        option = input(out)
        check_2(option,out)


def meet_belko():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 114:
        text = file.__next__()
        if line >=105:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(3)
    print('Now what you want?')
    out ="\t1.meet her aunt\n\t2.meet Rosie's family\n"
    option = input(out)
    check_3(option,out)


def check_3(option,out):                             # checking option from the function(meet_belko)
    out=out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_3(option,out)
    if option in ('MEET','HER','AUNT','MEETHERAUNT','1'):
        meet_aunt()
    elif option in ("'MEET','ROSIE'S','FAMILY','MEETROSIE'SFAMILY','2'"):
        meet_family()
    else:
        print('Enter from the given option')
        option = input(out)
        check_3(option,out)


def meet_aunt():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 122:
        text = file.__next__()
        if line >=115:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(3)
    normal()                                 #function call


def meet_family():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 125:
        text = file.__next__()
        if line >=123:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(3)
    normal()


def normal():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 128:
        text = file.__next__()
        if line >=126:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Do want to meet Terry?')
    out = '\t1.yes\n\t2.no\n'
    option = input(out)
    check_4(option,out)


def check_4(option,out):
    out=out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_4(option,out)
    if option in ('YES','1'):
        meet_terry()
    elif option in ('NO','2'):
        exit11()
    else:
        print('Enter from the given option')
        option = input(out)
        check_4(option,out)


def meet_terry():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 136:
        text = file.__next__()
        if line >=129:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Do you want to meet Darren?')
    out = '\t1.yes\n\t2.No\n'
    option = input(out)
    check_5(option,out)


def check_5(option,out):
    out=out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_5(option,out)
    if option in ('YES','1'):
        meet_darren_again()
    elif option in ('NO','2'):
        exit0()
    else:
        print('Enter from the given option')
        option = input(out)
        check_5(option,out)


def meet_darren_again():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 140:
        text = file.__next__()
        if line >=137:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Do you want to meet Gwen?')
    out = '\t1.yes\n\t2.no\n'
    option = input(out)
    check_6(option,out)


def check_6(option,out):
    out=out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_6(option,out)
    if option in ('YES','1'):
        meet_gwen()
    elif option in ('NO','2'):
        exit_2()
    else:
        print('Enter from the given option')
        option = input(out)
        check_6(option,out)


def meet_gwen():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 145:
        text = file.__next__()
        if line >=141:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    CASINO()


def exit0():
    print('You select the wrong option if you met darren then how would you find the murderer')
    print('Game End')
    time.sleep(1000)

def exit_2():
    print('you select the worng option.if you not met gwen then how would you found the muderer')
    print('Game End')
    time.sleep(1000)

def exit11():
    print('You entered the wrong option if you not met terry then how would you find the murderer')
    print('Game END')
    time.sleep(1000)

def CASINO():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 147:
        text = file.__next__()
        if line >=146:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Do you want to see cameras?')
    out = '\t1.yes\n\t2.no\n'
    option = input(out)
    check_7(option,out)


def check_7(option,out):
    out= out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_7(option,out)
    if option in ('YES','1'):
        see_cameras()
    elif option in ('NO','2'):
        exit_3()
    else:
        print('Enter from the given option')
        option = input(out)
        check_7(option,out)


def see_cameras():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 149:
        text = file.__next__()
        if line >=148:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Do you want to arrest Darren?')
    out = '\t1.yes\n\t2.no\n'
    option = input(out)
    check_8(option,out)


def check_8(option,out):
    out= out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_8(option,out)
    if option in ('YES','1'):
        arrest()
    elif option in ('NO','2'):
        exit_4()
    else:
        print('Enter from the given option')
        option = input(out)
        check_8(option,out)


def arrest():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 152:
        text = file.__next__()
        if line >=150:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Do you want to torture him')
    out = '\t1.yes\n\t2.no\n'
    option = input(out)
    check_9(option,out)


def check_9(option,out):
    out= out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_9(option,out)
    if option in ('YES','1'):
        torture()
    elif option in ('NO','2'):
        information()
    else:
        print('Enter from the given option')
        option = input(out)
        check_9(option,out)


def torture():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 154:
        text = file.__next__()
        if line >=153:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    information()


def information():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 158:
        text = file.__next__()
        if line >=155:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    casino()


def exit_4():
    print('You select the wrong option darren is a clear suspect then why you not arreest the darren')
    print('You are Playing so bad.\n GAME END')
    time.sleep(1000)

def exit_3():
    print('You select the wrond option is you not see the cameras recording then how would you found the murderer')
    print('GAME END')
    time.sleep(1000)

def casino():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 161:
        text = file.__next__()
        if line >= 159:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Now what you want?')
    out = '\t1.see cameras recording again\n\t2.go to the upper floor\n'
    option = input(out)
    check_10(option,out)


def check_10(option,out):
    out= out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_10(option,out)
    if option in ('SEE','CAMERAS','RECORDING','AGAIN','SEECAMERASRECORDINGAGAIN','1'):
        cameras_recording()
    elif option in ('GO','TO','THE','UPPER','FLOOR','GOTOTHEUPPERFLOOR','2'):
        upper_floor()
    else:
        print('Enter from the given option')
        option = input(out)
        check_10(option,out)


def cameras_recording():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 163:
        text = file.__next__()
        if line >=162:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    upper_floor()


def upper_floor():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 166:
        text = file.__next__()
        if line >=164:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Do you want to meet Gwen?')
    out = '\t1.yes\n\t2.no\n'
    option = input(out)
    check_11(option,out)


def check_11(option,out):
    out= out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_11(option,out)
    if option in ('YES','1'):
        meet_gwen_again()
    elif option in ('NO','2'):
        exit_5()
    else:
        print('Enter from the given option')
        option = input(out)
        check_11(option,out)


def meet_gwen_again():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 174:
        text = file.__next__()
        if line >= 167:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Do you want to meet casino owner?')
    out = '\t1.yes\n\t2.no\n'
    option = input(out)
    check_12(option,out)


def check_12(option,out):
    out= out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_12(option,out)
    if option in ('YES','1'):
        meet_jackson()
    elif option in ('NO','2'):
        exit_6()
    else:
        print('Enter from the given option')
        option = input(out)
        check_12(option,out)


def meet_jackson():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 183:
        text = file.__next__()
        if line >= 175:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Now what you want?')
    out = '\t1.meet terry again\n\t2.meet her friends\n'
    option = input(out)
    check_13(option,out)


def check_13(option,out):
    out=out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_13(option,out)
    if option in ('MEET','TERRY','AGAIN','MEETTERRYAGAIN','1'):
        meet_terry_again()
    elif option in ('MEET','HER','FRIENDS','MEETHERFRIENDS','2'):
        meet_friends()
    else:
        print('Enter from the given option')
        option = input(out)
        check_13(option,out)


def meet_terry_again():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 188:
        text = file.__next__()
        if line >= 184:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Do you want to meet Ames?')
    out = '\t1.yes\n\t2.no\n'
    option = input(out)
    check_14(option,out)


def check_14(option,out):
    out= out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_14(option,out)
    if option in ('YES','1'):
        meet_ames()
    elif option in ('NO','2'):
        meet_friends()
    else:
        print('Enter from the given option')
        option = input(out)
        check_14(option,out)


def meet_ames():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 195:
        text = file.__next__()
        if line >= 189:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Do you want to release the darren from jail?')
    out = '\t1.yes\n\t2.no\n'
    option = input(out)
    check_15(option,out)


def check_15(option,out):
    out= out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_15(option,out)
    if option in ('YES','1'):
        release()
    elif option in ('NO','2'):
        meet_friends()
    else:
        print('Enter from the given option')
        option = input(out)
        check_15(option,out)


def release():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 198:
        text = file.__next__()
        if line >= 196:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    meet_friends()


def meet_friends():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 205:
        text = file.__next__()
        if line >= 199:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Do you want to meet jasper again?')
    out = '\t1.yes\n\t2.no'
    option = input(out)
    check_16(option,out)


def check_16(option,out):
    out= out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_16(option,out)
    if option in ('YES','1'):
        jasper()
    elif option in ('NO','2'):
        uncle_dead()
    else:
        print('Enter from the given option')
        option = input(out)
        check_16(option,out)


def jasper():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 211:
        text = file.__next__()
        if line >= 206:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    uncle_dead()


def uncle_dead():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 218:
        text = file.__next__()
        if line >= 212:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Now what you want?')
    out = '\t1.arrest belko\n\t2.invesitage the belko\n'
    option = input(out)
    check_17(option,out)


def check_17(option,out):
    out = out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_17(option,out)
    if option in ('ARREST','BELKO','ARRESTBELKO','1'):
        print("You cannot arrest him without any investigation")
        time.sleep(2)
        investigate_belko()
    elif option in ('INVESTIGATE','THE','BELKO','INVESTIGATETHEBELKO','2'):
        investigate_belko()
    else:
        print('Enter from the given option')
        option = input(out)
        check_17(option,out)


def investigate_belko():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 224:
        text = file.__next__()
        if line >= 219:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Do you want to see the license of the gun?')
    out = '\t1.yes\n\t2.no\n'
    option = input(out)
    check_18(option,out)


def check_18(option,out):
    out = out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_18(option,out)
    if option in ('YES','1'):
        license()
    elif option in ('NO','2'):
        outside()
    else:
        print('Enter from the given option')
        option = input(out)
        check_18(option,out)


def license():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 227:
        text = file.__next__()
        if line >= 225:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    outside()


def exit_6():
    print('You select the wrong option if you not meet jackson then how would you found the murderer.\nYou are not a good detective.')
    print('Game End')
    time.sleep(1000)


def exit_5():
    print('You select the wrong option if you not meet gwen then how would you found the murderer.\nYou are not a good detective.')
    print('Game End')
    time.sleep(1000)

def outside():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 232:
        text = file.__next__()
        if line >= 228:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Now what you want?')
    out = '\t1.meet her brother\n\t2.meet darren'
    option = input(out)
    check_19(option,out)


def check_19(option,out):
    out = out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_19(option,out)
    if option in ('MEET','HER','BROTHER','MEETHERBROTHER','1'):
        meet_brother()
    elif option in ('MEET','DARREN','2'):
        darren()
    else:
        print('Enter from the given option')
        option = input(out)
        check_19(option,out)


def meet_brother():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 235:
        text = file.__next__()
        if line >= 233:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Do you want to meet jasper?')
    out ='\t1.yes\n\t2.no\n'
    option= input(out)
    check_20(option,out)


def check_20(option,out):
    out = out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_20(option,out)
    if option in ('YES','1'):
        meet_jasper_again()
    elif option in ('NO','2'):
        darren()
    else:
        print('Enter from the given option')
        option = input(out)
        check_20(option,out)


def meet_jasper_again():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 241:
        text = file.__next__()
        if line >= 236:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    darren()


def darren():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 244:
        text = file.__next__()
        if line >= 242:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Do you want to meet jamie?')
    out = '\t1.yes\n\t2.no\n'
    option = input(out)
    check_21(option,out)


def check_21(option,out):
    out = out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_21(option,out)
    if option in ('YES','1'):
        meet_jamie()
    elif option in ('NO','2'):
        other()
    else:
        print('Enter from the given option')
        option = input(out)
        check_21(option,out)


def meet_jamie():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 250:
        text = file.__next__()
        if line >= 245:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    other()


def other():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 252:
        text = file.__next__()
        if line >= 251:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Now whom do you want to investigate?')
    out = '\t1.Darren\n\t2.Terry\n\t3.Gwen\n\t4.Ames\n\t5.Jamie\n'
    option = input(out)
    check_22(option,out)


def check_22(option,out):
    out = out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_22(option,out)
    if option in ('DARREN','1'):
        darren_meeting()
    elif option in ('TERRY','2'):
        terry_meeting()
    elif option in ('GWEN','3'):
        gwen_meeting()
    elif option in ('AMES','4'):
        ames_meeting()
    elif option in ('JAMIE','5'):
        jamie_meeting()
    else:
        print('Enter from the given option')
        option = input(out)
        check_22(option,out)


def darren_meeting():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 252:
        text = file.__next__()
        if line >= 251:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    attack()

def terry_meeting():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 263:
        text = file.__next__()
        if line >= 258:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    attack()


def gwen_meeting():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 268:
        text = file.__next__()
        if line >= 264:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    attack()


def ames_meeting():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 273:
        text = file.__next__()
        if line >= 269:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    attack()


def jamie_meeting():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 278:
        text = file.__next__()
        if line >= 274:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    attack()


def attack():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 284:
        text = file.__next__()
        if line >= 279:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Do you want yo meet darren?')
    out = '\t1.yes\n\t2.no'
    option = input(out)
    check_23(option,out)


def check_23(option,out):
    out = out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_23(option,out)
    if option in ('YES','1'):
        DARREN()
    elif option in ('NO','2'):
        exit_7()
    else:
        print('Enter from the given option')
        option = input(out)
        check_23(option,out)


def DARREN():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 289:
        text = file.__next__()
        if line >= 285:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Do you want torture him?')
    out = '\t1.yes\n\t2.no'
    option = input(out)
    check_24(option,out)


def check_24(option,out):
    out = out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_24(option,out)
    if option in ('YES','1'):
        truth()
    elif option in ('NO','2'):
        keep()
    else:
        print('Enter from the given option')
        option = input(out)
        check_24(option,out)


def truth():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 291:
        text = file.__next__()
        if line >= 290:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    Camera()

def keep():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 293:
        text = file.__next__()
        if line >= 292:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    Camera()


def exit_7():
    print('You select the worng option.If you not meet the darren then how would you solve the case.You are not a good detective')
    print('GAME END')
    time.sleep(1000)


def Camera():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 295:
        text = file.__next__()
        if line >= 294:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Do you want to arrest terry?')
    out = '\t1.Yes\n\t2.no'
    option = input(out)
    check_25(option,out)


def check_25(option,out):
    out = out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_25(option,out)
    if option in ('YES','1'):
        arrest_terry()
    elif option in ('NO','2'):
        exit_8()
    else:
        print('Enter from the given option')
        option = input(out)
        check_25(option,out)


def arrest_terry():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 300:
        text = file.__next__()
        if line >= 296:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('Whom do you want to arrest and torture')
    out = '\t1.Jackson\n\t2.Jamie\n\t3.Ames\n'
    option = input(out)
    check_26(option,out)


def check_26(option,out):
    out = out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_26(option,out)
    if option in ('JACKSON','1'):
        arrest_jackson()
    elif option in ('JAMIE','2'):
        arrest_jamie()
    elif option in ('AMES','3'):
        arrest_ames()
    else:
        print('Enter from the given option')
        option = input(out)
        check_26(option,out)


def arrest_jackson():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 303:
        text = file.__next__()
        if line >= 301:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    arrest_ames()


def arrest_jamie():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 309:
        text = file.__next__()
        if line >= 307:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    murderer()


def arrest_ames():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 306:
        text = file.__next__()
        if line >= 304:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    arrest_jamie()


def murderer():
    file = open('season_1', 'r', 1)
    line = 1
    while line <= 320:
        text = file.__next__()
        if line >= 310:
            print(text)
            time.sleep(1)
        line = line + 1
    time.sleep(2)
    print('After the whole investigation who was the main murderer?')
    out = '\t1.terry\n\t2.Jamie\n\t3.jackson\n\t4.Ames'
    option = input(out)
    check_27(option,out)


def check_27(option,out):
    out = out
    option = option.replace(' ','')
    option = option.upper()
    if option == '':
        print ('please enter something')
        option = input(out)
        return check_27(option,out)
    if option in ('TERRY','1'):
        print('WELLDONE!!!\nYou find out the murderer.Police arrest the Terry.Court punished her to spent her remaining life in the jail\nGAME END.')
        time.sleep(1000)
    elif option in ('JAMIE','2'):
        print('WELLDONE!!!\nYou find out the murderer.Police arrest the Jamie.Court punished him to spent his remaining life in the jail\nGAME END.')
        time.sleep(10000)
    elif option in ('JACKSON','3'):
        print('Sorry!!!Jackson is not the murderer.He is only present in the meeting but not involved in the murderer.\nYou are not a good detective\nGAME END.')
        time.sleep(1000)
    elif option in ('AMES','4'):
        print('SORRY!!!Ames is not the murderer.He is only present in the meeting but not involved in the murderer.\nYou are not a good detective\nGAME END  ')
        time.sleep(1000)
    else:
        print('Enter from the given option')
        option = input(out)
        check_27(option,out)


def exit_8():
    print('You select the wrong option if you not arrest terry then how would you solve the case')
    print('GAME END')
    time.sleep(1000)
