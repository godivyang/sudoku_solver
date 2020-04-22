from tkinter import *
from tkinter.font import Font

main = Tk()

main.config(bg='black')

e=Label(main, text='SUDOKU SOLVER', bg='yellow')
e.grid(row=0, column=0, columnspan=11)
e.config(font=("Courier", 30))

temp=[['','','','','','','','',''],
      ['','','','','','','','',''],
      ['','','','','','','','',''],
      ['','','','','','','','',''],
      ['','','','','','','','',''],
      ['','','','','','','','',''],
      ['','','','','','','','',''],
      ['','','','','','','','',''],
      ['','','','','','','','','']]

question=[[0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0]]

def entry():
    for i in range(9):
        for j in range(9):
            if temp[i][j].get('1.0')=='\n':
                continue
            else:
                question[i][j]=int(temp[i][j].get('1.0'))
    sudoku=question
    return sudoku

e1=Label(main, text='', font=("Helvetica", 1), bg='black')
e1.grid(row=1, column=3)
e2=Label(main, text='', font=("Helvetica", 1), bg='black')
e2.grid(row=1, column=7)
e3=Label(main, text='', font=("Helvetica", 1), bg='black')
e3.grid(row=4, column=0)
e4=Label(main, text='', font=("Helvetica", 1), bg='black')
e4.grid(row=8, column=0)
e5=Label(main, text='', font=("Helvetica", 1), bg='black')
e5.grid(row=12, column=0)
e6=Label(main, text='', font=("Helvetica", 1), bg='black')
e6.grid(row=14, column=0)

for i in range(3):
    for j in range(3):
        temp_value=StringVar()
        temp[i][j] = Text(main, width=2, height=1, font=("Helvetica", 20))
        temp[i][j].grid(row=i+1, column=j)

for i in range(3):
    for j in range(3,6):
        temp_value=StringVar()
        temp[i][j] = Text(main, width=2, height=1, font=("Helvetica", 20), bg='#FFFF99')
        temp[i][j].grid(row=i+1, column=j+1)

for i in range(3):
    for j in range(6,9):
        temp_value=StringVar()
        temp[i][j] = Text(main, width=2, height=1, font=("Helvetica", 20))
        temp[i][j].grid(row=i+1, column=j+2)

for i in range(3,6):
    for j in range(3):
        temp_value=StringVar()
        temp[i][j] = Text(main, width=2, height=1, font=("Helvetica", 20), bg='#FFFF99')
        temp[i][j].grid(row=i+2, column=j)

for i in range(3,6):
    for j in range(3,6):
        temp_value=StringVar()
        temp[i][j] = Text(main, width=2, height=1, font=("Helvetica", 20))
        temp[i][j].grid(row=i+2, column=j+1)

for i in range(3,6):
    for j in range(6,9):
        temp_value=StringVar()
        temp[i][j] = Text(main, width=2, height=1, font=("Helvetica", 20), bg='#FFFF99')
        temp[i][j].grid(row=i+2, column=j+2)

for i in range(6,9):
    for j in range(3):
        temp_value=StringVar()
        temp[i][j] = Text(main, width=2, height=1, font=("Helvetica", 20))
        temp[i][j].grid(row=i+3, column=j)

for i in range(6,9):
    for j in range(3,6):
        temp_value=StringVar()
        temp[i][j] = Text(main, width=2, height=1, font=("Helvetica", 20), bg='#FFFF99')
        temp[i][j].grid(row=i+3, column=j+1)

for i in range(6,9):
    for j in range(6,9):
        temp_value=StringVar()
        temp[i][j] = Text(main, width=2, height=1, font=("Helvetica", 20))
        temp[i][j].grid(row=i+3, column=j+2)

sudoku=entry()

pencil=[[],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],[],
        [],[],[],[],[],[],[],[],[]]

sudoku1=sudoku
pencil1=pencil

def block_no(a1):
    a11=0
    a11=a1//3
    if a11==0:
        a3=[0,1,2]
    elif a11==1:
        a3=[3,4,5]
    elif a11==2:
        a3=[6,7,8]
    return a3

def pencil_filler(i,j,n):
    for i1 in range(9):
        if sudoku[i1][j]==n:
            return False
    for j1 in range(9):
        if sudoku[i][j1]==n:
            return False
    a1=[]
    a1=block_no(i)
    b1=[]
    b1=block_no(j)
    for i1 in a1:
        for j1 in b1:
            if sudoku[i1][j1]==n:
                return False
    return True

def remover(i,j,n):
    pencil[9*i+j]=()
    for i1 in range(9):
        if n in pencil[9*i1+j]:
            pencil[9*i1+j].remove(n)
    for j1 in range(9):
        if n in pencil[9*i+j1]:
            pencil[9*i+j1].remove(n)
    a1=block_no(i)
    b1=block_no(j)
    for i2 in a1:
        for j2 in b1:
            if n in pencil[9*i2+j2]:
                pencil[9*i2+j2].remove(n)

def naked_single(i,j,n):
    if len(pencil[9*i+j])==1:
        remover(i,j,n)
        return True
    return False

def hidden_single_C(i,j,n):
    a=[0,1,2,3,4,5,6,7,8]
    a.remove(i)
    for i1 in a:
        if n in pencil[9*i1+j]:
            return False
    remover(i,j,n)
    return True

def hidden_single_R(i,j,n):
    b=[0,1,2,3,4,5,6,7,8]
    b.remove(j)
    for j1 in b:
        if n in pencil[9*i+j1]:
            return False
    remover(i,j,n)
    return True

def naked_pair_R(i,j,n):
    if len(pencil[9*i+j])==2:
        j1=[0,1,2,3,4,5,6,7,8]
        j1.remove(j)
        for j2 in j1:
            if len(pencil[9*i+j2])==2:
                if pencil[9*i+j2][0]==pencil[9*i+j][0] and pencil[9*i+j2][1]==pencil[9*i+j][1]:
                    j1.remove(j2)
                    for j3 in j1:
                        if n in pencil[9*i+j3]:
                            pencil[9*i+j3].remove(n)

def naked_pair_C(i,j,n):
    if len(pencil[9*i+j])==2:
        i1=[0,1,2,3,4,5,6,7,8]
        i1.remove(i)
        for i2 in i1:
            if len(pencil[9*i2+j])==2:
                if pencil[9*i2+j][0]==pencil[9*i+j][0] and pencil[9*i2+j][1]==pencil[9*i+j][1]:
                    i1.remove(i2)
                    for i3 in i1:
                        if n in pencil[9*i3+j]:
                            pencil[9*i3+j].remove(n)

def naked_pair_B(i,j,n):
    if len(pencil[9*i+j])==2:
        a1=block_no(i)
        b1=block_no(j)
        for i1 in a1:
            for j1 in b1:
                if i1==i and j1==j:
                    continue
                else:
                    if len(pencil[9*i1+j1])==2:
                        if pencil[9*i1+j1][0]==pencil[9*i+j][0] and pencil[9*i1+j1][1]==pencil[9*i+j][1]:
                            for i2 in a1:
                                for j2 in b1:
                                    if i2==i and j2==j:
                                        continue
                                    elif i2==i1 and j2==j1:
                                        continue
                                    else:
                                        if pencil[9*i+j][0] in pencil[9*i2+j2]:
                                            pencil[9*i2+j2].remove(pencil[9*i+j][0])
                                        if pencil[9*i+j][1 ] in pencil[9*i2+j2]:
                                            pencil[9*i2+j2].remove(pencil[9*i+j][1])
def pointing_pair(i,j,n):
    a1=block_no(i)
    b1=block_no(j)
    a=[]
    b=[]
    for i1 in a1:
        for j1 in b1:
            if n in pencil[9*i1+j1]:
                a.append(i1)
                b.append(j1)
    aa=set(a)
    bb=set(b)
    if len(aa)==1:
        b2=[0,1,2,3,4,5,6,7,8]
        b2.remove(b1[0])
        b2.remove(b1[1])
        b2.remove(b1[2])
        for j3 in b2:
            if n in pencil[9*i+j3]:
                pencil[9*i+j3].remove(n)
    elif len(bb)==1:
        a2=[0,1,2,3,4,5,6,7,8]
        a2.remove(a1[0])
        a2.remove(a1[1])
        a2.remove(a1[2])
        for i3 in a2:
            if n in pencil[9*i3+j]:
                pencil[9*i3+j].remove(n)

def naked_triple_C(i,j,n):
    if len(pencil[9*i+j])==2:
        n1=[pencil[9*i+j][0],pencil[9*i+j][1]]
        a1=[i]
        for i1 in range(9):
            if set(n1).issubset(pencil[9*i1+j]):
                if len(pencil[9*i1+j])==2 and i1!=i:
                    return None
                if len(pencil[9*i1+j])==3:
                    a1.append(i1)
                    for n2 in pencil[9*i1+j]:
                        if n2 not in n1:
                            n1.append(n2)
        if len(a1)==3 and len(n1)==3:
            a=[0,1,2,3,4,5,6,7,8]
            a.remove(a1[0])
            a.remove(a1[1])
            a.remove(a1[2])
            for ii in a:
                for nn in n1:
                    if nn in pencil[9*ii+j]:
                        pencil[9*ii+j].remove(nn)
    elif len(pencil[9*i+j])==3:
        n1=[pencil[9*i+j][0],pencil[9*i+j][1],pencil[9*i+j][2]]
        a1=[]
        for i1 in range(9):
            if set(n1).issubset(pencil[9*i1+j]):
                if len(pencil[9*i1+j])<=3:
                    a1.append(i1)
            if len(a1)==3:
                a=[0,1,2,3,4,5,6,7,8]
                a.remove(a1[0])
                a.remove(a1[1])
                a.remove(a1[2])
                for ii in a:
                    for nn in n1:
                        if nn in pencil[9*ii+j]:
                            pencil[9*ii+j].remove(nn)

def naked_triple_R(i,j,n):
    if len(pencil[9*i+j])==2:
        n1=[pencil[9*i+j][0],pencil[9*i+j][1]]
        b1=[j]
        for j1 in range(9):
            if set(n1).issubset(pencil[9*i+j1]):
                if len(pencil[9*i+j1])==2 and j1!=j:
                    return None
                if len(pencil[9*i+j1])==3:
                    b1.append(j1)
                    for n2 in pencil[9*i+j1]:
                        if n2 not in n1:
                            n1.append(n2)
        if len(b1)==3 and len(n1)==3:
            b=[0,1,2,3,4,5,6,7,8]
            b.remove(b1[0])
            b.remove(b1[1])
            b.remove(b1[2])
            for jj in b:
                for nn in n1:
                    if nn in pencil[9*i+jj]:
                        pencil[9*i+jj].remove(nn)
    elif len(pencil[9*i+j])==3:
        n1=[pencil[9*i+j][0],pencil[9*i+j][1],pencil[9*i+j][2]]
        b1=[]
        for j1 in range(9):
            if set(n1).issubset(pencil[9*i+j1]):
                if len(pencil[9*i+j1])<=3:
                    b1.append(j1)
            if len(b1)==3:
                b=[0,1,2,3,4,5,6,7,8]
                b.remove(b1[0])
                b.remove(b1[1])
                b.remove(b1[2])
                for jj in b:
                    for nn in n1:
                        if nn in pencil[9*i+jj]:
                            pencil[9*i+jj].remove(nn)

def x_wing_R(i,j,n):
    b=[]
    for j1 in range(9):
        if n in pencil[9*i+j1]:
            b.append(j1)
    if len(b)==2:
        i1=[0,1,2,3,4,5,6,7,8]
        i1.remove(i)
        for i3 in i1:
            b1=[]
            if n in pencil[9*i3+b[0]]:
                for j2 in range(9):
                    if n in pencil[9*i3+j2]:
                        b1.append(j2)
                if len(b1)==2 and b1[1]==b[1]:
                    ii=[0,1,2,3,4,5,6,7,8]
                    ii.remove(i)
                    ii.remove(i3)
                    for i2 in ii:
                        if n in pencil[9*i2+b[0]]:
                            pencil[9*i2+b[0]].remove(n)
                        if n in pencil[9*i2+b[1]]:
                            pencil[9*i2+b[1]].remove(n)

def x_wing_C(i,j,n):
    a=[]
    for i1 in range(9):
        if n in pencil[9*i1+j]:
            a.append(i1)
    if len(a)==2:
        j1=[0,1,2,3,4,5,6,7,8]
        j1.remove(j)
        for j3 in j1:
            a1=[]
            if n in pencil[9*a[0]+j3]:
                for i2 in range(9):
                    if n in pencil[9*i2+j3]:
                        a1.append(i2)
                if len(a1)==2 and a1[1]==a[1]:
                    jj=[0,1,2,3,4,5,6,7,8]
                    jj.remove(j)
                    jj.remove(j3)
                    for j2 in jj:
                        if n in pencil[9*a[0]+j2]:
                            pencil[9*a[0]+j2].remove(n)
                        if n in pencil[9*a[1]+j2]:
                            pencil[9*a[1]+j2].remove(n)

def hidden_pair(i,j,n):
    a1=block_no(i)
    b1=block_no(j)
    a=[]
    b=[]
    n1=[1,2,3,4,5,6,7,8,9]
    n1.remove(n)
    for i1 in a1:
        for j1 in b1:
            if n in pencil[9*i1+j1]:
                a.append(i1)
                b.append(j1)
    aa=set(a)
    bb=set(b)
    if len(aa)==1 and len(bb)==2:
        for n2 in n1:
            a2=[]
            b2=[]
            for i1 in a1:
                for j1 in b1:
                    if n2 in pencil[9*i1+j1]:
                        a2.append(i1)
                        b2.append(j1)
            if len(set(a2))==1 and len(set(b2))==2:
                if a[0]==a2[0] and b[0]==b2[0] and b[1]==b2[1]:
                    for n4 in pencil[9*a[0]+b[0]]:
                        if n4!=n and n4!=n2:
                            pencil[9*a[0]+b[0]].remove(n4)
                    for n4 in pencil[9*a[0]+b[1]]:
                        if n4!=n and n4!=n2:
                            pencil[9*a[0]+b[1]].remove(n4)
    if len(aa)==2 and len(bb)==1:
        for n2 in n1:
            a2=[]
            b2=[]
            for i1 in a1:
                for j1 in b1:
                    if n2 in pencil[9*i1+j1]:
                        a2.append(i1)
                        b2.append(j1)
            if len(set(a2))==2 and len(set(b2))==1:
                if b[0]==b2[0] and a[0]==a2[0] and a[1]==a2[1]:
                    for n4 in pencil[9*a[0]+b[0]]:
                        if n4!=n and n4!=n2:
                            pencil[9*a[0]+b[0]].remove(n4)
                    for n4 in pencil[9*a[1]+b[0]]:
                        if n4!=n and n4!=n2:
                            pencil[9*a[1]+b[0]].remove(n4)

def zero_checker():
    a=[]
    for i in range(9):
        for j in range(9):
            if int(sudoku1[i][j])==0:
                a.append(9*i+j)
    if len(a)==0:
        return True
    return a

def iterator(i,j,nn):
    sudoku[i][j]=nn
    remover(i,j,nn)
    for itr in range(10):
        for n in range(1,10):
            for i in range(9):
                for j in range(9):
                    if n in pencil[9*i+j]:
                        if naked_single(i,j,n):
                            sudoku[i][j]=n
                        if hidden_single_R(i,j,n):
                            sudoku[i][j]=n
                        if hidden_single_C(i,j,n):
                            sudoku[i][j]=n
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]==0 and len(pencil[9*i+j])==0:
                return False
            else:
                sudoku1=sudoku
                pencil1=pencil
                return True

def abc():
    if zero_checker()==True:
        return True
    else:
        a=[]
        a=zero_checker()
        for n in a:
            i=0
            j=0
            i=n//9
            j=n%9
            if len(pencil[n])==2:
                if iterator(i,j,pencil[n][0]):
                    continue
                else:
                    iterator(i,j,pencil[n][1])
    if zero_checker()==True:
        return True
    else:
        abc()

def solution():
    for n in range(1,10):
        for i in range(9):
            for j in range(9):
                if sudoku[i][j]==0:
                    if pencil_filler(i,j,n):
                        pencil[9*i+j].append(n)
    for itr in range(10):
        for n in range(1,10):
            for i in range(9):
                for j in range(9):
                    if n in pencil[9*i+j]:
                        if naked_single(i,j,n):
                            sudoku[i][j]=n
                        if hidden_single_R(i,j,n):
                            sudoku[i][j]=n
                        if hidden_single_C(i,j,n):
                            sudoku[i][j]=n
        for n in range(1,10):
            for i in range(9):
                for j in range(9):
                    if n in pencil[9*i+j]:
                        naked_pair_R(i,j,n)
                        naked_pair_C(i,j,n)
                        naked_pair_B(i,j,n)
                        pointing_pair(i,j,n)
                        naked_triple_R(i,j,n)
                        naked_triple_C(i,j,n)
                        x_wing_R(i,j,n)
                        x_wing_C(i,j,n)
                        hidden_pair(i,j,n)
    sudoku1=sudoku
    pencil1=pencil
    if abc():
        return sudoku
    return sudoku1

def display():
    sudoku=entry()
    try:
        sol=solution()
    except Exception as e:
        return ee.insert('1.0', "Can't get an answer. ")
    for i in range(9):
        for j in range(9):
            if len(temp[i][j].get('1.0', 'end-1c'))== 0:
                temp[i][j].insert(END, sol[i][j])
                temp[i][j].config(font=('Helvatica','20','italic'))
            else:
                temp[i][j].config(width=2, height=1, font=('Helvetica','20','bold'))

ee=Text(main, bg='yellow', font=("Courier", 10))
ee.grid(row=13, column=0, columnspan=11)
ee.insert(END, 'Enter the digits correctly and click below to solve.')
ee.config(font=("Courier", 10), width=40, height=2)

b1=Button(main, text="SOLVE", width=35, command=display, bg='olive')
b1.grid(row=15, column=0, columnspan=11)

main.mainloop()
