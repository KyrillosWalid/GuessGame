#####2GGAME#####
import random
xve = int(random.randint(0,10))
xe = int(random.randint(0,100))
xm = int(random.randint(0,1000))
xd = int(random.random() * 100)
mxvd = xve + 0.6 + xe + 0.4 + xm + 0.02 + xd + 0.04
xvd = float(random.randint(0,1000) + random.randint(0,1000) + mxvd)
print("**********************************************************")
print("* THIS CODE BY KOKADEV...KYRILLOSWALIDRADI               *")
print("* ALL COPYRIGHYS ARE SAVED TO KYRILLOSWALIDRADI          *")
print("* + 2 0 1 0 6 2 7 0 4 4 1 3 - + 2 0 1 2 1 1 2 8 0 3 5 8  *")
print("* KYRILLOSWALIDRADI@HOTMAIL.COM                          *")
print("* WWW.FACEBOOK.COM/KOKADEV                               *")
print("*  WWW.GITHUB.COM/KOKADev                                *")
print("**********************************************************")
print("==========================================================")
print("╔═══╦╗ ╔╦═══╦═══╦═══╗    ╔═══╦═══╦═╗╔═╦═══╗")
print("║╔═╗║║ ║║╔══╣╔═╗║╔═╗║    ║╔═╗║╔═╗║║╚╝║║╔══╝")
print("║║─╚╣║ ║║╚══╣╚══╣╚══╗    ║║─╚╣║─║║╔╗╔╗║╚══╗")
print("║║╔═╣║ ║║╔══╩══╗╠══╗║╔══╗║║╔═╣╚═╝║║║║║║╔══╝")
print("║╚╩═║╚═╝║╚══╣╚═╝║╚═╝║╚══╝║╚╩═║╔═╗║║║║║║╚══╗")
print("╚═══╩═══╩═══╩═══╩═══╝    ╚═══╩╝ ╚╩╝╚╝╚╩═══╝")
print("")
t=0
def vegame():
    print("Guess what the right number is :)")
    print("")
    while True:
        try:
            y = int(input(""))
        except Exception:
            print("Erorr : Enter Valid Number.")
            vegame()
        global t
        t= t+1
        if(xve>y):
            print("")
            print("Higher")
            print("")
        if(xve<y):
            print("")
            print("Lower")
            print("")
        if(t==5):
            print("Do you want help ?")
            print("y/n")
            try:
                h = input("")
            except Exception:
                print("Erorr : Enter y or n only")
                break
            if(h=="y"):
                print("Number between 0 and 10")
            if(h=="n"):
                print("Okey... Guess!")
        if(xve == y):
            print("Congratulations! You guessed the right number :D")
            print("After {}".format(t),"tries")
            s = xve - t
            print("Your score is : {}".format(s))

            print("**********************************************************")
            print("* THIS CODE BY KOKADEV...KYRILLOSWALIDRADI               *")
            print("* ALL COPYRIGHYS ARE SAVED TO KYRILLOSWALIDRADI          *")
            print("* + 2 0 1 0 6 2 7 0 4 4 1 3 - + 2 0 1 2 1 1 2 8 0 3 5 8  *")
            print("* KYRILLOSWALIDRADI@HOTMAIL.COM                          *")
            print("* WWW.FACEBOOK.COM/KOKADEV                               *")
            print("  WWW.GITHUB.COM/KOKADev                                 *")
            print("**********************************************************")

            break

def egame():
    print("Guess what the right number is :)")
    print("")
    while True:
        try:
            y = int(input(""))
        except Exception:
            print("Erorr : Enter Valid Number.")
            egame()
        global t
        t= t+1
        if(xe>y):
            print("")
            print("Higher")
            print("")
        if(xe<y):
            print("")
            print("Lower")
            print("")
        if(t==10):
            print("Do you want help ?")
            print("y/n")
            try:
                h = input("")
            except Exception:
                print("Erorr : Enter y or n only")
                break
            if(h=="y"):
                print("Number between 0 and 100")
            if(h=="n"):
                print("Okey... Guess!")
        if(xe == y):
            print("")
            print("Congratulations! You guessed the right number :D")
            print("After {}".format(t),"tries")
            s = xe*2 - t
            print("Your score is : {}".format(s))
            print("**********************************************************")
            print("* THIS CODE BY KOKADEV...KYRILLOSWALIDRADI               *")
            print("* ALL COPYRIGHYS ARE SAVED TO KYRILLOSWALIDRADI          *")
            print("* + 2 0 1 0 6 2 7 0 4 4 1 3 - + 2 0 1 2 1 1 2 8 0 3 5 8  *")
            print("* KYRILLOSWALIDRADI@HOTMAIL.COM                          *")
            print("* WWW.FACEBOOK.COM/KOKADEV                               *")
            print("  WWW.GITHUB.COM/KOKADev                                 *")
            print("**********************************************************")
            break

def mgame():
    print("Guess what the right number is :)")
    print("")
    while True:
        try:
            y = int(input(""))
        except Exception:
            print("Erorr : Enter Valid Number.")
            mgame()
        global t
        t= t+1
        if(xm>y):
            print("")
            print("Higher")
            print("")
        if(xm<y):
            print("")
            print("Lower")
            print("")
        if(t==20):
            print("Do you want help ?")
            print("y/n")
            try:
                h = input("")
            except Exception:
                print("Erorr : Enter y or n only")
                break
            if(h=="y"):
                print("Number between 0 and 1000")
            if(h=="n"):
                print("Okey... Guess!")
        if(xm == y):
            print("")
            print("Congratulations! You guessed the right number :D")
            print("After {}".format(t),"tries")
            s = xm*3 - t
            print("Your score is : {}".format(s))
            print("**********************************************************")
            print("* THIS CODE BY KOKADEV...KYRILLOSWALIDRADI               *")
            print("* ALL COPYRIGHYS ARE SAVED TO KYRILLOSWALIDRADI          *")
            print("* + 2 0 1 0 6 2 7 0 4 4 1 3 - + 2 0 1 2 1 1 2 8 0 3 5 8  *")
            print("* KYRILLOSWALIDRADI@HOTMAIL.COM                          *")
            print("* WWW.FACEBOOK.COM/KOKADEV                               *")
            print("  WWW.GITHUB.COM/KOKADev                                 *")
            print("**********************************************************")
            break

def dgame():
    print("Guess what the right number is :)")
    print("")
    while True:
        try:
            y = int(input(""))
        except Exception:
            print("Erorr : Enter Valid Number.")
            dgame()
        global t
        t= t+1
        if(xd>y):
            print("")
            print("Higher")
            print("")
        if(xd<y):
            print("")
            print("Lower")
            print("")
        if(t==25):
            print("Do you want help ?")
            print("y/n")
            try:
                h = input("")
            except Exception:
                print("Erorr : Enter y or n only")
                break
            if(h=="y"):
                print("Number between 0 and All numbers!")
            if(h=="n"):
                print("Okey... Guess!")
        if(xd == y):
            print("")
            print("Congratulations! You guessed the right number :D")
            print("After {}".format(t),"tries")
            s = xd*4 - t
            print("Your score is : {}".format(s))
            print("**********************************************************")
            print("* THIS CODE BY KOKADEV...KYRILLOSWALIDRADI               *")
            print("* ALL COPYRIGHYS ARE SAVED TO KYRILLOSWALIDRADI          *")
            print("* + 2 0 1 0 6 2 7 0 4 4 1 3 - + 2 0 1 2 1 1 2 8 0 3 5 8  *")
            print("* KYRILLOSWALIDRADI@HOTMAIL.COM                          *")
            print("* WWW.FACEBOOK.COM/KOKADEV                               *")
            print("  WWW.GITHUB.COM/KOKADev                                 *")
            print("**********************************************************")
            break

def vdgame():
    print("Guess what the right number is :)")
    print("")
    while True:
        try:
            y = int(input(""))
        except Exception:
            print("Erorr : Enter Valid Number.")
            vdgame()
        global t
        t= t+1
        if(xvd>y):
            print("")
            print("Higher")
            print("")
        if(xvd<y):
            print("")
            print("Lower")
            print("")
        if(t==20):
            print("Do you want help ?")
            print("y/n")
            try:
                h = input("")
            except Exception:
                print("Erorr : Enter y or n only")
                break
            if(h=="y"):
                print("Number has a decimal.")
            if(h=="n"):
                print("Okey... Guess!")
        if(t==35):
            print("Do you want help ?")
            print("y/n")
            try:
                h = input("")
            except Exception:
                print("Erorr : Enter y or n only")
                break
            if(h=="y"):
                print("The decimal is 0.6")
            if(h=="n"):
                print("Okey... Guess!")
        if(xvd == y):
            print("")
            print("Congratulations! You guessed the right number :D")
            print("After {}".format(t),"tries")
            s = vde*5 - t
            print("Your score is : {}".format(s))
            print("**********************************************************")
            print("* THIS CODE BY KOKADEV...KYRILLOSWALIDRADI               *")
            print("* ALL COPYRIGHYS ARE SAVED TO KYRILLOSWALIDRADI          *")
            print("* + 2 0 1 0 6 2 7 0 4 4 1 3 - + 2 0 1 2 1 1 2 8 0 3 5 8  *")
            print("* KYRILLOSWALIDRADI@HOTMAIL.COM                          *")
            print("* WWW.FACEBOOK.COM/KOKADEV                               *")
            print("  WWW.GITHUB.COM/KOKADev                                 *")
            print("**********************************************************")
            break


def start():
    print("Choose the difficulty : ")
    print("1. VeryEasy")
    print("2. Easy")
    print("3. Medium")
    print("4. Hard")
    print("5. VeryHard")
    try:
        c =  int(input(""))
    except Exception:
        print("Erorr : Enter Valid Number.")
    if(c>5):
        print("ERORR: Choose a difficulty from the list.")
    if(c<1):
        print("ERORR: Choose a difficulty from the list.")
    if(c==1):
        vegame()
    if(c==2):
        egame()
    if(c==3):
        mgame()
    if(c==4):
        dgame()
    if(c==5):
        vdgame()
start()
