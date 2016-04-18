from Tkinter import *
from PIL import ImageTk, Image

class Start_UI:
                                
                
        def __init__(self, root):
                
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
                        
                #GETTING PICTURES
                nl_mon_pic = PhotoImage(file="MS_NL_Mon.gif")
                nl_tues_pic = PhotoImage(file="MS_NL_Tues.gif")
                nl_wed_pic = PhotoImage(file="MS_NL_Wed.gif")
                nl_thurs_pic = PhotoImage(file="MS_NL_Thurs.gif")
                nl_fri_pic = PhotoImage(file="MS_NL_Fri.gif")
                #Lightning Pics
                l_mon_pic = PhotoImage(file="MS_L_Mon.gif")
                l_tues_pic = PhotoImage(file="MS_L_Tues.gif")
                l_wed_pic = PhotoImage(file="MS_L_Wed.gif")
                l_thurs_pic = PhotoImage(file="MS_L_Thurs.gif")
                l_fri_pic = PhotoImage(file="MS_L_Fri.gif")
                        
                label_monday = Label(root, image= nl_mon_pic, borderwidth = 0, highlightthickness= 0)
                label_monday.grid(row=0)
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
        
class Monday_UI:
        
        def __init__(self, root):
                frame = Frame(root, width=300,height=200)
                frame.grid(row=0)                




start_main = Tk()
monday_main = Tk()
s = Start_UI(start_main)
m = Monday_UI(monday_main)
start_main.mainloop()