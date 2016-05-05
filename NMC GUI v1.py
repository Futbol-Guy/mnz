#--------------------------------

# NMC GUI v1.2

# 

# NOTE: You will have to quit the program to see the values printed properly. Either that or press the button twice

#

#--------------------------------------------


from Tkinter import *
from PIL import ImageTk, Image

class Start_UI:
                                
                
        def __init__(self, root):
                
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
                        monday_main.lift()                
                        
                root.title("NMC Scheduler")
                        
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
                        
                label_tuesday = Label(root, image= nl_tues_pic, borderwidth = 0, highlightthickness= 0)
                label_tuesday.grid(row=0, column= 1)
                label_tuesday.bind("<Enter>", lambda event: tuesday_L(event, l_tues_pic))
                label_tuesday.bind("<Leave>", lambda event: tuesday_L(event, nl_tues_pic))
                label_tuesday.bind("<Button-1>", lift_monday)
                        
                label_wednesday = Label(root, image= nl_wed_pic, borderwidth = 0, highlightthickness= 0)
                label_wednesday.grid(row=0, column= 2)
                label_wednesday.bind("<Enter>", lambda event: wednesday_L(event, l_wed_pic))
                label_wednesday.bind("<Leave>", lambda event: wednesday_L(event, nl_wed_pic))
                label_wednesday.bind("<Button-1>", lift_monday)
                        
                label_thursday = Label(root, image= nl_thurs_pic, borderwidth = 0, highlightthickness= 0)
                label_thursday.grid(row=0, column= 3)
                label_thursday.bind("<Enter>", lambda event: thursday_L(event, l_thurs_pic))
                label_thursday.bind("<Leave>", lambda event: thursday_L(event, nl_thurs_pic))
                label_thursday.bind("<Button-1>", lift_monday)
                        
                label_friday = Label(root, image= nl_fri_pic, borderwidth = 0, highlightthickness= 0)
                label_friday.grid(row=0, column= 4)
                label_friday.bind("<Enter>", lambda event: friday_L(event, l_fri_pic))
                label_friday.bind("<Leave>", lambda event: friday_L(event, nl_fri_pic))
                label_friday.bind("<Button-1>", lift_monday)

#All the days will be created as objects here. I will implement that after I finish formatting the grid layout properly        
class Days_UI:
        
        
        def __init__(self, root):
                              
                
                #A ton of stuff that will not be here later 
                test2 = PhotoImage(file="3.gif")
        
                l = Label(root, image= test2 ,borderwidth = 0, highlightthickness= 0)
                l.image= test2
                l.grid(row=0)
                l2 = Label(root, image= test2,borderwidth = 0, highlightthickness= 0)
                l2.test= test2
                l2.grid(row=1)
                l3 = Label(root, image= test2,borderwidth = 0, highlightthickness= 0)
                l3.test= test2
                l3.grid(row=2)  
                l4 = Label(root, image= test2,borderwidth = 0, highlightthickness= 0)
                l4.test= test2
                l4.grid(row=3)                
                
                
                time_tuple = ("1 AM","2 AM","3 AM","4 AM","5 AM","6 AM","7 AM","9 AM","10 AM","11 AM","12 AM","1 PM","2 PM","3 PM","4 PM","5 PM","6 PM","7 PM","9 PM","10 PM","11 PM","12 PM")
                
                 
                #Initializing spinners
                root.geometry("1000x700")
                self.spinner1 = Spinbox(root, values=time_tuple ,width=5)
                self.spinner1.grid(row=0,column=2)                  
                self.spinner2 = Spinbox(root, values=time_tuple,width=5)
                self.spinner2.grid(row=1,column=2) 
                self.spinner3 = Spinbox(root, values=time_tuple,width=5)
                self.spinner3.grid(row=2,column=2)  
                self.spinner4 = Spinbox(root, values=time_tuple,width=5)
                self.spinner4.grid(row=3,column=2)                
                
                #Initializing text boxes
                self.entry1 = Entry(root)
                self.entry1.grid(row=0,column=4)
                self.entry2 = Entry(root)
                self.entry2.grid(row=1,column=4)
                self.entry3 = Entry(root)
                self.entry3.grid(row=2,column=4)
                self.entry4 = Entry(root)                
                self.entry4.grid(row=3,column=4)
                
                
                #Making buttons so you can test the inputs
                b = Button(root, text="Print Values",command= self.print_values)
                b.grid(row=0,column=5)
                b2 = Button(root, text="Set Defaults",command= self.set_values)
                b2.grid(row=0,column=6) 
                #buttons for testing file I/O
                b3 = Button(root, text="Save Values",command= self.save_values)
                b3.grid(row=0,column=7)
                b4 = Button(root, text="Read Values",command= self.read_values)
                b4.grid(row=0,column=8)                
        
        #writes the values of all text fields and spinners to a file
        def save_values(self):
                self.get_spinner()
                self.get_text()
                li = [[self.in_textbox1, self.in_textbox2, self.in_textbox3, self.in_textbox4], [self.in_spin1, self.in_spin2, self.in_spin3, self.in_spin4]]               
                f = open("Example.txt", "w") # Change this so the file is named based on the object
                for row in li:
                        for item in row:
                                f.write(str(item) + "|") # is str(item) necessary?
                        f.write("\n")
                f.close()
                     
        #reads the values of text values and spinners from a file
        def read_values(self):
                f = open("Example.txt", "r") # Change this so the file is named based on the object
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
                
                self.in_spin1 = li[1][0]
                self.in_spin2 = li[1][1]
                self.in_spin3 = li[1][2]
                self.in_spin4 = li[1][3]                        
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
        
        #getting the text entries      
        def get_text(self):
                self.in_textbox1 = self.entry1.get()
                self.in_textbox2 = self.entry2.get()
                self.in_textbox3 = self.entry3.get()
                self.in_textbox4 = self.entry4.get()
                        
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
                
root_main = Tk()
monday_main = Toplevel(root_main)

s = Start_UI(root_main)
m = Days_UI(monday_main)
#m.get_spinner() commented this out for now because it breaks read_values()
root_main.mainloop()