from Tkinter import *
import schedule
import time
from PIL import ImageTk, Image
import os
import Tkinter as tk
from PIL import ImageTk, Image
import webbrowser

    
root = Tk()
root.title("GUESS WHO?")
root.attributes("-fullscreen", True)

def url():
    webbrowser.open("https://virtuallearning.instructure.com/") 
def close_window(): 
    root.destroy()
    
def whole():
    
    
    def work():
        labelfont = ('times', 30, 'bold')
        widget = Label(root, text='GET BACK TO WORK, NOW')
        widget.config(bg='black', fg='yellow')  
        widget.config(font=labelfont)           
        widget.config(height=2, width=20)       
        widget.pack(expand=NO, fill=BOTH)
        
    
    def again():
        labelfont = ('times', 50, 'bold')
        widget = Label(root, text='EVEN HE AGREES')
        widget.config(bg='black', fg='yellow')  
        widget.config(font=labelfont)           
        widget.config(height=1, width=20)       
        widget.pack(expand=NO, fill=BOTH)
    
    
    work()
    again()
    
    path = '/home/mm/Desktop/icon.jpg'
    img = ImageTk.PhotoImage(Image.open(path))
    panel = tk.Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "no")
    
    
    root.mainloop()
    

def joke():
    #schedule.every(0.066).minutes.do(whole)
    button = tk.Button(root, text='Stop Bugging Me!!!', width=25, command=url)
    button.pack({"side": "bottom"})
    button = tk.Button(root, text='Fine, I will get back to work', width=25, command=root.destroy)
    button.pack({"side": "bottom"})
    whole()

joke()
joke()
joke()

while True:
    schedule.run_pending()
    time.sleep(1)
    
