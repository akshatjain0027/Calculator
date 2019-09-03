import tkinter as tk
from tkinter import ttk,messagebox

calculator=tk.Tk()
calculator.title('My Calculator')
calculator.geometry('300x200')

expression=""

def clearall():
    global expression
    entryvar.set("0")
    expression=''

def button_press(pressed_button):
    global expression,back_variable
    expression = expression + str(pressed_button)
    entryvar.set(expression)

def equal_to_function():
    global expression
    try:
        value=str(eval(expression))
        entryvar.set(value)
        expression=''
    except:
        messagebox.showerror('Error','Check your expression')

def back_button_function():
    global expression
    expression=expression[0:len(expression)-1]
    entryvar.set(expression)
            

# creating entry screen
entryvar=tk.StringVar()
entrybox=tk.Entry(calculator,width=50,state='readonly',textvariable=entryvar,fg='blue')
entrybox.pack(side=tk.TOP,fill=tk.Y)
entryvar.set('0')

#creating labelframe
labelframe=tk.LabelFrame(calculator,background='black')
labelframe.pack(fill=tk.BOTH,expand=True)

# clear all and backspace buttons
clear_all_button=ttk.Button(labelframe,text='AC',command=clearall)
clear_all_button.grid(row=0,column=0,padx=2,pady=2)

back_button=ttk.Button(labelframe, text='<--',command=back_button_function)
back_button.grid(row=0,column=1,padx=2,pady=2)


#### number buttons
button1=ttk.Button(labelframe,text='1')
button1.grid(row=1,column=0,padx=2,pady=2)
button1.configure(command=lambda:button_press(1))

button2=ttk.Button(labelframe,text='2')
button2.grid(row=1,column=1,padx=2,pady=2)
button2.configure(command=lambda:button_press(2))

button3=ttk.Button(labelframe,text='3',command=lambda:button_press(3))
button3.grid(row=1,column=2,padx=2,pady=2)

button4=ttk.Button(labelframe,text='4',command=lambda:button_press(4))
button4.grid(row=2,column=0,padx=2,pady=2)

button5=ttk.Button(labelframe,text='5',command=lambda:button_press(5))
button5.grid(row=2,column=1,padx=2,pady=2)

button6=ttk.Button(labelframe,text='6',command=lambda:button_press(6))
button6.grid(row=2,column=2,padx=2,pady=2)

button7=ttk.Button(labelframe,text='7',command=lambda:button_press(7))
button7.grid(row=3,column=0,padx=2,pady=2)

button8=ttk.Button(labelframe,text='8',command=lambda:button_press(8))
button8.grid(row=3,column=1,padx=2,pady=2)

button9=ttk.Button(labelframe,text='9',command=lambda:button_press(9))
button9.grid(row=3,column=2,padx=2,pady=2)

button0=ttk.Button(labelframe,text='0',command=lambda:button_press(0))
button0.grid(row=4,column=1,padx=2,pady=2)

button00=ttk.Button(labelframe,text='00',command=lambda:button_press('00'))
button00.grid(row=4,column=0,padx=2,pady=2)

# dot button
dot_button=ttk.Button(labelframe,text='.',command=lambda:button_press('.'))
dot_button.grid(row=0,column=2,padx=2,pady=2)

#operators buttons
percent_button=ttk.Button(labelframe,text='%')
percent_button.grid(row=4,column=2,padx=2,pady=2)

add_button=ttk.Button(labelframe,text='+',width=7,command=lambda:button_press('+'))
add_button.grid(row=0,column=3,padx=2,pady=2)

subtract_button=ttk.Button(labelframe,text='-',width=7,command=lambda:button_press('-'))
subtract_button.grid(row=1,column=3,padx=2,pady=2)

divide_button=ttk.Button(labelframe,text='/',width=7,command=lambda:button_press('/'))
divide_button.grid(row=2,column=3,padx=2,pady=2)

multiply_button=ttk.Button(labelframe,text='x',width=7,command=lambda:button_press('*'))
multiply_button.grid(row=3,column=3,padx=2,pady=2)

equal_to_button=ttk.Button(labelframe,text='=',width=7,command=equal_to_function)
equal_to_button.grid(row=4,column=3,padx=2,pady=2)




calculator.mainloop()
