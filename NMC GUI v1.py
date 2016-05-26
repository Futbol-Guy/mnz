#--------------------------------

# NMC GUI v1.2

# 

# NOTE: You will have to quit the program to see the values printed properly. Either that or press the button twice

#

#--------------------------------------------


from Tkinter import *
from PIL import ImageTk, Image
import tkFont
import webbrowser
import schedule
import time
import sys
import subprocess

def centre_screen(root):
        # get screen width and height
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight() 
        
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (500)
        y = (hs/2) - (350)
        
        root.geometry('%dx%d+%d+%d' % (1000, 700, x, y))        

class Start_UI:
                                
                
        def __init__(self, root):
                root.maxsize(width=1000,height=700)
                root.minsize(width=1000,height=700)
                centre_screen(root)
                
                #creating methods to change the image when the mouse hovers over
                def monday_L(event, pic):
                        label_monday.config(image= pic)
                                                    
                def tuesday_L(event, pic):
                        label_tuesday.config(image= pic)
                                        
                def wednesday_L(event, pic):
                        label_wednesday.config(image= pic)
                                            
                def thursday_L(event, pic):
                        label_thursday.config(image= pic)
                                
                def friday_L(event, pic):
                        label_friday.config(image= pic)                
                
                def lift_monday(event):
                        image= PhotoImage(file="Images\Mon Art.gif")
                        monday_main = Toplevel(root_main)
                        m = Days_UI(monday_main,image)
                        m.name = "Monday" 
                
                def lift_tuesday(event):                       
                        image= PhotoImage(file="Images\Tues Art.gif")
                        monday_main = Toplevel(root_main)
                        m = Days_UI(monday_main, image)
                
                def lift_wednesday(event):                       
                        image= PhotoImage(file="Images\Wed Art.gif")
                        monday_main = Toplevel(root_main)
                        m = Days_UI(monday_main, image)
                
                def lift_thursday(event):                       
                        image= PhotoImage(file="Images\Thurs Art.gif")
                        monday_main = Toplevel(root_main)
                        m = Days_UI(monday_main, image)
                
                def lift_friday(event):                       
                        image= PhotoImage(file="Images\Fri Art.gif")
                        monday_main = Toplevel(root_main)
                        m = Days_UI(monday_main, image)                
                        
                root.title("Never Miss A Class")
                        
                #Getting the default pictures
                nl_mon_pic = PhotoImage(file="Images\MS_NL_Mon.gif")
                nl_tues_pic = PhotoImage(file="Images\MS_NL_Tues.gif")
                nl_wed_pic = PhotoImage(file="Images\MS_NL_Wed.gif")
                nl_thurs_pic = PhotoImage(file="Images\MS_NL_Thurs.gif")
                nl_fri_pic = PhotoImage(file="Images\MS_NL_Fri.gif")
                #Lightning Pics
                l_mon_pic = PhotoImage(file="Images\MS_L_Mon.gif")    
                l_tues_pic = PhotoImage(file="Images\MS_L_Tues.gif")
                l_wed_pic = PhotoImage(file="Images\MS_L_Wed.gif")
                l_thurs_pic = PhotoImage(file="Images\MS_L_Thurs.gif")
                l_fri_pic = PhotoImage(file="Images\MS_L_Fri.gif")
                
                #creating a label for each image        
                label_monday = Label(root, image= nl_mon_pic, borderwidth = 0, highlightthickness= 0)
                label_monday.grid(row=0)
                #changing what the label does when it is hovered over or clicked.
                label_monday.bind("<Enter>", lambda event: monday_L(event, l_mon_pic))
                label_monday.bind("<Leave>", lambda event: monday_L(event, nl_mon_pic))
                label_monday.bind("<Button-1>", lift_monday)
                #schedule.every().monday.at("11:16").do(webbrowser.open("www.virtuallearning.ca"))
                        
                label_tuesday = Label(root, image= nl_tues_pic, borderwidth = 0, highlightthickness= 0)
                label_tuesday.grid(row=0, column= 1)
                label_tuesday.bind("<Enter>", lambda event: tuesday_L(event, l_tues_pic))
                label_tuesday.bind("<Leave>", lambda event: tuesday_L(event, nl_tues_pic))
                label_tuesday.bind("<Button-1>", lift_tuesday)
                        
                label_wednesday = Label(root, image= nl_wed_pic, borderwidth = 0, highlightthickness= 0)
                label_wednesday.grid(row=0, column= 2)
                label_wednesday.bind("<Enter>", lambda event: wednesday_L(event, l_wed_pic))
                label_wednesday.bind("<Leave>", lambda event: wednesday_L(event, nl_wed_pic))
                label_wednesday.bind("<Button-1>", lift_wednesday)
                        
                label_thursday = Label(root, image= nl_thurs_pic, borderwidth = 0, highlightthickness= 0)
                label_thursday.grid(row=0, column= 3)
                label_thursday.bind("<Enter>", lambda event: thursday_L(event, l_thurs_pic))
                label_thursday.bind("<Leave>", lambda event: thursday_L(event, nl_thurs_pic))
                label_thursday.bind("<Button-1>", lift_thursday)
                        
                label_friday = Label(root, image= nl_fri_pic, borderwidth = 0, highlightthickness= 0)
                label_friday.grid(row=0, column= 4)
                label_friday.bind("<Enter>", lambda event: friday_L(event, l_fri_pic))
                label_friday.bind("<Leave>", lambda event: friday_L(event, nl_fri_pic))
                label_friday.bind("<Button-1>", lift_friday)
                
                



#All the days will be created as objects here. I will implement that after I finish formatting the grid layout properly        
class Days_UI:
        
                
        def __init__(self, root,bg_image):
                #webbrowser.open("www.virtuallearning.ca")  
                centre_screen(root)
                root.title("Never Miss A Class")
                root.maxsize(width=1000,height=700)
                root.minsize(width=1000,height=700)
                
                #setting a font
                helv36 = tkFont.Font(family='Helvetica',
                size=36, weight='bold')  
                
                
                
                self.main_canvas = Canvas(root,width=1000,height=700, highlightthickness=0)
                self.main_canvas.grid(row=0, column=0)
                
                self.main_canvas.create_image(0,0,anchor=NW, image=bg_image)
                self.main_canvas.image=bg_image              
                     
                        
                time_tuple = ("1 AM","2 AM","3 AM","4 AM","5 AM","6 AM","7 AM","9 AM","10 AM","11 AM","12 AM","1 PM","2 PM","3 PM","4 PM","5 PM","6 PM","7 PM","9 PM","10 PM","11 PM","12 PM")
                
                #Placing the buttons.
                                
                self.default_button = Button(self.main_canvas, text="Set Defaults",command= self.set_values)
                self.default_button.place(x=250,y=550)
                self.save_button = Button(self.main_canvas, text="Save Values",command= self.save_values)
                self.save_button.place(x=350,y=550)
                self.read_button = Button(self.main_canvas, text="Read Values",command= self.read_values)
                self.read_button.place(x=450,y=550)
                self.home_button = Button(self.main_canvas, text="Back to Home Screen",command= self.lift_main(root))
                self.home_button.place(x=600,y=550)                
                
                #Creting the text
                self.main_canvas.create_text(80,80, text = "Enter the time, name and URL of each class. Then click 'Save Changes'. ",anchor=NW,font='helv36')
                self.main_canvas.create_text(250,200, text = "Class 1",anchor=NW,font='helv36')  
                self.main_canvas.create_text(250,250, text = "Class 2",anchor=NW,font='helv36')
                self.main_canvas.create_text(250,300, text = "Class 3",anchor=NW,font='helv36')
                self.main_canvas.create_text(250,350, text = "Class 4",anchor=NW,font='helv36')
                self.main_canvas.create_text(250,400, text = "Class 5",anchor=NW,font='helv36')
                self.main_canvas.create_text(250,450, text = "Class 6",anchor=NW,font='helv36')
                
                #Initializing spinners
                
                self.spinner1 = Spinbox(self.main_canvas, values=time_tuple ,width=5)
                self.spinner1.place(x=350,y=200)                  
                self.spinner2 = Spinbox(self.main_canvas, values=time_tuple,width=5)
                self.spinner2.place(x=350,y=250) 
                self.spinner3 = Spinbox(self.main_canvas, values=time_tuple,width=5)
                self.spinner3.place(x=350,y=300)   
                self.spinner4 = Spinbox(self.main_canvas, values=time_tuple,width=5)
                self.spinner4.place(x=350,y=350) 
                self.spinner5 = Spinbox(self.main_canvas, values=time_tuple,width=5)
                self.spinner5.place(x=350,y=400)   
                self.spinner6 = Spinbox(self.main_canvas, values=time_tuple,width=5)
                self.spinner6.place(x=350,y=450)                 
                
                #Initializing text boxes
                self.entry1 = Entry(self.main_canvas,width = 30)
                self.entry1.place(x=400,y=200)
                self.entry2 = Entry(self.main_canvas,width = 30)
                self.entry2.place(x=400,y=250)
                self.entry3 = Entry(self.main_canvas,width = 30)
                self.entry3.place(x=400,y=300)
                self.entry4 = Entry(self.main_canvas,width = 30)                
                self.entry4.place(x=400,y=350)
                self.entry5 = Entry(self.main_canvas,width = 30)
                self.entry5.place(x=400,y=400)
                self.entry6 = Entry(self.main_canvas,width = 30)                
                self.entry6.place(x=400,y=450)                
                
                                
        
        def lift_main(self,root):
                root.attributes("-topmost", True)
                
        #writes the values of all text fields and spinners to a file
        def save_values(self):
                self.get_spinner()
                self.get_text()
                li = [[self.in_textbox1, self.in_textbox2, self.in_textbox3, self.in_textbox4, self.in_textbox5, self.in_textbox6], 
                      [self.in_spin1, self.in_spin2, self.in_spin3, self.in_spin4, self.in_spin5, self.in_spin6]]               
                f = open(self.name + ".txt", "w") # Change this so the file is named based on the object
                for row in li:
                        for item in row:
                                f.write(str(item) + "|") # is str(item) necessary?
                        f.write("\n")
                f.close()
                     
        #reads the values of text values and spinners from a file
        def read_values(self):
                f = open(self.name + ".txt", "r") # Change this so the file is named based on the object
                li = []
                for line in f:
                        li.append(line.strip("\n").split("|"))
                f.close()
                #remove the empty string at the last index of both rows caused by the last item's pipe
                for row in li:
                        row.remove(row[-1])
                print li 
                #assign the values back to the object
                self.in_textbox1 = li[0][0]
                self.in_textbox2 = li[0][1]
                self.in_textbox3 = li[0][2]
                self.in_textbox4 = li[0][3]
                self.in_textbox5 = li[0][4]
                self.in_textbox6 = li[0][5]
                
                self.in_spin1 = li[1][0]
                self.in_spin2 = li[1][1]
                self.in_spin3 = li[1][2]
                self.in_spin4 = li[1][3]
                self.in_spin5 = li[1][4]
                self.in_spin6 = li[1][5]
                
        #Test method to print the values that you inputted.        
        def print_values(self):
                self.get_spinner()
                self.get_text()
                print self.in_spin1,self.in_spin2,self.in_spin3,self.in_spin4
                print self.in_textbox1,self.in_textbox2,self.in_textbox3,self.in_textbox4
        
        #getting the spinner values
        def get_spinner(self):
                self.in_spin1 = self.spinner1.get()
                self.in_spin2 = self.spinner2.get()
                self.in_spin3 = self.spinner3.get()
                self.in_spin4 = self.spinner4.get()
                self.in_spin5 = self.spinner5.get()
                self.in_spin6 = self.spinner6.get()
        
        #getting the text entries      
        def get_text(self):
                self.in_textbox1 = self.entry1.get()
                self.in_textbox2 = self.entry2.get()
                self.in_textbox3 = self.entry3.get()
                self.in_textbox4 = self.entry4.get()
                self.in_textbox5 = self.entry5.get()
                self.in_textbox6 = self.entry6.get()
                        
        def set_values(self):
                #Fills the appropriate values to the text boxes and spinners
                self.spinner1.delete(0,"end")
                self.spinner1.insert(0,self.in_spin1)
                self.entry1.delete(0,END)
                self.entry1.insert(0,self.in_textbox1)
                self.spinner2.delete(0,"end")
                self.spinner2.insert(0,self.in_spin2)
                self.entry2.delete(0,END)
                self.entry2.insert(0,self.in_textbox2)
                self.spinner3.delete(0,"end")
                self.spinner3.insert(0,self.in_spin3)
                self.entry3.delete(0,END)
                self.entry3.insert(0,self.in_textbox3)      
                self.spinner4.delete(0,"end")
                self.spinner4.insert(0,self.in_spin4)
                self.entry4.delete(0,END)
                self.entry4.insert(0,self.in_textbox4)
                self.spinner5.delete(0,"end")
                self.spinner5.insert(0,self.in_spin5)
                self.entry5.delete(0,END)
                self.entry5.insert(0,self.in_textbox5)  
                self.spinner6.delete(0,"end")
                self.spinner6.insert(0,self.in_spin6)
                self.entry6.delete(0,END)
                self.entry6.insert(0,self.in_textbox6)                   
                
root_main = Tk()

s = Start_UI(root_main)
#m.get_spinner() commented this out for now because it breaks read_values()
root_main.mainloop()