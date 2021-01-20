# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 12:15:46 2020

@author: rockg
"""

import statistics as st
import pickle
import sys

pickle_in = open('gradedict.pkl','rb')
gradedict = pickle.load(pickle_in)


def more(x,y):
    while True:
        if x =='Yes':
            return y
            break
        elif x == 'No':
            return 0
            break
        else:
            x = input("Sorry, I didn't catch that. Please answer 'Yes' or 'No': ")

def addStudent():
    print("Please provide the student's name and grade")
    name = input("Student Name: ")
    grade = input("Grade: ")
    print("Adding new grade to the database...")
    if name in gradedict:
        gradedict[name].append(int(grade))
        print(gradedict)
    else:
        newstudent = input('Student does not exist. Would you like to add the student? (Yes/No): ')
        if newstudent == 'Yes':
            gradedict[name] = []
            gradedict[name].append(int(grade))
            print(gradedict)
        elif newstudent == 'No':
            print('Ok, no grades were added')
        else:
            print("Sorry, I didn't understand your request")

def removeStudent():
    
    name = input("Who would you like to remove from the database? ")
    print("Removing student from the database...")
    if name in gradedict:
        del gradedict[name]
        print(gradedict)
    else:
        print("That student doesn't appear to be in the database")

def studentAVG():
    name = input("Who's average would you like to know? ")
    if name == 'All' or name == 'all':
        avglist = []
        for k,v in gradedict.items():
            avglist.append(st.mean(v))
        avg = st.mean(avglist)
        print("The class average over all the tests is",avg)            
    else:
        try:
            print("Calculating average... This won't take long")
            x = st.mean(gradedict[name])
            print(name,"got an average of",x,)
        except Exception:
            print("Sorry, I'm not able to calculate that average")
        
def main():
    try:
        print("""
    How may I assist you?"
    (1) Shall I add new grades for a student?"
    (2) Shall I remove a student from the database?"
    (3) Do you want a student's average grade?"
    (4) Would you like to change your password?"
    (5) Are my services not currently required?
              """)
        task = int(input("Please enter a number: "))
    except ValueError:
        print("Sorry, I don't know how to do that")
        task = 0
    
    while task == 1:
        addStudent()
        m = input("Do you want to add any more grades? (Yes/No): ")
        task = more(m,task)
                            
    while task == 2:
        removeStudent()
        m = input("Do you want to remove any other students? (Yes/No): ")
        task = more(m,task)
        
    while task == 3:
        studentAVG()
        m = input("Do you want any more averages? (Yes/No): ")
        task = more(m,task)
       
    while task == 4:
        password_2 = input("New password: ")
        password_3 = input("Retype new password: ")
        if password_2 == password_3:
            pickle_out = open('password.pkl','wb')
            pickle.dump(password_2,pickle_out)
            pickle_out.close()
            task = 0
        else:
            retry = input('Passwords do not match. Would you like to try again? (Yes/No): ')
                                
            while True:
                if retry == 'Yes':
                    break
                elif retry == 'No':
                    print("Ok, you're password was not changed")
                    task = 0
                    break
                else:
                    retry = input("Sorry, I didn't quite catch that. Do you still want to change your password? (Yes/No): ")
                            
    while task == 5:
        print("Thank you for using the grades database. Have a nice day")
        pickle_out = open('gradedict.pkl','wb')
        pickle.dump(gradedict,pickle_out)
        pickle_out.close()
        sys.exit()
    
    while task >= 6 or task < 0:
        print('Sorry, I don\'t know how to do that')
        task = 0
                
                
                


username = 'Admin'
pickle_in = open('password.pkl','rb')
password = pickle.load(pickle_in)

username_1 = input("Username: ")
password_1 = input("Password: ")

if username_1 == username and password_1 == password:
    print("Hello and welcome to the grade database")
    task = 0
    while True:
       main()
                
else:
    print("Does not compute... Please go away, you have confused me and made me sad")
    