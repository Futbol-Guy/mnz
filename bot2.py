from Tkinter import *
import schedule
import time
from PIL import ImageTk, Image
import os
import Tkinter as tk
from PIL import ImageTk, Image
import webbrowser



def complete():
        
    root = Tk()
    root.title("IT'S ME AGAIN!!!")
    root.attributes("-fullscreen", True)
    
    def url():
        webbrowser.open("https://virtuallearning.instructure.com/") 
        
        
    def quit():
            self.root.destroy()    
        
    def whole1():
            
        def work1():
            labelfont = ('times', 15, 'bold')
            widget = Label(root, text='DID YOU THINK I WOULD JUST LET YOU BETRAY ME LIKE THAT?')
            widget.config(bg='black', fg='yellow')  
            widget.config(font=labelfont)           
            widget.config(height=2, width=20)       
            widget.pack(expand=NO, fill=BOTH)
           
        def again1():
            labelfont = ('times', 35, 'bold')
            widget = Label(root, text='NOPE, NO ONE MESSES WITH ME!!!')
            widget.config(bg='black', fg='yellow')  
            widget.config(font=labelfont)           
            widget.config(height=1, width=20)       
            widget.pack(expand=NO, fill=BOTH)
        
        work1()
        again1()
        
        path = '/home/mm/Desktop/icon1.jpg'
        img = ImageTk.PhotoImage(Image.open(path))
        panel = tk.Label(root, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "no")
        
        
        root.mainloop()
        
    
    def joke1():
        button = tk.Button(root, text='Stop Bugging Me!!!', width=25, command=url)
        button.pack({"side": "bottom"})
        button1 = tk.Button(root, text='Fine, I will get back to work', width=25, command=root.withdraw)
        button1.pack({"side": "bottom"})
        whole1()
        time.sleep(10)
        quit()
    
    
    joke1()

    while True:
        schedule.run_pending()
        time.sleep(1)
        
complete()
time.sleep(40)
complete()
        
