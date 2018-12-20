from Tkinter import *
import ast

def buttonClick(numbers):
    global operator
    operator = operator+str(numbers)
    text_input.set(operator)

def cleardisplay():
    global operator
    operator=''
    text_input.set('')

def equals():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)

cal = Tk()
cal.title("Calculator")
operator=""
text_input=StringVar()


textDisplay = Entry(cal,font=('arial',20,'bold'),textvariable=text_input,bd=15,insertwidth=4,
                    bg='light blue',justify='right').grid(columnspan=4)

#buttons in grid
btn7=Button(cal,padx=15,bd=5,fg='black',font=('arial',20,'bold'),text='7',bg='light blue',command=lambda :buttonClick(7)).grid(row=1,column=0)
btn8=Button(cal,padx=15,bd=5,fg='black',font=('arial',20,'bold'),text='8',bg='light blue',command=lambda :buttonClick(8)).grid(row=1,column=1)
btn9=Button(cal,padx=15,bd=5,fg='black',font=('arial',20,'bold'),text='9',bg='light blue',command=lambda :buttonClick(9)).grid(row=1,column=2)
btn6=Button(cal,padx=15,bd=5,fg='black',font=('arial',20,'bold'),text='6',bg='light blue',command=lambda :buttonClick(6)).grid(row=2,column=0)
btn5=Button(cal,padx=15,bd=5,fg='black',font=('arial',20,'bold'),text='5',bg='light blue',command=lambda :buttonClick(5)).grid(row=2,column=1)
btn4=Button(cal,padx=15,bd=5,fg='black',font=('arial',20,'bold'),text='4',bg='light blue',command=lambda :buttonClick(4)).grid(row=2,column=2)
btn3=Button(cal,padx=15,bd=5,fg='black',font=('arial',20,'bold'),text='3',bg='light blue',command=lambda :buttonClick(3)).grid(row=3,column=0)
btn2=Button(cal,padx=15,bd=5,fg='black',font=('arial',20,'bold'),text='2',bg='light blue',command=lambda :buttonClick(2)).grid(row=3,column=1)
btn1=Button(cal,padx=15,bd=5,fg='black',font=('arial',20,'bold'),text='1',bg='light blue',command=lambda :buttonClick(1)).grid(row=3,column=2)
btnAdd=Button(cal,padx=15,bd=5,fg='black',font=('arial',20,'bold'),text='+',bg='light blue',command=lambda :buttonClick('+')).grid(row=1,column=3)
btnSub=Button(cal,padx=18,bd=5,fg='black',font=('arial',20,'bold'),text='-',bg='light blue',command=lambda :buttonClick('-')).grid(row=2,column=3)
btnMul=Button(cal,padx=15,bd=5,fg='black',font=('arial',20,'bold'),text='X',bg='light blue',command=lambda :buttonClick('*')).grid(row=3,column=3)
btnDiv=Button(cal,padx=18,bd=5,fg='black',font=('arial',20,'bold'),text='/',bg='light blue',command=lambda :buttonClick('/')).grid(row=4,column=3)
btnClear=Button(cal,padx=15,bd=5,fg='black',font=('arial',20,'bold'),text='C',bg='light blue',command=lambda :cleardisplay()).grid(row=4,column=0)
btnEqual=Button(cal,padx=15,bd=5,fg='black',font=('arial',20,'bold'),text='=',bg='light blue',command=lambda :equals()).grid(row=4,column=2)
btnZero=Button(cal,padx=15,bd=5,fg='black',font=('arial',20,'bold'),text='0',bg='light blue',command=lambda :buttonClick(0)).grid(row=4,column=1)
#buttons added

cal.mainloop() #method is for blocking . waits for an event and updates the gui

