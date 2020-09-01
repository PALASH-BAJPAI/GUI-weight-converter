from tkinter import *      #tkinter is built in module. import all from tinkter
                           #tkinter app=window+widget
                           #run by only python script1.py not by vs run feature
window=Tk()                #window assign

def convert():
    gram=float(e2_value.get())*1000  #kg to gram
    pound=float(e2_value.get())*2.20462  #kg to pound
    ounce=float(e2_value.get())*35.274   #kg to ounce

    #Empty The Text boxes if they had text from previous use and fill them again
    t1.delete("1.0",END)  #Deletes the content of text box from start to end
    t1.insert(END,gram)  #Fill in the box with value of gram variable
    t2.delete("1.0",END)
    t2.insert(END,pound)
    t3.delete("1.0",END)
    t3.insert(END,ounce)

e1=Label(window,text="Input in Kg")
e1.grid(row=0,column=0)             #label is placed in 0,0 in window

e2_value=StringVar()
e2=Entry(window,width=10,textvariable=e2_value)  #creates an entry box for user to enter value
e2.grid(row=0,column=1)

b1=Button(window,text="Convert",width=20,command=convert)
b1.grid(row=0,column=2)

tl1=Label(window,text="         weight in Gram :")
tl1.grid(row=1,column=0)
t1=Text(window,height=1,width=20)
t1.grid(row=1,column=2)

tl2=Label(window,text="          weight in Pound :")
tl2.grid(row=2,column=0)
t2=Text(window,height=1,width=20)
t2.grid(row=2,column=2)

tl3=Label(window,text="          weight in Ounce :")
tl3.grid(row=3,column=0)
t3=Text(window,height=1,width=20)
t3.grid(row=3,column=2)

window.mainloop()           #window ends here , Generate cross buttonto close window