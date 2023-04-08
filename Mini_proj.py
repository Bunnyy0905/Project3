from tkinter import *
from tkinter import messagebox
import string   #string module contains a number of functions to process the standard python string
import random #random module can generate random numbers
import pyperclip  #pyperclip module allows us to copy and paste text to and from the clipboard to your computer
equation=""
def generator():
    alpha=string.ascii_letters  #will return all the small alphabets from a-z with the help of string module
    # calpha=string.ascii_uppercase   #will return all the capital alphabets from A-Z
    num=string.digits #will return all the numbers from 0-9
    # punctuation=string.punctuation  #will return all the spcl characters
    punctuation="!@#$%^&*()<>"
    comb=alpha+num+punctuation

    pass_len= int(box.get()) #will return whatever the user enters the length of the pass
    # print(pass_len)
    # password=random.sample(comb, pass_len)#used to generate a password randomly
    # passfield.insert(0,password)#display the password in the field
    if choice.get()==1:
        passfield.insert(0, random.sample(alpha,pass_len))
    if choice.get()==2:
        passfield.insert(0, random.sample(alpha+num,pass_len))
    if choice.get()==3:
        passfield.insert(0, random.sample(comb,pass_len))
    
def clear():
    global equation     #declaring a global variable inside a function 
    equation=""         #changing value of global variable in a local context
    passfield.config(text=equation)

def copy():
    # value=messagebox.askquestion("Information", "Are you sure you want to copy the Password")
    # if value=="yes":
    #     msg="Great! Password Copied"
    # else:
    #     msg="Ohhk! As your wish"
    # messagebox.showinfo("Result", msg)

    random_pass=passfield.get()
    pyperclip.copy(random_pass)

root=Tk()
root.title("Random Password Generator") #title() set the title of the window
root.geometry("300x500")    #geometry() set the width and height of the window
root.resizable(0,0) #resizable(0,0) set the fixed size of the window
# root.maxsize(300,550) 
root.config(bg="gold")

Font=("arial", 15, "bold")

# gray20
passlabel=Label(root,text="Password Generator", bg="gold",fg="black",font=("times new roman", 25, "bold"))
passlabel.grid(pady=10)
choice=IntVar()
wradio=Radiobutton(root,text="Weak",font=Font, variable=choice, value=1)
wradio.grid(pady=5)
mradio=Radiobutton(root,text="Medium",font=Font, variable=choice, value=2)
mradio.grid(pady=5)
sradio=Radiobutton(root,text="Strong",font=Font, variable=choice, value=3)
sradio.grid(pady=5)

lenlabel=Label(root,text="Password Length", bg="gold",fg="black",font=Font)
lenlabel.grid(pady=5)

box=Spinbox(root,from_=5, to=10, font=Font, width=5)
box.grid(pady=5)

genbutton=Button(root,text="Generate",font=Font, command=generator)
genbutton.grid(pady=5)

passfield=Entry(root, font=Font,width=15,fg="violet")
passfield.grid(pady=5)

copybutton=Button(root,text="Copy",font=Font, command=copy())
copybutton.grid(pady=5)

clearbutton=Button(root,text="Clear",font=Font, command=clear())
clearbutton.grid(pady=5)

Button(root, text="Exit", bg="red", font=Font,command=root.destroy).grid()
root.mainloop()
