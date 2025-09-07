from tkinter import *
import tkinter.messagebox as tkmess

def calculate(equal):
    result = eval(user.get())
    user.set(result)
    
def show(key):
    current =user.get()
    user.set(current+ str(key))
    
def erase():
    user.set("")


root = Tk()

canvasWidth =  325
canvasHeight = 550
root.geometry(f"{canvasWidth}x{canvasHeight}")
root.title("calculater")

user = StringVar()
userentry = Entry(root, textvariable=user, width=40, font="Helvetica 50", justify=RIGHT, relief=SUNKEN)
userentry.pack(ipady=50)

frame = Frame(root, background="black" , borderwidth=20, relief=SUNKEN ,height=400 , width=200, pady=10 )
frame.pack(fill=BOTH, expand=TRUE)

Button_1 = Button(frame , background="skyblue",text="1", command=lambda x="1" : show("1"))
Button_1.grid(row=0, column=0, ipadx=25, ipady=15, padx=2, pady=2)
Button_2 = Button(frame , background="skyblue",text="2", command=lambda x="2" : show("2"))
Button_2.grid(row=0, column=1, ipadx=25, ipady=15, padx=2, pady=2)
Button_3 = Button(frame , background="skyblue",text="3", command=lambda x="3" : show("3"))
Button_3.grid(row=0, column=2, ipadx=25, ipady=15, padx=2, pady=2)
Button_4 = Button(frame , background="skyblue",text="4", command=lambda x="4" : show("4"))
Button_4.grid(row=1, column=0, ipadx=25, ipady=15, padx=2, pady=2)
Button_5 = Button(frame , background="skyblue",text="5", command=lambda x="5" : show("5"))
Button_5.grid(row=1, column=1, ipadx=25, ipady=15, padx=2, pady=2)
Button_6 = Button(frame , background="skyblue",text="6", command=lambda x="6" : show("6"))
Button_6.grid(row=1, column=2, ipadx=25, ipady=15, padx=2, pady=2)
Button_7 = Button(frame , background="skyblue",text="7", command=lambda x="7" : show("7"))
Button_7.grid(row=2, column=0, ipadx=25, ipady=15, padx=2, pady=2)
Button_8 = Button(frame , background="skyblue",text="8", command=lambda x="8" : show("8"))
Button_8.grid(row=2, column=1, ipadx=25, ipady=15, padx=2, pady=2)
Button_9 = Button(frame , background="skyblue",text="9", command=lambda x="9" : show("9"))
Button_9.grid(row=2, column=2, ipadx=25, ipady=15, padx=2, pady=2)
Button_0 = Button(frame , background="skyblue",text="0", command=lambda x="0" : show("0"))
Button_0.grid(row=3, column=1, ipadx=25, ipady=15, padx=2, pady=2)
Button_add = Button(frame , background="orange", text="+", command=lambda x="+" : show("+"))
Button_add.grid(row=0, column=3, ipadx=25, ipady=15, padx=2, pady=2)
Button_sub = Button(frame , background="orange", text="-", command=lambda x="-" : show("-"))
Button_sub.grid(row=1, column=3, ipadx=25, ipady=15 , padx=2, pady=2)
Button_mul = Button(frame , background="orange", text="X", command=lambda x="x" : show("*"))
Button_mul.grid(row=2, column=3, ipadx=25, ipady=15, padx=2, pady=2)
Button_div = Button(frame , background="orange",text="/", command=lambda x="/" : show("/"))
Button_div.grid(row=3, column=3, ipadx=25, ipady=15, padx=2, pady=2)
Button_decimal = Button(frame , background="orange",text=".", command=lambda x="." : show("."))
Button_decimal.grid(row=3, column=0, ipadx=25, ipady=15, padx=2, pady=2)
Button_erase = Button(frame , background="red", text="C", command=lambda x="C" : erase())
Button_erase.grid(row=4,column=0, columnspan=4, rowspan=4, ipadx=25, ipady=15, padx=2, pady=2)
Button_equal = Button(frame , bg="green",text="=", command=lambda x="=" : calculate(user.set))
Button_equal.grid(row=3, column=2, ipadx=25, ipady=15, padx=2, pady=2)

root.mainloop()