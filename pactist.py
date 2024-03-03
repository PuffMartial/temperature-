from tkinter import *

def submit():
    print("the temperature is: "+ str(scale.get())+ "degrees C")

window = Tk()

scale = Scale(window,from_=100,to=0,length=600,orient=VERTICAL,tickinterval=10,showvalue=0,)
scale.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()