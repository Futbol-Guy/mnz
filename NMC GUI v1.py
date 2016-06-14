#--------------------------------
#
# NMC GUI v1.2
#
# 
#
# Authors: Muhammad Abdulhafiz, Najib Abukar and Zachary van Noppen
#
# Purpose: To create a program that allows a user to schedule a class and have that class open automatically.
#
# 
#
#--------------------------------------------

from Tkinter import *
from ScrolledText import ScrolledText
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
import thread

#creating a function to centre the window on the screen
def centre_screen(root,w,h):
        # get screen width and height
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight() 
        
        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w)
        y = (hs/2) - (h+30)
        
        #placing the window on the screen
        root.geometry('%dx%d+%d+%d' % (1000, 700, x, y)) 

#creating a window to display that the function is running
class Run_UI:
        def __init__(self,root):
                #creating the title and window dimensions
                root.iconbitmap('Images\img.ico')
                root.title("Never Miss Class")
                root.maxsize(width=450,height=300)
                root.minsize(width=450,height=300) 
                centre_screen(root,225,150)
                #creating a canvas to place widgets on
                self.main_canvas = Canvas(root,width = 450, height =300,highlightthickness=0)
                self.main_canvas.pack()                        
                self.text_field = ScrolledText(self.main_canvas,width=52,height=18)
                #You have to set the state to normal to make changes to it. Disabling it makes it uneditable
                self.text_field.configure(state='normal')
                #deleting anything previously in the text field
                self.text_field.delete(1.0,END)
                #putting stuff in the text field. Works just like appending onto a list. 
                self.text_field.insert(END, "The program is now running in the background. \n")

                #open the current day's database file
                today = datetime.datetime.now().weekday() 
                weekdays = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday"}
                f = open(weekdays[today]+".txt", "r")
                classes = []
                for line in f:
                        classes.append(line.strip("\n").split("|"))                       
                f.close()                        
                
                # sort the 2d list by class times, and sort the class names and URLs
                # in the same way so the times and names stay together
                insert_sort(classes[1], classes[0], classes[2])
                
                # set up default names for any classes the user has not named
                for i in range(len(classes[2])):
                        if classes[2][i] == "":
                                classes[2][i] = "Class " + str(i)                
                
                # print out the sorted schedule
                self.text_field.insert(END, "Here is "+weekdays[today]+"'s schedule: \n")
                self.text_field.insert(END, ("{0:25}{1:>10}").format("Class Name", "Class Time \n"))
                self.text_field.insert(END, "-" * 35 + "\n")

                # iterate through the list of URLs
                for i in range(len(classes[0])):
                        # for every non-empty url, print the associated name and date of the class
                        if classes[0][i] != "":
                                self.text_field.insert(END, ("{0:25}{1:>10}").format(classes[2][i], classes[1][i] + "\n"))
                
                # disable the text field after writing to it
                self.text_field.configure(state='disabled')                 
                self.text_field.place(x=5,y=5)
                
                
        
#creating the second help window       
class Help_two_UI:
        def __init__(self,root,bg_image):
                
                #opening the URL to the help video
                def onObjectClick(event):
                        webbrowser.open_new(r"http://nmacvlc.blogspot.ca/") 
                
                #opening the first help window        
                def lift_last():
                        root.destroy()
                        main = Toplevel(root_main)
                        Help_one_UI(main,bg_image)                        
                #setting a custom font
                self.customFont_small = tkFont.Font(family="Minecraft", size=10)
                 
                 #setting the title, and dimensions of the window
                root.iconbitmap('Images\img.ico')
                root.title("Never Miss A Class")
                root.maxsize(width=1000,height=700)
                root.minsize(width=1000,height=700)                
                centre_screen(root,500,350)
                #placing a canvas on the window to hold the baground image and text.
                self.main_canvas = Canvas(root,width=1000,height=700, highlightthickness=0)
                self.main_canvas.grid(row=0, column=0)
                #positioning the background image                
                self.main_canvas.create_image(0,0,anchor=NW, image=bg_image)
                self.main_canvas.image=bg_image 
                
                help_1 = PhotoImage(file="Images\Help 7.gif")
                #creating the text
                self.main_canvas.create_text(20,90, text = "Finally, save your changes by clicking the button. Then click the 'Run' button on the home page.",anchor=NW,font=self.customFont_small)
                self.main_canvas.create_text(20,110, text = "If you would like to lauch the Connect window instead of the class in a new tab (eg. when the class is launched in firefox), launch the class in firefox and copy ",anchor=NW,font=self.customFont_small)
                self.main_canvas.create_text(20,130, text = "the link found in the pop up window (not in the actual connect room).",anchor=NW,font=self.customFont_small)
                self.main_canvas.create_text(430,150, text = "For more useful information and help, take a look at our website", anchor=NW,font=self.customFont_small)
                self.main_canvas.create_text(430,170, text = "and read the readMe file located in where this program is installed.",anchor=NW,font=self.customFont_small)               
                                
                #creating the click-able link
                self.obj1Id = self.main_canvas.create_text(430,150,activefill="#33adff",text='For more useful information and help, take a look at our website', fill="#0099ff",tags='obj1Tag',anchor=NW,font=self.customFont_small)
                self.main_canvas.tag_bind(self.obj1Id, '<ButtonPress-1>', onObjectClick) 
                
                #creating buttons to navigate the UI
                self.main_B = Button(self.main_canvas, text = "Previous Page",command= lift_last,font=self.customFont_small)
                self.main_B.place(x=20,y=660)
                self.next_B = Button(self.main_canvas, text = "Back to Home Page",command= root.destroy,font=self.customFont_small)
                self.next_B.place(x=840,y=660)  
                
                #creating a canvas to place other images
                self.h1_canvas = Canvas(self.main_canvas,width=400,height=246, highlightthickness=0)
                self.h1_canvas.place(x=20,y=150)
                self.h1_canvas.create_image(0,0,image=help_1,anchor=NW)
                self.h1_canvas.image = help_1                
                                

class Help_one_UI:
        def __init__(self,root,bg_image):
                #opening the second help window
                def lift_next():
                        root.destroy()
                        main = Toplevel(root_main)
                        Help_two_UI(main,bg_image)                  
                #setting a custom font
                self.customFont_small = tkFont.Font(family="Minecraft", size=10)
                #creating the title and dimensions of the window 
                root.iconbitmap('Images\img.ico')                  
                root.title("Never Miss A Class")
                root.maxsize(width=1000,height=700)
                root.minsize(width=1000,height=700)                
                centre_screen(root,500,350)
                
                help_1 = PhotoImage(file="Images\Help 1.gif")
                help_2 = PhotoImage(file="Images\Help 2.gif")
                help_3 = PhotoImage(file="Images\Help 3.gif")
                help_4 = PhotoImage(file="Images\Help 4.gif")   
                help_5 = PhotoImage(file="Images\Help 5.gif") 
                
                #creating a canvas to place the bg image and text on
                self.main_canvas = Canvas(root,width=1000,height=700, highlightthickness=0)
                self.main_canvas.grid(row=0, column=0)
                #creating the image
                self.main_canvas.create_image(0,0,anchor=NW, image=bg_image)
                self.main_canvas.image=bg_image  
                
                #creating the text seen on the page
                self.main_canvas.create_text(20,90, text = "Welcome to Never Miss a Class! To get started, click what day you have",anchor=NW,font=self.customFont_small)
                self.main_canvas.create_text(270,110, text = " a class on.",anchor=NW,font=self.customFont_small) 
                self.main_canvas.create_text(20,470, text = "Next, select the time your class starts.",anchor=NW,font=self.customFont_small)
                self.main_canvas.create_text(780,90, text = "Next, get the class URL. ",anchor=NW,font=self.customFont_small)
                self.main_canvas.create_text(520,260, text = "Copy the link pictured below and paste it into the appropriate text box. ",anchor=NW,font=self.customFont_small)
                
                #creating canvases to place images
                self.h1_canvas = Canvas(self.main_canvas,width=250,height=336, highlightthickness=0)
                self.h1_canvas.place(x=20,y=110)
                self.h1_canvas.create_image(0,0,image=help_1,anchor=NW)
                self.h1_canvas.image = help_1
                self.h2_canvas = Canvas(self.main_canvas,width=478,height=160, highlightthickness=0)
                self.h2_canvas.place(x=20,y=490)
                self.h2_canvas.create_image(0,0,image=help_2,anchor=NW)
                self.h2_canvas.image = help_2
                self.h3_canvas = Canvas(self.main_canvas,width=250,height=153, highlightthickness=0)
                self.h3_canvas.place(x=520,y=90)
                self.h3_canvas.create_image(0,0,image=help_3,anchor=NW)
                self.h3_canvas.image = help_3
                self.h4_canvas = Canvas(self.main_canvas,width=350,height=174, highlightthickness=0)
                self.h4_canvas.place(x=520,y=280)
                self.h4_canvas.create_image(0,0,image=help_4,anchor=NW)
                self.h4_canvas.image = help_4
                self.h5_canvas = Canvas(self.main_canvas,width=408,height=157, highlightthickness=0)
                self.h5_canvas.place(x=520,y=490)
                self.h5_canvas.create_image(0,0,image=help_5,anchor=NW)
                self.h5_canvas.image = help_5                
                
                #creating buttons to navigate the UI
                self.main_B = Button(self.main_canvas, text = "Back to Home Screen",command= root.destroy,font=self.customFont_small)
                self.main_B.place(x=20,y=660)
                self.next_B = Button(self.main_canvas, text = "Next Page",command= lift_next,font=self.customFont_small)
                self.next_B.place(x=900,y=660)                                                                
                      
                
#creating the starting user interface
class Start_UI:         
        def __init__(self, root):
                #setting the title and window dimensions
                root.iconbitmap('Images\img.ico')
                root.title("Never Miss A Class")
                root.maxsize(width=1000,height=700)
                root.minsize(width=1000,height=700)
                centre_screen(root,500,350)
                
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
                        
                def bwednesday_L(event,pic):
                        label_bwed.config(image=pic)                
                
                def bthursday_L(event,pic):
                        label_bthur.config(image=pic)
                
                #creating functions to open each day's window
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
                        help = Help_one_UI(main,image)  
                
                def close_window(event): 
                        if tkMessageBox.askyesno("NMC","Quitting will stop the effects of the program. Your classes will not be launched automatically. Would you still like to quit?"):
                                root_main.destroy()
                                        
                def main_function(event):
                        main = Toplevel(root_main)                       
                        Run_UI(main)
                        weekdays = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday"}
                        today = datetime.datetime.now().weekday()

                        f = open(weekdays[today]+".txt", "r")
                        classes = []
                        for line in f:
                                classes.append(line.strip("\n").split("|"))
                        f.close()
                        
                        for i in range(len(classes[0])):
                                # add every class entered for the current day to the job queue
                                # along with its scheduled time in 24 hr format
                                if classes[0][i] != "":
                                        class_url = classes[0][i]
                                        class_time = time_convert(classes[1][i])
                                        schedule.every().day.at(time_convert(classes[1][i])).do(webbrowser.open, classes[0][i])               
                       
                        # a function for checking for pending classes
                        def pending_classes():
                                while True:
                                        schedule.run_pending()
                                        # check every 5 seconds
                                        time.sleep(5)
                        
                        # create a new thread and let pending_classes() run indefinitely
                        try:
                                thread.start_new_thread(pending_classes, ())
                        except:
                                # open a file for dumping debug text in case of an exception
                                new_file = open("debug.txt","w")
                                new_file.write("An error has occurred in the scheduling function.")
                                new_file.close()                      
                                
                        
                                     
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
                l_mon_pic = PhotoImage(file="Images\L_M.gif")    
                l_tues_pic = PhotoImage(file="Images\L_T.gif")
                l_wed_pic = PhotoImage(file="Images\L_W.gif")
                l_thurs_pic = PhotoImage(file="Images\L_Th.gif")
                l_fri_pic = PhotoImage(file="Images\L_F.gif")
                l_btues_pic = PhotoImage(file="Images\L_BT.gif") 
                l_bwed_pic = PhotoImage(file="Images\L_BW.gif")
                l_bthurs_pic = PhotoImage(file="Images\L_BTh.gif")
                
                #creating a label for each image and placing images in those labels       
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
                label_btues.bind("<Button-1>", main_function)
                
                        
                label_wednesday = Label(root, image= nl_wed_pic, borderwidth = 0, highlightthickness= 0)
                label_wednesday.grid(row=0, column= 2)
                label_wednesday.bind("<Enter>", lambda event: wednesday_L(event, l_wed_pic))
                label_wednesday.bind("<Leave>", lambda event: wednesday_L(event, nl_wed_pic))
                label_wednesday.bind("<Button-1>", lift_wednesday)
                
                label_bwed = Label(root, image = nl_bwed_pic, borderwidth = 0, highlightthickness= 0)
                label_bwed.grid(row=1,column=2)
                label_bwed.bind("<Enter>", lambda event: bwednesday_L(event, l_bwed_pic))
                label_bwed.bind("<Leave>", lambda event: bwednesday_L(event, nl_bwed_pic))
                label_bwed.bind("<Button-1>", lift_help)                
                        
                label_thursday = Label(root, image= nl_thurs_pic, borderwidth = 0, highlightthickness= 0)
                label_thursday.grid(row=0, column= 3)
                label_thursday.bind("<Enter>", lambda event: thursday_L(event, l_thurs_pic))
                label_thursday.bind("<Leave>", lambda event: thursday_L(event, nl_thurs_pic))
                label_thursday.bind("<Button-1>", lift_thursday)
                
                label_bthur = Label(root, image= nl_bthurs_pic, borderwidth = 0, highlightthickness= 0)
                label_bthur.grid(row=1, column= 3)
                label_bthur.bind("<Enter>", lambda event: bthursday_L(event, l_bthurs_pic))
                label_bthur.bind("<Leave>", lambda event: bthursday_L(event, nl_bthurs_pic))
                label_bthur.bind("<Button-1>", close_window)                
                        
                label_friday = Label(root, image= nl_fri_pic, borderwidth = 0, highlightthickness= 0)
                label_friday.grid(row=0, column= 4)
                label_friday.bind("<Enter>", lambda event: friday_L(event, l_fri_pic))
                label_friday.bind("<Leave>", lambda event: friday_L(event, nl_fri_pic))
                label_friday.bind("<Button-1>", lift_friday)
                
                label_bfri = Label(root, image = nl_bfri_pic, borderwidth = 0, highlightthickness= 0)
                label_bfri.image = nl_bfri_pic
                label_bfri.grid(row=1,column=4)                
    
                                       
#creating a class to run all of the days        
class Days_UI:         
        def __init__(self, root,bg_image,name):
                self.name = name
                centre_screen(root,500,350)
                root.iconbitmap('Images\img.ico')
                root.title("Never Miss A Class")
                root.maxsize(width=1000,height=700)
                root.minsize(width=1000,height=700)
                
                #setting custom fonts
                self.customFont = tkFont.Font(family="Minecraft", size=14)
                self.customFont_small = tkFont.Font(family="Minecraft", size=10)
                
                #creating a canvas to place text and entry boxes
                self.main_canvas = Canvas(root,width=1000,height=700, highlightthickness=0)
                self.main_canvas.grid(row=0, column=0)
                #placing the background image
                self.main_canvas.create_image(0,0,anchor=NW, image=bg_image)
                self.main_canvas.image=bg_image              
                     
                #creating a tuple of times to put in the spinner        
                time_tuple = ("6:00 AM","6:15 AM","6:30 AM","6:45 AM","7:00 AM","7:15 AM","7:30 AM","7:45 AM","8:00 AM","8:15 AM","8:30 AM","8:45 AM","9:00 AM","9:15 AM","9:30 AM","9:40 AM","10:00 AM","10:15 AM","10:30 AM","10:45 AM","11:00 AM","11:15 AM","11:30 AM","11:45 AM","12:00 PM","12:15 PM","12:30 PM","12:45 PM","1:00 PM","1:15 PM","1:30 PM","1:45 PM","2:00 PM","2:15 PM","2:30 PM","2:45 PM","3:00 PM","3:15 PM","3:30 PM","3:45 PM","4:00 PM","4:15 PM","4:30 PM","4:45 PM","5:00 PM","5:15 PM","5:30 PM","5:45 PM","6:00 PM","6:15 PM","6:30 PM","6:45 PM","7:00 PM","7:15 PM","7:30 PM","7:45 PM","8:00 PM","8:15 PM","8:30 PM","8:45 PM","9:00 PM")
                
                #placing the buttons
                self.class_name_button = Button(self.main_canvas, text="Change Class Name ",command= self.change_names,font=self.customFont_small)
                self.class_name_button.place(x=250,y=550)                                 
                self.default_button = Button(self.main_canvas, text="Save Changes",command= self.save_values,font=self.customFont_small)
                self.default_button.place(x=400,y=550)
                self.save_button = Button(self.main_canvas, text="Back to Home Screen",command= root.destroy,font=self.customFont_small)
                self.save_button.place(x=510,y=550)              
                
                #initializing spinners 
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
                
                #initializing text boxes
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
                #setting each classes properties based on what the user has previously inputted
                self.set_values()
                self.display_names()
                
                #creting the text
                self.main_canvas.create_text(150,150, text = "Enter the time, name and URL of each class. Then click 'Save Changes'. ",anchor=NW,font=self.customFont)
                
        #creating a function that sets the names of each function                                                 
        def display_names(self):
                #checking to see if the user has previously made a name for each class
                #if not, a default name is set
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
                               
        #creating a function that allows the user to change the name of each class 
        def change_names(self): 
                self.main_canvas.delete(self.p_name1)
                self.main_canvas.delete(self.p_name2)
                self.main_canvas.delete(self.p_name3)
                self.main_canvas.delete(self.p_name4)
                self.main_canvas.delete(self.p_name5)
                self.main_canvas.delete(self.p_name6)                
                #placing entry boses over the text
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
                
                #creating a button to save the changes made
                self.class_name_button = Button(self.main_canvas, text="Save Name Changes",command= self.save_names,font=self.customFont_small)
                self.class_name_button.place(x=250,y=550) 
                
        #writes the values of all text fields and spinners to a file
        def save_values(self):
                #getting the URL, and time
                self.get_spinner()
                self.get_text()
                #placing the names, URL and time in a matrix
                li = [[self.in_textbox1, self.in_textbox2, self.in_textbox3, self.in_textbox4, self.in_textbox5, self.in_textbox6], [self.in_spin1, self.in_spin2, self.in_spin3, self.in_spin4, self.in_spin5, self.in_spin6],[self.name_list[0],self.name_list[1],self.name_list[2],self.name_list[3],self.name_list[4],self.name_list[5]]]              
              
                #writing the matrix to the file
                f = open(str(self.name + ".txt"), "w")
                for row in li:
                        for item in row:
                                f.write(str(item) + "|") 
                        f.write("\n")
                f.close()
                     
        
        #creating a function to save names        
        def save_names(self):
                self.get_names()
                self.save_values()
                
                #deleting the old names 
                self.entry7.destroy()
                self.entry8.destroy()
                self.entry9.destroy()
                self.entry10.destroy()
                self.entry11.destroy()
                self.entry12.destroy()
                self.class_name_button.destroy()
                #displaying the new names
                 
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
                
        #getting the values of each name         
        def get_names(self):
                self.name1 = self.entry7.get()
                self.name2 = self.entry8.get()
                self.name3 = self.entry9.get()
                self.name4 = self.entry10.get()
                self.name5 = self.entry11.get()
                self.name6 = self.entry12.get()
                #if there is no new name entered, just leave it as the default
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
        
        #setting the values  the URL and time                
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
                
                #gets the names of each class from the file
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

# converts time from 12 hr format to 24 hr format
def time_convert(x):
        time = "0:00" # default value
        if "AM" in x:
                split_time = x.strip(" AM").split(":")
                hours = str(int(split_time[0]))
                #use 0 to represent midnight (12:00 AM) instead of 12
                if str(int(hours) + 12) == "24":
                        hours = "0"
                # put the string back together again
                time = hours + ":" + split_time[1]                
        if "PM" in x:
                # split the time in half by the colon, ex. 9:30 becomes 9 and 30
                split_time = x.strip(" PM").split(":")
                # add 12 to the hours portion
                hours = str(int(split_time[0]) + 12)
                #use 12 to represent noon (12:00 PM) instead of 24
                if hours == "24":
                        hours = "12"
                # put the string back together again
                time = hours + ":" + split_time[1]
        return time

# converts time from 24 hr format to an int representing minutes past midnight
def time_to_int(x):
        time = 0 # default value
        if re.match("^[0-9]{1,2}:[0-9]{2}$", x):
                if len(x) < 5:
                        x = "0" + x
                time = (int(x[0:2]) * 60) + int(x[3:5])                 
        return time 

# this insertion sort algorithm was sourced from the "Sorting Algorithms" page in the investigations
# accepts a list of class times and a list of names and sorts by time 

def insert_sort(class_times, class_urls, class_names):     
        for i in range(len(class_times)-1):
                j = i + 1 # j will go from 1 to max_index
                item_time = class_times[j] # temporary storage of item
                item_urls = class_urls[j]
                item_names = class_names[j]
                # Run through the list backwards until item is less than element
                while (j > 0) and (time_to_int(time_convert(item_time)) < time_to_int(time_convert(class_times[j-1]))):
                        # Shift larger items to the right by one
                        class_times[j] = class_times[j-1]   
                        class_urls[j] = class_urls[j-1] 
                        class_names[j] = class_names[j-1] 
                        # Prepare to check the next item to the left
                        j -= 1
                        # put sorted item in open location
                        class_times[j] = item_time
                        class_urls[j] = item_urls
                        class_names[j] = item_names
        
        # return a sorted 2d list                
        return [class_times, class_urls, class_names]

#running the start page
root_main = Tk()
# Makes the close button minimze
root_main.protocol("WM_DELETE_WINDOW", root_main.iconify)
# Replaces tk icon with a custom made one
root_main.iconbitmap('Images\img.ico')


s = Start_UI(root_main)
root_main.mainloop()