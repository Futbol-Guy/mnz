#!/usr/bin/env python
import webbrowser
import schedule
import time
import sys
import subprocess



    


def action():
    class_link = raw_input("Link: ")
    while class_link == "done":
        break
    else:
        while True:
            def job():
                webbrowser.open(class_link) 
            time = raw_input("Time: ")  
            while True:    
                day = raw_input("Day: ")  
                if day == "monday":
                    schedule.every().monday.at(time).do(job)
                elif day == "tuesday":
                    schedule.every().tuesday.at(time).do(job)
                elif day == "wednesday":
                    schedule.every().wednesday.at(time).do(job)
                elif day == "thursday":
                    schedule.every().thursday.at(time).do(job)
                elif day == "friday":
                    schedule.every().friday.at(time).do(job) 
                elif day == "saturday":
                    schedule.every().saturday.at(time).do(job)
                elif day == "sunday":
                    schedule.every().sunday.at(time).do(job)
                else:
                    break          
            break


def again():
    an = raw_input("Another Class? ")
    while an == "no" or "quit":
        print "Thanks, your class will open during the time you have set it to!"
        break
    else:
        action()
        
        
action()
again()

while True:
    schedule.run_pending()
    
    
    
    