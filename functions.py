#По моей части уже
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
a=[]
f=[]
s=[]
megacheck=0
d=0
n=0
h=0
dblchk=0
num1=0
y=0
floatcheck=0
b=0
chk=0
g=0
def test():
    msg = messagebox.showinfo("Info", "Testing")


def addup1():
    global g, u
    a.append(1)
    g=0
    for i in a:
        u = i / 10
        g = (g + u) * 10
    print(g)
def addup2():
    global g, u
    a.append(2)
    g=0
    for i in a:
        u = i / 10
        g = (g + u) * 10
    print(g)
def addup3():
    global g, u
    a.append(3)
    g=0
    for i in a:
        u = i / 10
        g = (g + u) * 10
    print(g)
def addup4():
    global g, u
    a.append(4)
    g=0
    for i in a:
        u = i / 10
        g = (g + u) * 10
    print(g)
def addup5():
    global g, u
    a.append(5)
    g=0
    for i in a:
        u = i / 10
        g = (g + u) * 10
    print(g)
def addup6():
    global g, u
    g=0
    a.append(6)
    for i in a:
        u = i / 10
        g = (g + u) * 10
    print(g)
def addup7():
    global g, u
    g=0
    a.append(7)
    for i in a:
        u = i / 10
        g = (g + u) * 10
    print(g)
def addup8():
    global g, u
    g=0
    a.append(8)
    for i in a:
        g+=str(i)
    print(int(g))
def addup9():
    global g, u
    g=0
    a.append(9)
    for i in a:
        u = i / 10
        g = (g + u) * 10
    print(g)
def addup0():
    global g, u
    g=0
    a.append(0)
    for i in a:
        u = i / 10
        g = (g + u) * 10
    print(g)

def testaddupA():
    global b, u, y, flt
    a.append('A')
def testaddupB():
    global b, u, y, flt
    a.append('B')
def testaddupC():
    global b, u, y, flt
    a.append('C')
def testaddupD():
    global b, u, y, flt
    a.append('D')
def testaddupE():
    global b, u, y, flt
    a.append('E')
def testaddupF():
    global b, u, y, flt
    a.append('F')

def bstoreplus():
    global g, num1, chk, a
    for i in range(100):
        print(' ')
    if chk==0 or chk==2 or chk==3:
        print(num1)
        num1+=g
        print('+')
        g=0
    elif chk==1:
        num1-=g
        print(num1)
        g=0
        print('+')
    elif chk==4:
        num1*=g
        print(num1)
        print('+')
        g=0
    a=[]
    chk=2


def bmin():
    global num1, chk, g, a
    for i in range(100):
        print(' ')
    if chk==2:
        print(num1+g)
        g=0
        print('-')
    elif chk==1:
        num1=num1-g
        print(num1)
        print('-')
        g=0
    elif chk==3:
        print(num1)
        print('-')
        g=0
    elif chk==0:
        print(g)
        print('-')
        num1=g
        g=0
    elif chk==4:
        num1*=g
        print(num1)
        print('-')
        g=0
    a=[]
    chk=1


def equal():
    global g, num1, chk, flt, a
    for i in range(100):
        print(' ')
    if chk==1:
        num1=num1-g
        print(num1+g)
        print('-')
        print(g)
        print('=')
        print(num1)
        print('----')
    elif chk==2:
        num1 = num1 + g
        print(num1 - g)
        print('+')
        print(g)
        print('=')
        print(num1)
        print('----')
    elif chk==3:
        print(num1)
    elif chk==4:
        print(num1)
        print('*')
        print(g)
        print('=')
        num1*=g
        print(num1)
        print('----')
        g=0
    elif chk==5 and g!=0:
        print(num1)
        print('/')
        print(g)
        print('=')
        num1/=g
        print(num1)
        print('----')
        g=0
    elif g==0 and chk!=5:
        print('=')
        print(g)
        print('----')
        num1=g
    elif chk==5 and g==0:
        g=1
        print(num1)
        print('/')
        print(1)
        print('=')
        num1 /= g
        print(num1)
        print('----')
        g = 0
    else:
        print('=')
        print(g)
        print('----')
        num1=g
    chk=3
    a=[]

def backspace():
    global a
    if len(a)>0:
        a.pop()
        g=0
        for i in a:
            u = i / 10
            g = (g + u) * 10
        print(g)
def floatb():
    global g
    global floatcheck
    floatcheck=1
def tm():
    global num1, g, a, chk
    for i in range(100):
        print(' ')
    if chk==0:
        num1=g
        print(g)
        print('*')
        g=0
    elif chk==1:
        num1=num1-g
        print(num1)
        print('*')
        g=0
    elif chk==2:
        num1+=g
        print(num1)
        print('*')
        g=0
    elif chk==3:
        print(num1)
        print('*')
        g=0
    elif chk==4:
        num1*=g
        print(num1)
        print('*')
        g=0
    elif chk == 5:
        num1 /= g
        print(num1)
        print('/')
        g = 0
    chk=4
    a=[]
def dv():
    global num1, g, a, chk, n

    for i in range(100):
        print(' ')
    if chk == 0:
        num1 = g
        print(g)
        print('/')
    elif chk == 1:
        num1 = num1 - g
        print(num1)
        print('/')
        g = 0
    elif chk == 2:
        num1 += g
        print(num1)
        print('/')
        g = 0
    elif chk == 3:
        print(num1)
        print('/')
        g = 0
    elif chk == 4:
        num1 *= g
        print(num1)
        print('/')
        g = 0
    elif chk == 5:
        num1 /= g
        print(num1)
        print('/')
        g = 0
    elif chk == 5 and g==0:
        g=1
        num1 /= g
        print(num1)
        print('/')
        g = 0
    elif megacheck==1:
        s=''
        while g>0:
            s=str(g%n)
            g//=n
        return s
    chk = 5
    a=[]
def ac():
    global num1, b, y, floatcheck, u, e, r, flt, chk, g, a, q, e, r, s, h, y, l, p
    num1=0
    b=0
    y=0
    floatcheck=0
    u=0
    flt=0
    chk=0
    g=0
    h=0
    y=0
    l=0
    p=0
    q=[]
    e=[]
    r=[]
    s=[]
    a=[]
    for i in range(100):
        print(' ')


#First night - код в 273 строки...

#GUI update - 427!!

#Func update - 525   0_0

#HOF update - 354

#
# 0 - base, AC
# 1 - minus
# 2 - plus
# 3 - equal
# 4 - times
# 5 - division
#
#442...


# Variables
dblchk = 0
win = Tk()
win.title('Калькулятор Сс v0.5.0')
win.iconbitmap(default="CalculatorCc.ico")
win.geometry('283x400')
win.resizable(False, False)
def Cc():
    global dblchk, g, a, chk
    if dblchk == 1:
        b0['command'] = addup0
        b1['command'] = addup1
        b2['command'] = addup2
        b3['command'] = addup3
        b4['command'] = addup4
        b5['command'] = addup5
        b6['command'] = addup6
        b7['command'] = addup7
        b8['command'] = addup8
        b9['command'] = addup9
        bParenthesis1['command'] = test
        bParenthesis2['command'] = test
        bDivision['command'] = dv
        bMultiply['command'] = tm
        bMinus['command'] = bmin
        bPlus['command'] = bstoreplus
        bEqual['command'] = equal
        b0['text'] = '0'
        bParenthesis1['text'] = '('
        bParenthesis2['text'] = ')'
        bDivision['text'] = '/'
        bMultiply['text'] = '*'
        bMinus['text'] = '-'
        bPlus['text'] = '+'
        bEqual['text'] = '='
        b0['state'] = DISABLED
        b1['state'] = DISABLED
        b2['state'] = DISABLED
        b3['state'] = DISABLED
        b4['state'] = DISABLED
        b5['state'] = DISABLED
        b6['state'] = DISABLED
        b7['state'] = DISABLED
        b8['state'] = DISABLED
        b9['state'] = DISABLED
        bA['state'] = DISABLED
        bB['state'] = DISABLED
        bC['state'] = DISABLED
        bD['state'] = DISABLED
        bE['state'] = DISABLED
        bF['state'] = DISABLED
        bParenthesis2['state'] = DISABLED
        bParenthesis1['state'] = DISABLED
        bDivision['state'] = NORMAL
        bMultiply['state'] = NORMAL
        bMinus['state'] = NORMAL
        bPlus['state'] = NORMAL
        bEqual['state'] = NORMAL
        bAC['state'] = NORMAL
        bBackspace['state'] = NORMAL
        dblchk = 0
        chk = 0
    elif dblchk == 0:
        b0['command'] = nreset
        b2['command'] = nset2
        b3['command'] = nset3
        b4['command'] = nset4
        b5['command'] = nset5
        b6['command'] = nset6
        b7['command'] = nset7
        b8['command'] = nset8
        b9['command'] = nset9
        bParenthesis1['command'] = nset10
        bParenthesis2['command'] = nset11
        bDivision['command'] = nset12
        bMultiply['command'] = nset13
        bMinus['command'] = nset14
        bPlus['command'] = nset15
        bEqual['command'] = nset16
        b0['text'] = 'Reset'
        bParenthesis1['text'] = '10'
        bParenthesis2['text'] = '11'
        bDivision['text'] = '12'
        bMultiply['text'] = '13'
        bMinus['text'] = '14'
        bPlus['text'] = '15'
        bEqual['text'] = '16'
        b0['state'] = NORMAL
        b1['state'] = DISABLED
        b2['state'] = NORMAL
        b3['state'] = NORMAL
        b4['state'] = NORMAL
        b5['state'] = NORMAL
        b6['state'] = NORMAL
        b7['state'] = NORMAL
        b8['state'] = NORMAL
        b9['state'] = NORMAL
        bA['state'] = DISABLED
        bB['state'] = DISABLED
        bC['state'] = DISABLED
        bD['state'] = DISABLED
        bE['state'] = DISABLED
        bF['state'] = DISABLED
        bParenthesis1['state'] = NORMAL
        bParenthesis2['state'] = NORMAL
        bDivision['state'] = NORMAL
        bMultiply['state'] = NORMAL
        bMinus['state'] = NORMAL
        bPlus['state'] = NORMAL
        bEqual['state'] = NORMAL
        bAC['state'] = DISABLED
        bBackspace['state'] = DISABLED
        chk = 0
        dblchk = 1
    win.update_idletasks()
def nset2():
    global n, megacheck
    n=2
    b0['command'] = addup0
    b1['command'] = addup1
    b2['command'] = addup2
    b3['command'] = addup3
    b4['command'] = addup4
    b5['command'] = addup5
    b6['command'] = addup6
    b7['command'] = addup7
    b8['command'] = addup8
    b9['command'] = addup9
    bParenthesis1['command'] = test
    bParenthesis2['command'] = test
    bDivision['command'] = dv
    bMultiply['command'] = tm
    bMinus['command'] = bmin
    bPlus['command'] = bstoreplus
    bEqual['command'] = equal
    b0['text'] = '0'
    bParenthesis1['text'] = '('
    bParenthesis2['text'] = ')'
    bDivision['text'] = '/'
    bMultiply['text'] = '*'
    bMinus['text'] = '-'
    bPlus['text'] = '+'
    bEqual['text'] = '='
    b0['state'] = NORMAL
    b1['state'] = NORMAL
    b2['state'] = DISABLED
    b3['state'] = DISABLED
    b4['state'] = DISABLED
    b5['state'] = DISABLED
    b6['state'] = DISABLED
    b7['state'] = DISABLED
    b8['state'] = DISABLED
    b9['state'] = DISABLED
    bA['state'] = DISABLED
    bB['state'] = DISABLED
    bC['state'] = DISABLED
    bD['state'] = DISABLED
    bE['state'] = DISABLED
    bF['state'] = DISABLED
    bParenthesis2['state'] = DISABLED
    bParenthesis1['state'] = DISABLED
    bDivision['state'] = NORMAL
    bMultiply['state'] = NORMAL
    bMinus['state'] = NORMAL
    bPlus['state'] = NORMAL
    bEqual['state'] = NORMAL
    bAC['state'] = NORMAL
    bBackspace['state'] = NORMAL
    megacheck=1
    ac()
def nset3():
    global n, megacheck
    n=3
    b0['command'] = addup0
    b1['command'] = addup1
    b2['command'] = addup2
    b3['command'] = addup3
    b4['command'] = addup4
    b5['command'] = addup5
    b6['command'] = addup6
    b7['command'] = addup7
    b8['command'] = addup8
    b9['command'] = addup9
    bParenthesis1['command'] = test
    bParenthesis2['command'] = test
    bDivision['command'] = dv
    bMultiply['command'] = tm
    bMinus['command'] = bmin
    bPlus['command'] = bstoreplus
    bEqual['command'] = equal
    b0['text'] = '0'
    bParenthesis1['text'] = '('
    bParenthesis2['text'] = ')'
    bDivision['text'] = '/'
    bMultiply['text'] = '*'
    bMinus['text'] = '-'
    bPlus['text'] = '+'
    bEqual['text'] = '='
    b0['state'] = NORMAL
    b1['state'] = NORMAL
    b2['state'] = NORMAL
    b3['state'] = DISABLED
    b4['state'] = DISABLED
    b5['state'] = DISABLED
    b6['state'] = DISABLED
    b7['state'] = DISABLED
    b8['state'] = DISABLED
    b9['state'] = DISABLED
    bA['state'] = DISABLED
    bB['state'] = DISABLED
    bC['state'] = DISABLED
    bD['state'] = DISABLED
    bE['state'] = DISABLED
    bF['state'] = DISABLED
    bParenthesis2['state'] = DISABLED
    bParenthesis1['state'] = DISABLED
    bDivision['state'] = NORMAL
    bMultiply['state'] = NORMAL
    bMinus['state'] = NORMAL
    bPlus['state'] = NORMAL
    bEqual['state'] = NORMAL
    bAC['state'] = NORMAL
    bBackspace['state'] = NORMAL
    megacheck=1
    ac()
def nset4():
    global n, megacheck
    n=4
    b0['command'] = addup0
    b1['command'] = addup1
    b2['command'] = addup2
    b3['command'] = addup3
    b4['command'] = addup4
    b5['command'] = addup5
    b6['command'] = addup6
    b7['command'] = addup7
    b8['command'] = addup8
    b9['command'] = addup9
    bParenthesis1['command'] = test
    bParenthesis2['command'] = test
    bDivision['command'] = dv
    bMultiply['command'] = tm
    bMinus['command'] = bmin
    bPlus['command'] = bstoreplus
    bEqual['command'] = equal
    b0['text'] = '0'
    bParenthesis1['text'] = '('
    bParenthesis2['text'] = ')'
    bDivision['text'] = '/'
    bMultiply['text'] = '*'
    bMinus['text'] = '-'
    bPlus['text'] = '+'
    bEqual['text'] = '='
    b0['state'] = NORMAL
    b1['state'] = NORMAL
    b2['state'] = NORMAL
    b3['state'] = NORMAL
    b4['state'] = DISABLED
    b5['state'] = DISABLED
    b6['state'] = DISABLED
    b7['state'] = DISABLED
    b8['state'] = DISABLED
    b9['state'] = DISABLED
    bA['state'] = DISABLED
    bB['state'] = DISABLED
    bC['state'] = DISABLED
    bD['state'] = DISABLED
    bE['state'] = DISABLED
    bF['state'] = DISABLED
    bParenthesis2['state'] = DISABLED
    bParenthesis1['state'] = DISABLED
    bDivision['state'] = NORMAL
    bMultiply['state'] = NORMAL
    bMinus['state'] = NORMAL
    bPlus['state'] = NORMAL
    bEqual['state'] = NORMAL
    bAC['state'] = NORMAL
    bBackspace['state'] = NORMAL
    megacheck=1
    ac()
def nset5():
    global n, megacheck
    n=5
    b0['command'] = addup0
    b1['command'] = addup1
    b2['command'] = addup2
    b3['command'] = addup3
    b4['command'] = addup4
    b5['command'] = addup5
    b6['command'] = addup6
    b7['command'] = addup7
    b8['command'] = addup8
    b9['command'] = addup9
    bParenthesis1['command'] = test
    bParenthesis2['command'] = test
    bDivision['command'] = dv
    bMultiply['command'] = tm
    bMinus['command'] = bmin
    bPlus['command'] = bstoreplus
    bEqual['command'] = equal
    b0['text'] = '0'
    bParenthesis1['text'] = '('
    bParenthesis2['text'] = ')'
    bDivision['text'] = '/'
    bMultiply['text'] = '*'
    bMinus['text'] = '-'
    bPlus['text'] = '+'
    bEqual['text'] = '='
    b0['state'] = NORMAL
    b1['state'] = NORMAL
    b2['state'] = NORMAL
    b3['state'] = NORMAL
    b4['state'] = NORMAL
    b5['state'] = DISABLED
    b6['state'] = DISABLED
    b7['state'] = DISABLED
    b8['state'] = DISABLED
    b9['state'] = DISABLED
    bA['state'] = DISABLED
    bB['state'] = DISABLED
    bC['state'] = DISABLED
    bD['state'] = DISABLED
    bE['state'] = DISABLED
    bF['state'] = DISABLED
    bParenthesis2['state'] = DISABLED
    bParenthesis1['state'] = DISABLED
    bDivision['state'] = NORMAL
    bMultiply['state'] = NORMAL
    bMinus['state'] = NORMAL
    bPlus['state'] = NORMAL
    bEqual['state'] = NORMAL
    bAC['state'] = NORMAL
    bBackspace['state'] = NORMAL
    megacheck=1
    ac()
def nset6():
    global n, megacheck
    n=6
    b0['command'] = addup0
    b1['command'] = addup1
    b2['command'] = addup2
    b3['command'] = addup3
    b4['command'] = addup4
    b5['command'] = addup5
    b6['command'] = addup6
    b7['command'] = addup7
    b8['command'] = addup8
    b9['command'] = addup9
    bParenthesis1['command'] = test
    bParenthesis2['command'] = test
    bDivision['command'] = dv
    bMultiply['command'] = tm
    bMinus['command'] = bmin
    bPlus['command'] = bstoreplus
    bEqual['command'] = equal
    b0['text'] = '0'
    bParenthesis1['text'] = '('
    bParenthesis2['text'] = ')'
    bDivision['text'] = '/'
    bMultiply['text'] = '*'
    bMinus['text'] = '-'
    bPlus['text'] = '+'
    bEqual['text'] = '='
    b0['state'] = NORMAL
    b1['state'] = NORMAL
    b2['state'] = NORMAL
    b3['state'] = NORMAL
    b4['state'] = NORMAL
    b5['state'] = NORMAL
    b6['state'] = DISABLED
    b7['state'] = DISABLED
    b8['state'] = DISABLED
    b9['state'] = DISABLED
    bA['state'] = DISABLED
    bB['state'] = DISABLED
    bC['state'] = DISABLED
    bD['state'] = DISABLED
    bE['state'] = DISABLED
    bF['state'] = DISABLED
    bParenthesis2['state'] = DISABLED
    bParenthesis1['state'] = DISABLED
    bDivision['state'] = NORMAL
    bMultiply['state'] = NORMAL
    bMinus['state'] = NORMAL
    bPlus['state'] = NORMAL
    bEqual['state'] = NORMAL
    bAC['state'] = NORMAL
    bBackspace['state'] = NORMAL
    megacheck=1
    ac()
def nset7():
    global n, megacheck
    n=7
    b0['command'] = addup0
    b1['command'] = addup1
    b2['command'] = addup2
    b3['command'] = addup3
    b4['command'] = addup4
    b5['command'] = addup5
    b6['command'] = addup6
    b7['command'] = addup7
    b8['command'] = addup8
    b9['command'] = addup9
    bParenthesis1['command'] = test
    bParenthesis2['command'] = test
    bDivision['command'] = dv
    bMultiply['command'] = tm
    bMinus['command'] = bmin
    bPlus['command'] = bstoreplus
    bEqual['command'] = equal
    b0['text'] = '0'
    bParenthesis1['text'] = '('
    bParenthesis2['text'] = ')'
    bDivision['text'] = '/'
    bMultiply['text'] = '*'
    bMinus['text'] = '-'
    bPlus['text'] = '+'
    bEqual['text'] = '='
    b0['state'] = NORMAL
    b1['state'] = NORMAL
    b2['state'] = NORMAL
    b3['state'] = NORMAL
    b4['state'] = NORMAL
    b5['state'] = NORMAL
    b6['state'] = NORMAL
    b7['state'] = DISABLED
    b8['state'] = DISABLED
    b9['state'] = DISABLED
    bA['state'] = DISABLED
    bB['state'] = DISABLED
    bC['state'] = DISABLED
    bD['state'] = DISABLED
    bE['state'] = DISABLED
    bF['state'] = DISABLED
    bParenthesis2['state'] = DISABLED
    bParenthesis1['state'] = DISABLED
    bDivision['state'] = NORMAL
    bMultiply['state'] = NORMAL
    bMinus['state'] = NORMAL
    bPlus['state'] = NORMAL
    bEqual['state'] = NORMAL
    bAC['state'] = NORMAL
    bBackspace['state'] = NORMAL
    megacheck=1
    ac()
def nset8():
    global n, megacheck
    n=8
    b0['command'] = addup0
    b1['command'] = addup1
    b2['command'] = addup2
    b3['command'] = addup3
    b4['command'] = addup4
    b5['command'] = addup5
    b6['command'] = addup6
    b7['command'] = addup7
    b8['command'] = addup8
    b9['command'] = addup9
    bParenthesis1['command'] = test
    bParenthesis2['command'] = test
    bDivision['command'] = dv
    bMultiply['command'] = tm
    bMinus['command'] = bmin
    bPlus['command'] = bstoreplus
    bEqual['command'] = equal
    b0['text'] = '0'
    bParenthesis1['text'] = '('
    bParenthesis2['text'] = ')'
    bDivision['text'] = '/'
    bMultiply['text'] = '*'
    bMinus['text'] = '-'
    bPlus['text'] = '+'
    bEqual['text'] = '='
    b0['state'] = NORMAL
    b1['state'] = NORMAL
    b2['state'] = NORMAL
    b3['state'] = NORMAL
    b4['state'] = NORMAL
    b5['state'] = NORMAL
    b6['state'] = NORMAL
    b7['state'] = NORMAL
    b8['state'] = DISABLED
    b9['state'] = DISABLED
    bA['state'] = DISABLED
    bB['state'] = DISABLED
    bC['state'] = DISABLED
    bD['state'] = DISABLED
    bE['state'] = DISABLED
    bF['state'] = DISABLED
    bParenthesis2['state'] = DISABLED
    bParenthesis1['state'] = DISABLED
    bDivision['state'] = NORMAL
    bMultiply['state'] = NORMAL
    bMinus['state'] = NORMAL
    bPlus['state'] = NORMAL
    bEqual['state'] = NORMAL
    bAC['state'] = NORMAL
    bBackspace['state'] = NORMAL
    megacheck=1
    ac()
def nset9():
    global n, megacheck
    n=9
    b0['command'] = addup0
    b1['command'] = addup1
    b2['command'] = addup2
    b3['command'] = addup3
    b4['command'] = addup4
    b5['command'] = addup5
    b6['command'] = addup6
    b7['command'] = addup7
    b8['command'] = addup8
    b9['command'] = addup9
    bParenthesis1['command'] = test
    bParenthesis2['command'] = test
    bDivision['command'] = dv
    bMultiply['command'] = tm
    bMinus['command'] = bmin
    bPlus['command'] = bstoreplus
    bEqual['command'] = equal
    b0['text'] = '0'
    bParenthesis1['text'] = '('
    bParenthesis2['text'] = ')'
    bDivision['text'] = '/'
    bMultiply['text'] = '*'
    bMinus['text'] = '-'
    bPlus['text'] = '+'
    bEqual['text'] = '='
    b0['state'] = NORMAL
    b1['state'] = NORMAL
    b2['state'] = NORMAL
    b3['state'] = NORMAL
    b4['state'] = NORMAL
    b5['state'] = NORMAL
    b6['state'] = NORMAL
    b7['state'] = NORMAL
    b8['state'] = NORMAL
    b9['state'] = DISABLED
    bA['state'] = DISABLED
    bB['state'] = DISABLED
    bC['state'] = DISABLED
    bD['state'] = DISABLED
    bE['state'] = DISABLED
    bF['state'] = DISABLED
    bParenthesis2['state'] = DISABLED
    bParenthesis1['state'] = DISABLED
    bDivision['state'] = NORMAL
    bMultiply['state'] = NORMAL
    bMinus['state'] = NORMAL
    bPlus['state'] = NORMAL
    bEqual['state'] = NORMAL
    bAC['state'] = NORMAL
    bBackspace['state'] = NORMAL
    megacheck=1
    ac()
def nset10():
    global n, megacheck
    n=10
    b0['command'] = addup0
    b1['command'] = addup1
    b2['command'] = addup2
    b3['command'] = addup3
    b4['command'] = addup4
    b5['command'] = addup5
    b6['command'] = addup6
    b7['command'] = addup7
    b8['command'] = addup8
    b9['command'] = addup9
    bParenthesis1['command'] = test
    bParenthesis2['command'] = test
    bDivision['command'] = dv
    bMultiply['command'] = tm
    bMinus['command'] = bmin
    bPlus['command'] = bstoreplus
    bEqual['command'] = equal
    b0['text'] = '0'
    bParenthesis1['text'] = '('
    bParenthesis2['text'] = ')'
    bDivision['text'] = '/'
    bMultiply['text'] = '*'
    bMinus['text'] = '-'
    bPlus['text'] = '+'
    bEqual['text'] = '='
    b0['state'] = NORMAL
    b1['state'] = NORMAL
    b2['state'] = NORMAL
    b3['state'] = NORMAL
    b4['state'] = NORMAL
    b5['state'] = NORMAL
    b6['state'] = NORMAL
    b7['state'] = NORMAL
    b8['state'] = NORMAL
    b9['state'] = NORMAL
    bA['state'] = DISABLED
    bB['state'] = DISABLED
    bC['state'] = DISABLED
    bD['state'] = DISABLED
    bE['state'] = DISABLED
    bF['state'] = DISABLED
    bParenthesis2['state'] = DISABLED
    bParenthesis1['state'] = DISABLED
    bDivision['state'] = NORMAL
    bMultiply['state'] = NORMAL
    bMinus['state'] = NORMAL
    bPlus['state'] = NORMAL
    bEqual['state'] = NORMAL
    bAC['state'] = NORMAL
    bBackspace['state'] = NORMAL
    megacheck=1
    ac()
def nset11():
    global n, megacheck
    n=11
    b0['command'] = addup0
    b1['command'] = addup1
    b2['command'] = addup2
    b3['command'] = addup3
    b4['command'] = addup4
    b5['command'] = addup5
    b6['command'] = addup6
    b7['command'] = addup7
    b8['command'] = addup8
    b9['command'] = addup9
    bParenthesis1['command'] = test
    bParenthesis2['command'] = test
    bDivision['command'] = dv
    bMultiply['command'] = tm
    bMinus['command'] = bmin
    bPlus['command'] = bstoreplus
    bEqual['command'] = equal
    b0['text'] = '0'
    bParenthesis1['text'] = '('
    bParenthesis2['text'] = ')'
    bDivision['text'] = '/'
    bMultiply['text'] = '*'
    bMinus['text'] = '-'
    bPlus['text'] = '+'
    bEqual['text'] = '='
    b0['state'] = NORMAL
    b1['state'] = NORMAL
    b2['state'] = NORMAL
    b3['state'] = NORMAL
    b4['state'] = NORMAL
    b5['state'] = NORMAL
    b6['state'] = NORMAL
    b7['state'] = NORMAL
    b8['state'] = NORMAL
    b9['state'] = NORMAL
    bA['state'] = NORMAL
    bB['state'] = DISABLED
    bC['state'] = DISABLED
    bD['state'] = DISABLED
    bE['state'] = DISABLED
    bF['state'] = DISABLED
    bParenthesis2['state'] = DISABLED
    bParenthesis1['state'] = DISABLED
    bDivision['state'] = NORMAL
    bMultiply['state'] = NORMAL
    bMinus['state'] = NORMAL
    bPlus['state'] = NORMAL
    bEqual['state'] = NORMAL
    bAC['state'] = NORMAL
    bBackspace['state'] = NORMAL
    megacheck=1
    ac()
def nset12():
    global n, megacheck
    n=12
    b0['command'] = addup0
    b1['command'] = addup1
    b2['command'] = addup2
    b3['command'] = addup3
    b4['command'] = addup4
    b5['command'] = addup5
    b6['command'] = addup6
    b7['command'] = addup7
    b8['command'] = addup8
    b9['command'] = addup9
    bParenthesis1['command'] = test
    bParenthesis2['command'] = test
    bDivision['command'] = dv
    bMultiply['command'] = tm
    bMinus['command'] = bmin
    bPlus['command'] = bstoreplus
    bEqual['command'] = equal
    b0['text'] = '0'
    bParenthesis1['text'] = '('
    bParenthesis2['text'] = ')'
    bDivision['text'] = '/'
    bMultiply['text'] = '*'
    bMinus['text'] = '-'
    bPlus['text'] = '+'
    bEqual['text'] = '='
    b0['state'] = NORMAL
    b1['state'] = NORMAL
    b2['state'] = NORMAL
    b3['state'] = NORMAL
    b4['state'] = NORMAL
    b5['state'] = NORMAL
    b6['state'] = NORMAL
    b7['state'] = NORMAL
    b8['state'] = NORMAL
    b9['state'] = NORMAL
    bA['state'] = NORMAL
    bB['state'] = NORMAL
    bC['state'] = DISABLED
    bD['state'] = DISABLED
    bE['state'] = DISABLED
    bF['state'] = DISABLED
    bParenthesis2['state'] = DISABLED
    bParenthesis1['state'] = DISABLED
    bDivision['state'] = NORMAL
    bMultiply['state'] = NORMAL
    bMinus['state'] = NORMAL
    bPlus['state'] = NORMAL
    bEqual['state'] = NORMAL
    bAC['state'] = NORMAL
    bBackspace['state'] = NORMAL
    megacheck=1
    ac()
def nset13():
    global n, megacheck
    n=13
    b0['command'] = addup0
    b1['command'] = addup1
    b2['command'] = addup2
    b3['command'] = addup3
    b4['command'] = addup4
    b5['command'] = addup5
    b6['command'] = addup6
    b7['command'] = addup7
    b8['command'] = addup8
    b9['command'] = addup9
    bParenthesis1['command'] = test
    bParenthesis2['command'] = test
    bDivision['command'] = dv
    bMultiply['command'] = tm
    bMinus['command'] = bmin
    bPlus['command'] = bstoreplus
    bEqual['command'] = equal
    b0['text'] = '0'
    bParenthesis1['text'] = '('
    bParenthesis2['text'] = ')'
    bDivision['text'] = '/'
    bMultiply['text'] = '*'
    bMinus['text'] = '-'
    bPlus['text'] = '+'
    bEqual['text'] = '='
    b0['state'] = NORMAL
    b1['state'] = NORMAL
    b2['state'] = NORMAL
    b3['state'] = NORMAL
    b4['state'] = NORMAL
    b5['state'] = NORMAL
    b6['state'] = NORMAL
    b7['state'] = NORMAL
    b8['state'] = NORMAL
    b9['state'] = NORMAL
    bA['state'] = NORMAL
    bB['state'] = NORMAL
    bC['state'] = NORMAL
    bD['state'] = DISABLED
    bE['state'] = DISABLED
    bF['state'] = DISABLED
    bParenthesis2['state'] = DISABLED
    bParenthesis1['state'] = DISABLED
    bDivision['state'] = NORMAL
    bMultiply['state'] = NORMAL
    bMinus['state'] = NORMAL
    bPlus['state'] = NORMAL
    bEqual['state'] = NORMAL
    bAC['state'] = NORMAL
    bBackspace['state'] = NORMAL
    megacheck=1
    ac()
def nset14():
    global n, megacheck
    n=14
    b0['command'] = addup0
    b1['command'] = addup1
    b2['command'] = addup2
    b3['command'] = addup3
    b4['command'] = addup4
    b5['command'] = addup5
    b6['command'] = addup6
    b7['command'] = addup7
    b8['command'] = addup8
    b9['command'] = addup9
    bParenthesis1['command'] = test
    bParenthesis2['command'] = test
    bDivision['command'] = dv
    bMultiply['command'] = tm
    bMinus['command'] = bmin
    bPlus['command'] = bstoreplus
    bEqual['command'] = equal
    b0['text'] = '0'
    bParenthesis1['text'] = '('
    bParenthesis2['text'] = ')'
    bDivision['text'] = '/'
    bMultiply['text'] = '*'
    bMinus['text'] = '-'
    bPlus['text'] = '+'
    bEqual['text'] = '='
    b0['state'] = NORMAL
    b1['state'] = NORMAL
    b2['state'] = NORMAL
    b3['state'] = NORMAL
    b4['state'] = NORMAL
    b5['state'] = NORMAL
    b6['state'] = NORMAL
    b7['state'] = NORMAL
    b8['state'] = NORMAL
    b9['state'] = NORMAL
    bA['state'] = NORMAL
    bB['state'] = NORMAL
    bC['state'] = NORMAL
    bD['state'] = NORMAL
    bE['state'] = DISABLED
    bF['state'] = DISABLED
    bParenthesis2['state'] = DISABLED
    bParenthesis1['state'] = DISABLED
    bDivision['state'] = NORMAL
    bMultiply['state'] = NORMAL
    bMinus['state'] = NORMAL
    bPlus['state'] = NORMAL
    bEqual['state'] = NORMAL
    bAC['state'] = NORMAL
    bBackspace['state'] = NORMAL
    megacheck=1
    ac()
def nset15():
    global n, megacheck
    n=15
    b0['command'] = addup0
    b1['command'] = addup1
    b2['command'] = addup2
    b3['command'] = addup3
    b4['command'] = addup4
    b5['command'] = addup5
    b6['command'] = addup6
    b7['command'] = addup7
    b8['command'] = addup8
    b9['command'] = addup9
    bParenthesis1['command'] = test
    bParenthesis2['command'] = test
    bDivision['command'] = dv
    bMultiply['command'] = tm
    bMinus['command'] = bmin
    bPlus['command'] = bstoreplus
    bEqual['command'] = equal
    b0['text'] = '0'
    bParenthesis1['text'] = '('
    bParenthesis2['text'] = ')'
    bDivision['text'] = '/'
    bMultiply['text'] = '*'
    bMinus['text'] = '-'
    bPlus['text'] = '+'
    bEqual['text'] = '='
    b0['state'] = NORMAL
    b1['state'] = NORMAL
    b2['state'] = NORMAL
    b3['state'] = NORMAL
    b4['state'] = NORMAL
    b5['state'] = NORMAL
    b6['state'] = NORMAL
    b7['state'] = NORMAL
    b8['state'] = NORMAL
    b9['state'] = NORMAL
    bA['state'] = NORMAL
    bB['state'] = NORMAL
    bC['state'] = NORMAL
    bD['state'] = NORMAL
    bE['state'] = NORMAL
    bF['state'] = DISABLED
    bParenthesis2['state'] = DISABLED
    bParenthesis1['state'] = DISABLED
    bDivision['state'] = NORMAL
    bMultiply['state'] = NORMAL
    bMinus['state'] = NORMAL
    bPlus['state'] = NORMAL
    bEqual['state'] = NORMAL
    bAC['state'] = NORMAL
    bBackspace['state'] = NORMAL
    megacheck=1
    ac()
def nset16():
    global n, megacheck
    n=16
    b0['command'] = addup0
    b1['command'] = addup1
    b2['command'] = addup2
    b3['command'] = addup3
    b4['command'] = addup4
    b5['command'] = addup5
    b6['command'] = addup6
    b7['command'] = addup7
    b8['command'] = addup8
    b9['command'] = addup9
    bParenthesis1['command'] = test
    bParenthesis2['command'] = test
    bDivision['command'] = dv
    bMultiply['command'] = tm
    bMinus['command'] = bmin
    bPlus['command'] = bstoreplus
    bEqual['command'] = equal
    b0['text'] = '0'
    bParenthesis1['text'] = '('
    bParenthesis2['text'] = ')'
    bDivision['text'] = '/'
    bMultiply['text'] = '*'
    bMinus['text'] = '-'
    bPlus['text'] = '+'
    bEqual['text'] = '='
    b0['state'] = NORMAL
    b1['state'] = NORMAL
    b2['state'] = NORMAL
    b3['state'] = NORMAL
    b4['state'] = NORMAL
    b5['state'] = NORMAL
    b6['state'] = NORMAL
    b7['state'] = NORMAL
    b8['state'] = NORMAL
    b9['state'] = NORMAL
    bA['state'] = NORMAL
    bB['state'] = NORMAL
    bC['state'] = NORMAL
    bD['state'] = NORMAL
    bE['state'] = NORMAL
    bF['state'] = NORMAL
    bParenthesis2['state'] = DISABLED
    bParenthesis1['state'] = DISABLED
    bDivision['state'] = NORMAL
    bMultiply['state'] = NORMAL
    bMinus['state'] = NORMAL
    bPlus['state'] = NORMAL
    bEqual['state'] = NORMAL
    bAC['state'] = NORMAL
    bBackspace['state'] = NORMAL
    megacheck=1
    ac()
def nreset():
    global n, megacheck
    n=0
    megacheck=0
    ac()

# Frame initialize

allFrame = tk.Frame(win)
bFrame1 = tk.Frame(allFrame)
bFrame2 = tk.Frame(allFrame)
bFrame3 = tk.Frame(allFrame)
bFrame4 = tk.Frame(allFrame)
bFrame5 = tk.Frame(allFrame)
bFrame6 = tk.Frame(allFrame)

# Button initialize
bA = ttk.Button(bFrame1, text="A", command=testaddupA, width=6, state=DISABLED)
bFloat = ttk.Button(bFrame1, text=",", command=floatb, width=6, state=DISABLED)
b0 = ttk.Button(bFrame1, text="0", command=addup0, width=6, state=DISABLED)
bCc = ttk.Button(bFrame1, text ="Сс", command = Cc, width=6)
bEqual = ttk.Button(bFrame1, text="=", command=equal, width=6, state=DISABLED)

bB = ttk.Button(bFrame2, text="B", command=testaddupB, width=6, state=DISABLED)
b1 = ttk.Button(bFrame2, text="1", command=addup1, width=6, state=DISABLED)
b2 = ttk.Button(bFrame2, text="2", command=addup2, width=6, state=DISABLED)
b3 = ttk.Button(bFrame2, text="3", command=addup3, width=6, state=DISABLED)
bPlus = ttk.Button(bFrame2, text="+", command=bstoreplus, width=6, state=DISABLED)

bC = ttk.Button(bFrame3, text="C", command=testaddupC, width=6, state=DISABLED)
b4 = ttk.Button(bFrame3, text="4", command=addup4, width=6, state=DISABLED)
b5 = ttk.Button(bFrame3, text="5", command=addup5, width=6, state=DISABLED)
b6 = ttk.Button(bFrame3, text="6", command=addup6, width=6, state=DISABLED)
bMinus = ttk.Button(bFrame3, text="-", command=bmin, width=6, state=DISABLED)

bD = ttk.Button(bFrame4, text="D", command=testaddupD, width=6, state=DISABLED)
b7 = ttk.Button(bFrame4, text="7", command=addup7, width=6, state=DISABLED)
b8 = ttk.Button(bFrame4, text="8", command=addup8, width=6, state=DISABLED)
b9 = ttk.Button(bFrame4, text="9", command=addup9, width=6, state=DISABLED)
bMultiply = ttk.Button(bFrame4, text="*", command=tm, width=6, state=DISABLED)

bE = ttk.Button(bFrame5, text="E", command=testaddupE, width=6, state=DISABLED)
bParenthesis1 = ttk.Button(bFrame5, text="(", command=test, width=6, state=DISABLED)
bParenthesis2 = ttk.Button(bFrame5, text=")", command=test, width=6, state=DISABLED)
bDivision = ttk.Button(bFrame5, text="/", command=dv, width=6, state=DISABLED)
bBackspace = ttk.Button(bFrame5, text="←", command=backspace, width=6, state=DISABLED)

bF = ttk.Button(bFrame6, text="F", command=testaddupF, width=6, state=DISABLED)
bAC = ttk.Button(bFrame6, text="AC", command=ac, width=6, state=DISABLED)

# Button pack

bA.pack(side=LEFT, ipady=10)
bFloat.pack(side=LEFT, ipady=10)
b0.pack(side=LEFT, ipady=10)
bEqual.pack(side=RIGHT, ipady=10)
bCc.pack(side=RIGHT, ipady=10)

bB.pack(side=LEFT, ipady=10)
b1.pack(side=LEFT, ipady=10)
b2.pack(side=LEFT, ipady=10)
bPlus.pack(side=RIGHT, ipady=10)
b3.pack(side=RIGHT, ipady=10)

bC.pack(side=LEFT, ipady=10)
b4.pack(side=LEFT, ipady=10)
b5.pack(side=LEFT, ipady=10)
bMinus.pack(side=RIGHT, ipady=10)
b6.pack(side=RIGHT, ipady=10)

bD.pack(side=LEFT, ipady=10)
b7.pack(side=LEFT, ipady=10)
b8.pack(side=LEFT, ipady=10)
bMultiply.pack(side=RIGHT, ipady=10)
b9.pack(side=RIGHT, ipady=10)

bE.pack(side=LEFT, ipady=10)
bParenthesis1.pack(side=LEFT, ipady=10)
bParenthesis2.pack(side=LEFT, ipady=10)
bBackspace.pack(side=RIGHT, ipady=10)
bDivision.pack(side=RIGHT, ipady=10)

bF.pack(side=LEFT, ipady=10, padx=[0, 69])
bAC.pack(side=RIGHT, ipady=10, padx=[69, 0])

# Warn

warning1=Label(win, text='В связи с некоторыми неполадками,', font=("Arial", 11))
warning2=Label(win, text='калькулятор, до поры, до времени,', font=("Arial", 11))
warning3=Label(win, text='работает в консоли PyCharm. Приносим', font=("Arial", 11))
warning4=Label(win, text='извинения, мы уже работаем над этим!', font=("Arial", 11))
version=Label(win, text='v0.5.0 Первый выпущенный прототип ', font=("Arial", 12))

# Window frame pack

Label.pack(warning1, anchor=N)
Label.pack(warning2, anchor=N)
Label.pack(warning3, anchor=N)
Label.pack(warning4, anchor=N)
Label.pack(version, side=BOTTOM, anchor=W)
bFrame6.pack(padx=[25, 25])
bFrame5.pack(padx=[25, 25])
bFrame4.pack(padx=[25, 25])
bFrame3.pack(padx=[25, 25])
bFrame2.pack(padx=[25, 25])
bFrame1.pack(padx=[25, 25])
allFrame.pack(side=BOTTOM, pady=[0, 5])

#Оставить и ни в коем случае не убирать :)

win.mainloop()