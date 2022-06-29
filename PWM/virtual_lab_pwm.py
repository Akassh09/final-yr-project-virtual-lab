from tkinter import *
from tkinter import filedialog as fd             #filedialog library is for selecting the file from a directory
import numpy as np                               #numpy library is for number representation
import matplotlib.pyplot as plt                  #matplotlib is for ploting
from scipy import signal                         #scipy is for waveform generation (Scientific Python)


def simulate():
    p=float(spb1.get())
    r1=0.5*x.get()
    r2=5.0
    c=0.01
    th=0.7*(r1+r2)*c
    tt=0.7*(r1+(2*r2))*c
    dc=th/tt
    freq=np.reciprocal(tt)
    lbl1.config(text=str(p))
    lbl2.config(text=str(round(freq,2)))
    lbl3.config(text=str(round(dc*100,2)))
    a=np.arange(0,5,0.01)
    b=p*signal.square(5*a,duty=dc)
    plt.plot(a,b)
    plt.show()

tk=Tk()
tk.title("Pulse Width Modulation using 555 Timer")
tk.geometry("1200x700")
#fg=fd.askopenfilename()                                            #Code for selecting files from directory
fg = 'pwm.png'
fig=PhotoImage(file='pwm.png')                                           #Code for opening the image file
Label(tk,image=fig,height=400,width=800).grid(row=0,column=1)      #Code for displaying image in label
Label(tk,text="Set Amplitude:").grid(row=1,column=0)
spb1=Spinbox(tk,from_=1,to=10)                                        #Spinbox creation for amplitude selection
spb1.grid(row=1,column=1)
Label(tk,text="Set Input Signal to vary R1:").grid(row=2,column=0)
x=DoubleVar()
sld=Scale(tk,from_=0.1,to=10,resolution=0.1,variable=x,length=300,orient=HORIZONTAL)   #Slider is to select R1
sld.grid(row=2,column=1)
Button(tk,text="Simulate",command=simulate).grid(row=3,column=1)      #Button is for simulation
Label(tk,text="Amplitude (Volt):").grid(row=4,column=0)
lbl1=Label(tk,text="NONE")
lbl1.grid(row=4,column=1)
Label(tk,text="Frequency (KHz):").grid(row=4,column=2)
lbl2=Label(tk,text="NONE")
lbl2.grid(row=4,column=3)
Label(tk,text="Duty Cycle (%):").grid(row=5,column=1)
lbl3=Label(tk,text="NONE")
lbl3.grid(row=5,column=2)
tk.mainloop()
