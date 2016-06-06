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
import datetime
import sys
import subprocess
import re
import tkMessageBox

def centre_screen(root):
        # get screen width and height
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight() 
        
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (500)
        y = (hs/2) - (350)
        
        root.geometry('%dx%d+%d+%d' % (1000, 700, x, y))        

class Help_UI:
        def __init__(self,root,bg_image):
                #setting a font
                self.customFont_small = tkFont.Font(family="Minecraft", size=10) 
                
                root.title("Never Miss A Class")
                root.maxsize(width=1000,height=700)
                root.minsize(width=1000,height=700)                
                centre_screen(root)
                
                help_1 = PhotoImage(file="Images\Help 1.gif")
                help_2 = PhotoImage(file="Images\Help 2.gif")
                help_3 = PhotoImage(file="Images\Help 3.gif")
                help_4 = PhotoImage(file="Images\Help 4.gif")                
                
                self.main_canvas = Canvas(root,width=1000,height=700, highlightthickness=0)
                self.main_canvas.grid(row=0, column=0)
                                
                self.main_canvas.create_image(0,0,anchor=NW, image=bg_image)
                self.main_canvas.image=bg_image  
                
                self.main_canvas.create_text(20,90, text = "Welcome to Never Miss a Class! To get started, click what day you have",anchor=NW,font=self.customFont_small)
                self.main_canvas.create_text(270,110, text = " a class on.",anchor=NW,font=self.customFont_small) 
                self.main_canvas.create_text(20,450, text = "Next, select the time your class starts. This program will launch the class ",anchor=NW,font=self.customFont_small)
                self.main_canvas.create_text(20,470, text = "Five minutes before the time that you select.",anchor=NW,font=self.customFont_small)
                self.main_canvas.create_text(20,470, text = "Next, get the class URL. ",anchor=NW,font=self.customFont_small)
                
                
                self.h1_canvas = Canvas(self.main_canvas,width=250,height=336, highlightthickness=0)
                self.h1_canvas.place(x=20,y=110)
                self.h1_canvas.create_image(0,0,image=help_1,anchor=NW)
                self.h1_canvas.image = help_1
                self.h2_canvas = Canvas(self.main_canvas,width=478,height=160, highlightthickness=0)
                self.h2_canvas.place(x=20,y=490)
                self.h2_canvas.create_image(0,0,image=help_2,anchor=NW)
                self.h2_canvas.image = help_2
                self.h3_canvas = Canvas(self.main_canvas,width=250,height=153, highlightthickness=0)
                self.h3_canvas.place(x=520,y=110)
                self.h3_canvas.create_image(0,0,image=help_3,anchor=NW)
                self.h3_canvas.image = help_3
                self.h4_canvas = Canvas(self.main_canvas,width=350,height=174, highlightthickness=0)
                self.h4_canvas.place(x=520,y=400)
                self.h4_canvas.create_image(0,0,image=help_4,anchor=NW)
                self.h4_canvas.image = help_4                
                
                self.main_B = Button(self.main_canvas, text = "Back to Home Screen",command= root.destroy,font=self.customFont_small)
                self.main_B.place(x=20,y=660)
                

class Start_UI:
                                
                
        def __init__(self, root):
                root.title("Never Miss A Class")
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
                
                def btuesday_L(event,pic):
                        label_btues.config(image=pic)
                
                def bthursday_L(event,pic):
                        label_bthur.config(image=pic)
                
                def lift_monday(event):
                        image= PhotoImage(file="Images\Mon Art.gif")
                        main = Toplevel(root_main)
                        m = Days_UI(main,image,"Monday")
                
                def lift_tuesday(event):                       
                        image= PhotoImage(file="Images\Tues Art.gif")
                        main = Toplevel(root_main)
                        t = Days_UI(main, image,"Tuesday")
                
                def lift_wednesday(event):                       
                        image= PhotoImage(file="Images\Wed Art.gif")
                        main = Toplevel(root_main)
                        w = Days_UI(main, image,"Wednesday")
                
                def lift_thursday(event):                       
                        image= PhotoImage(file="Images\Thurs Art.gif")
                        main = Toplevel(root_main)
                        th = Days_UI(main, image,"Thursday")
                
                def lift_friday(event):                       
                        image= PhotoImage(file="Images\Fri Art.gif")
                        main = Toplevel(root_main)
                        f = Days_UI(main, image,"Friday")
                
                def lift_help(event):
                        image= PhotoImage(file="Images\Help Art.gif")
                        main = Toplevel(root_main)
                        help = Help_UI(main,image)
                        
                def test_function(event):
                        tkMessageBox.showinfo("Never Miss Class", "Changes have been saved. The program is now running in the background.")
                        
                        
                #Getting the default pictures
                nl_mon_pic = PhotoImage(file="Images\Layer 5.gif")
                nl_tues_pic = PhotoImage(file="Images\Layer 4.gif")
                nl_wed_pic = PhotoImage(file="Images\Layer 3.gif")
                nl_thurs_pic = PhotoImage(file="Images\Layer 2.gif")
                nl_fri_pic = PhotoImage(file="Images\Layer 1.gif")
                nl_bmon_pic = PhotoImage(file="Images\Layer 10.gif")
                nl_btues_pic = PhotoImage(file="Images\Layer 9.gif")
                nl_bwed_pic = PhotoImage(file="Images\Layer 8.gif")
                nl_bthurs_pic = PhotoImage(file="Images\Layer 7.gif")
                nl_bfri_pic = PhotoImage(file="Images\Layer 6.gif") 
                #Lightning Pics
                l_mon_pic = PhotoImage(file="Images\L_M.gif")    
                l_tues_pic = PhotoImage(file="Images\L_T.gif")
                l_wed_pic = PhotoImage(file="Images\L_W.gif")
                l_thurs_pic = PhotoImage(file="Images\L_Th.gif")
                l_fri_pic = PhotoImage(file="Images\L_F.gif")
                l_btues_pic = PhotoImage(file="Images\L_BT.gif")    
                l_bthurs_pic = PhotoImage(file="Images\L_BTh.gif")
                    
                
                #creating a label for each image        
                label_monday = Label(root, image= nl_mon_pic, borderwidth = 0, highlightthickness= 0)
                label_monday.grid(row=0)
                #changing what the label does when it is hovered over or clicked.
                label_monday.bind("<Enter>", lambda event: monday_L(event, l_mon_pic))
                label_monday.bind("<Leave>", lambda event: monday_L(event, nl_mon_pic))
                label_monday.bind("<Button-1>", lift_monday)
                
                label_bmon = Label(root, image = nl_bmon_pic, borderwidth = 0, highlightthickness= 0)
                label_bmon.image = nl_bmon_pic
                label_bmon.grid(row=1,column=0)                
                #schedule.every().monday.at("11:16").do(webbrowser.open("www.virtuallearning.ca"))
                        
                label_tuesday = Label(root, image= nl_tues_pic, borderwidth = 0, highlightthickness= 0)
                label_tuesday.grid(row=0, column= 1)
                label_tuesday.bind("<Enter>", lambda event: tuesday_L(event, l_tues_pic))
                label_tuesday.bind("<Leave>", lambda event: tuesday_L(event, nl_tues_pic))
                label_tuesday.bind("<Button-1>", lift_tuesday)
                
                label_btues = Label(root, image= nl_btues_pic, borderwidth = 0, highlightthickness= 0)
                label_btues.grid(row=1, column= 1)
                label_btues.bind("<Enter>", lambda event: btuesday_L(event, l_btues_pic))
                label_btues.bind("<Leave>", lambda event: btuesday_L(event, nl_btues_pic))
                label_btues.bind("<Button-1>", test_function)
                #
                #                                    ^^^^
                #Najib, this is where you put your running loop
                #
                #
                        
                label_wednesday = Label(root, image= nl_wed_pic, borderwidth = 0, highlightthickness= 0)
                label_wednesday.grid(row=0, column= 2)
                label_wednesday.bind("<Enter>", lambda event: wednesday_L(event, l_wed_pic))
                label_wednesday.bind("<Leave>", lambda event: wednesday_L(event, nl_wed_pic))
                label_wednesday.bind("<Button-1>", lift_wednesday)
                
                label_bwed = Label(root, image = nl_bwed_pic, borderwidth = 0, highlightthickness= 0)
                label_bwed.image = nl_bwed_pic
                label_bwed.grid(row=1,column=2)                
                        
                label_thursday = Label(root, image= nl_thurs_pic, borderwidth = 0, highlightthickness= 0)
                label_thursday.grid(row=0, column= 3)
                label_thursday.bind("<Enter>", lambda event: thursday_L(event, l_thurs_pic))
                label_thursday.bind("<Leave>", lambda event: thursday_L(event, nl_thurs_pic))
                label_thursday.bind("<Button-1>", lift_thursday)
                
                label_bthur = Label(root, image= nl_bthurs_pic, borderwidth = 0, highlightthickness= 0)
                label_bthur.grid(row=1, column= 3)
                label_bthur.bind("<Enter>", lambda event: bthursday_L(event, l_bthurs_pic))
                label_bthur.bind("<Leave>", lambda event: bthursday_L(event, nl_bthurs_pic))
                label_bthur.bind("<Button-1>", lift_help)                
                        
                label_friday = Label(root, image= nl_fri_pic, borderwidth = 0, highlightthickness= 0)
                label_friday.grid(row=0, column= 4)
                label_friday.bind("<Enter>", lambda event: friday_L(event, l_fri_pic))
                label_friday.bind("<Leave>", lambda event: friday_L(event, nl_fri_pic))
                label_friday.bind("<Button-1>", lift_friday)
                
                label_bfri = Label(root, image = nl_bfri_pic, borderwidth = 0, highlightthickness= 0)
                label_bfri.image = nl_bfri_pic
                label_bfri.grid(row=1,column=4)                
                
                
                
                
                


                        

#All the days will be created as objects here. I will implement that after I finish formatting the grid layout properly        
class Days_UI:
        
                
        def __init__(self, root,bg_image,name):
                #webbrowser.open("www.virtuallearning.ca")  
                self.name = name
                centre_screen(root)
                root.title("Never Miss A Class")
                root.maxsize(width=1000,height=700)
                root.minsize(width=1000,height=700)
                
                #setting a font
                self.customFont = tkFont.Font(family="Minecraft", size=14)
                self.customFont_small = tkFont.Font(family="Minecraft", size=10)
                
                
                self.main_canvas = Canvas(root,width=1000,height=700, highlightthickness=0)
                self.main_canvas.grid(row=0, column=0)
                
                self.main_canvas.create_image(0,0,anchor=NW, image=bg_image)
                self.main_canvas.image=bg_image              
                     
                        
                time_tuple = ("6:00 AM","6:15 AM","6:30 AM","6:45 AM","7:00 AM","7:15 AM","7:30 AM","7:45 AM","8:00 AM","8:15 AM","8:30 AM","8:45 AM","9:00 AM","9:15 AM","9:30 AM","9:40 AM","10:00 AM","10:15 AM","10:30 AM","10:45 AM","11:00 AM","11:15 AM","11:30 AM","11:45 AM","12:00 AM","12:15 AM","12:30 AM","12:45 AM","1:00 PM","1:15 PM","1:30 PM","1:45 PM","2:00 PM","2:15 PM","2:30 PM","2:45 PM","3:00 PM","3:15 PM","3:30 PM","3:45 PM","4:00 PM","4:15 PM","4:30 PM","4:45 PM","5:00 PM","5:15 PM","5:30 PM","5:45 PM","6:00 PM","6:15 PM","6:30 PM","6:45 PM","7:00 PM","7:15 PM","7:30 PM","7:45 PM","8:00 PM","8:15 PM","8:30 PM","8:45 PM","9:00 PM")
                
                #Placing the buttons.
                self.class_name_button = Button(self.main_canvas, text="Change Class Name ",command= self.change_names,font=self.customFont_small)
                self.class_name_button.place(x=250,y=550)                                 
                self.default_button = Button(self.main_canvas, text="Reset to Defaults",command= self.set_values,font=self.customFont_small)
                self.default_button.place(x=400,y=550)
                self.save_button = Button(self.main_canvas, text="Save Changes",command= self.save_values,font=self.customFont_small)
                self.save_button.place(x=530,y=550)
                self.home_button = Button(self.main_canvas, text="Back to Home Screen",command= root.destroy,font=self.customFont_small)
                self.home_button.place(x=640,y=550)                
                
                
                #Initializing spinners
                
                self.spinner1 = Spinbox(self.main_canvas, values=time_tuple ,width=7)
                self.spinner1.place(x=340,y=200)                  
                self.spinner2 = Spinbox(self.main_canvas, values=time_tuple,width=7)
                self.spinner2.place(x=340,y=250) 
                self.spinner3 = Spinbox(self.main_canvas, values=time_tuple,width=7)
                self.spinner3.place(x=340,y=300)   
                self.spinner4 = Spinbox(self.main_canvas, values=time_tuple,width=7)
                self.spinner4.place(x=340,y=350) 
                self.spinner5 = Spinbox(self.main_canvas, values=time_tuple,width=7)
                self.spinner5.place(x=340,y=400)   
                self.spinner6 = Spinbox(self.main_canvas, values=time_tuple,width=7)
                self.spinner6.place(x=340,y=450)                 
                
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
                
                self.set_values()
                
                #Creting the text
                self.main_canvas.create_text(150,150, text = "Enter the time, name and URL of each class. Then click 'Save Changes'. ",anchor=NW,font=self.customFont)
                self.display_names()
                 
                                               
        def display_names(self):
                if self.name_list[0] != "":
                        self.p_name1 = self.main_canvas.create_text(250,200, text = self.name_list[0],anchor=NW,font=self.customFont) 
                else:
                        self.p_name1 = self.main_canvas.create_text(250,200, text = "Class 1",anchor=NW,font=self.customFont) 
                if self.name_list[1] != "":
                        self.p_name2 = self.main_canvas.create_text(250,250, text = self.name_list[1],anchor=NW,font=self.customFont)
                else:
                        self.p_name2 = self.main_canvas.create_text(250,250, text = "Class 2",anchor=NW,font=self.customFont)
                if self.name_list[2] != "":
                        self.p_name3 = self.main_canvas.create_text(250,300, text = self.name_list[2],anchor=NW,font=self.customFont) 
                else:
                        self.p_name3 = self.main_canvas.create_text(250,300, text = "Class 3",anchor=NW,font=self.customFont) 
                if self.name_list[3] != "":
                        self.p_name4 = self.main_canvas.create_text(250,350, text = self.name_list[3],anchor=NW,font=self.customFont)
                else:
                        self.p_name4 = self.main_canvas.create_text(250,350, text = "Class 4",anchor=NW,font=self.customFont)
                if self.name_list[4] != "":
                        self.p_name5 = self.main_canvas.create_text(250,400, text = self.name_list[4],anchor=NW,font=self.customFont) 
                else:
                        self.p_name5 = self.main_canvas.create_text(250,400, text = "Class 5",anchor=NW,font=self.customFont) 
                if self.name_list[5] != "":
                        self.p_name6 = self.main_canvas.create_text(250,450, text = self.name_list[5],anchor=NW,font=self.customFont)
                else:
                        self.p_name6 = self.main_canvas.create_text(250,450, text = "Class 6",anchor=NW,font=self.customFont)                
                               
        
        def change_names(self):                
                self.entry7 = Entry(self.main_canvas,width = 12)
                self.entry7.place(x=250,y=200)
                self.entry8 = Entry(self.main_canvas,width = 12)
                self.entry8.place(x=250,y=250)
                self.entry9 = Entry(self.main_canvas,width = 12)
                self.entry9.place(x=250,y=300)
                self.entry10 = Entry(self.main_canvas,width = 12)                
                self.entry10.place(x=250,y=350)
                self.entry11 = Entry(self.main_canvas,width = 12)
                self.entry11.place(x=250,y=400)
                self.entry12 = Entry(self.main_canvas,width = 12)                
                self.entry12.place(x=250,y=450)  
                
                self.class_name_button = Button(self.main_canvas, text="Save Name Changes",command= self.save_names,font=self.customFont_small)
                self.class_name_button.place(x=250,y=550) 
                
        #writes the values of all text fields and spinners to a file
        def save_values(self):
                self.get_spinner()
                self.get_text()
                li = [[self.in_textbox1, self.in_textbox2, self.in_textbox3, self.in_textbox4, self.in_textbox5, self.in_textbox6], [self.in_spin1, self.in_spin2, self.in_spin3, self.in_spin4, self.in_spin5, self.in_spin6],[self.name_list[0],self.name_list[1],self.name_list[2],self.name_list[3],self.name_list[4],self.name_list[5]]]              
              
                f = open(str(self.name + ".txt"), "w")
                for row in li:
                        for item in row:
                                f.write(str(item) + "|") # is str(item) necessary?
                        f.write("\n")
                f.close()
                     
                #self.in_textbox5 = li[0][4]
                #self.in_textbox6 = li[0][5]
                #self.in_spin5 = li[1][4]
                #self.in_spin6 = li[1][5]
                
        def save_names(self):
                self.get_names()
                self.save_values()
                
                self.entry7.destroy()
                self.entry8.destroy()
                self.entry9.destroy()
                self.entry10.destroy()
                self.entry11.destroy()
                self.entry12.destroy()
                self.class_name_button.destroy()
                
                self.main_canvas.delete(self.p_name1)
                self.main_canvas.delete(self.p_name2)
                self.main_canvas.delete(self.p_name3)
                self.main_canvas.delete(self.p_name4)
                self.main_canvas.delete(self.p_name5)
                self.main_canvas.delete(self.p_name6) 
                self.display_names()
                
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
                
        def get_names(self):
                self.name1 = self.entry7.get()
                self.name2 = self.entry8.get()
                self.name3 = self.entry9.get()
                self.name4 = self.entry10.get()
                self.name5 = self.entry11.get()
                self.name6 = self.entry12.get()
                if self.name1 != "":
                        self.name_list[0] = self.name1
                if self.name2 != "":
                        self.name_list[1] = self.name2
                if self.name3 != "":
                        self.name_list[2] = self.name3
                if self.name4 != "":
                        self.name_list[3] = self.name4
                if self.name5 != "":
                        self.name_list[4] = self.name5
                if self.name6 != "":
                        self.name_list[5] = self.name6               
                        
        def set_values(self):
                #Reading the values from the text file
                f = open(str(self.name + ".txt"), "r")
                li = []
                for line in f:
                        li.append(line.strip("\n").split("|"))
                f.close()
                #remove the empty string at the last index of both rows caused by the last item's pipe
                for row in li:
                        row.remove(row[-1])
                        
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
                
                self.name1 = li[2][0]
                self.name2 = li[2][1]
                self.name3 = li[2][2]
                self.name4 = li[2][3]   
                self.name5 = li[2][4]
                self.name6 = li[2][5]
                
                self.name_list = []
                self.name_list.append(self.name1)
                self.name_list.append(self.name2)
                self.name_list.append(self.name3)
                self.name_list.append(self.name4)
                self.name_list.append(self.name5)
                self.name_list.append(self.name6)
                
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
                self.entry6.delete(0,END)
                self.entry6.insert(0,self.in_textbox6) 
                
                
        
# takes a day object and returns the url of the class that needs to be launched next
def pending_class(x):
        li = [[],[]]
        t = time_to_int(current_time())
        # check for attributes, add them to a list
        # if there is a url attribute, add the corresponding time attribute
        if hasattr(in_textbox1, x):
                li[0].append(time_convert(x.in_spin1))
                li[1].append(x.in_textbox1)
        if hasattr(in_textbox2, x):
                li[0].append(time_convert(x.in_spin2))
                li[1].append(x.in_textbox2)                
        if hasattr(in_textbox3, x):
                li[0].append(time_convert(x.in_spin3))
                li[1].append(x.in_textbox3)                
        if hasattr(in_textbox4, x):
                li[0].append(time_convert(x.in_spin4))
                li[1].append(x.in_textbox4)                
        if hasattr(in_textbox5, x):
                li[0].append(time_convert(x.in_spin5))
                li[1].append(x.in_textbox5)                
        if hasattr(in_textbox6, x):
                li[0].append(time_convert(x.in_spin6))
                li[1].append(x.in_textbox6)      
        return class_url

# takes a day object and returns the time of the class that needs to be launched next                                
def pending_time():
        return class_time

# returns the current time in 24 hr format
def current_time():
        now = datetime.datetime.now()
        time = "%02d:%02d" % (now.hour, now.minute)
        return time

# converts time from 12 hr format to 24 hr format
def time_convert(x):
        time = "0:00" # default value
        if "AM" in x:
                time = x.strip(" AM")
        if "PM" in x:
                time = str(int(x.strip(" PM")) + 12)
                #if the time is midnight, then return 0:00 instead of 24:00
                if time == "24:00":
                        return "0:00"
        return time

# converts time from 24 hr format to an int representing minutes past midnight
def time_to_int(x):
        time = 0 # default value
        if re.match("^[0-9]{1,2}:[0-9]{2}$", x):
                if len(x) < 5:
                        x = "0" + x
                time = (int(x[0:2]) * 60) + int(x[3:5])                 
        return time 

root_main = Tk()


s = Start_UI(root_main)
#m.get_spinner() commented this out for now because it breaks read_values()
root_main.mainloop()
