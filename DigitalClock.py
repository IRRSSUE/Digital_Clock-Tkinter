#Import 
from tkinter import Label, Tk 
import time

#Making Window
app_window = Tk() 
app_window.title("Digital Clock") 
app_window.geometry("420x150") 
app_window.resizable(1,1)

#Creating UI interface
text_font= ("Boulder", 68, 'bold')
background = "#819de6"
foreground= "#050a09"
border_width = 25

#calling back data base
label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

#definding object
def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, digital_clock)


#final mainloop
digital_clock()
app_window.mainloop()
