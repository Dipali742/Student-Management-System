# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pymongo import MongoClient
from random import randint
from Tkinter import *
import tkMessageBox
import ttk
from Tkinter import Button
import sys

try:
	client = MongoClient(port=27017)
	db=client.Assignment08
	print("Connected to MongoDB")
except :
	print("Database connection Error ")
	print("No connection could be made because the target machine actively refused it ")
	tkMessageBox.showerror("Error", "Connection Error")
	sys.exit(1)
	


root=Tk()
root.geometry('400x350')
root.title("STUDENT Management System")

def add_STUDENTS(root,db): 
    def add_query():
        global root
        prn = E1.get()
        name = E2.get()
        email = E3.get()
        batch = E4.get()
        mobile = E5.get()
        PRN = [prn]
        NAME = [name]
        EMAIL = [email]
        BATCH = [batch]
        MOBILE = [mobile]
        Assignment08 = {
        'PRN' : PRN[randint(0, (len(PRN)-1))] ,
        'NAME' : NAME[randint(0, (len(NAME)-1))],
        'EMAIL' : EMAIL[randint(0, (len(EMAIL)-1))],
        'BATCH' : BATCH[randint(0, (len(BATCH)-1))],
        'MOBILE' : MOBILE[randint(0, (len(MOBILE)-1))]}
        
        if(len(prn)==0):
            tkMessageBox.showwarning("WARNING", "All fields are compulsory(Except: Mobile number)")
            return
        if(len(name)==0):
            tkMessageBox.showwarning("WARNING", "All fields are compulsory(Except: Mobile number)")
            return
        if(len(email)==0):
            tkMessageBox.showwarning("WARNING", "All fields are compulsory(Except: Mobile number)")
            return
        if(len(batch)==0):
            tkMessageBox.showwarning("WARNING", "All fields are compulsory(Except: Mobile number)")
            return
        if len(mobile)==0 and db.students.count_documents({ 'PRN': prn }, limit = 1)==0:
             result=db.students.insert_one({'PRN':prn,'NAME':name, 'EMAIL':email,'BATCH':batch})
        elif len(mobile)!=0 and db.students.count_documents({ 'PRN': prn }, limit = 1)==0:
             result=db.students.insert_one(Assignment08)
        else:
             tkMessageBox.showwarning("ERROR", "STUDENT Already Exists")
             return
       	
        newwin.destroy()
        tkMessageBox.showinfo("Add Student", "Student Added")
    newwin = Toplevel(root)
    newwin.geometry('400x400')
    newwin.title("Add STUDENTS")
    L1 = Label(newwin, text="PRN")
    L1.place(x=10,y=50)
    E1 = Entry(newwin, bd=7)
    E1.place(x=100,y=50)
    L2 = Label(newwin, text="NAME")
    L2.place(x=10,y=100)
    E2 = Entry(newwin, bd=7)
    E2.place(x=100,y=100)
    L3 = Label(newwin, text="EMAIL")
    L3.place(x=10,y=150)
    E3 = Entry(newwin, bd=7)
    E3.place(x=100,y=150)
    L4 = Label(newwin, text="BATCH")
    L4.place(x=10,y=200)
    E4 = Entry(newwin, bd=7)
    E4.place(x=100,y=200)
    L5 = Label(newwin, text="MOBILE")
    L5.place(x=10,y=250)
    E5 = Entry(newwin, bd=7)
    E5.place(x=100,y=250)
    sub=Button(newwin,text="Submit",command=add_query)
    sub.place(x=120,y=350)

def del_data(root,db):
    def delete():
        global root
        prn = E1.get()
        if(len(prn)==0):
            tkMessageBox.showwarning("WARNING", "Enter a Valid PRN")
            return
        if db.students.count_documents({ 'PRN': prn }, limit = 1)==0:
            tkMessageBox.showwarning("ERROR", "STUDENT Does Not Exist")
            return
        else:
            db.students.delete_one({'PRN':prn})
        newwin.destroy()
        tkMessageBox.showinfo("Delete Student", "Student Deleted")
    newwin=Toplevel(root)
    newwin.geometry('400x350')
    newwin.title("Delete STUDENT")
    L1 = Label(newwin, text="PRN")
    L1.place(x=10, y=50)
    E1 = Entry(newwin,bd=5)
    E1.place(x=100, y=50)
    sub = Button(newwin, text="Delete Entry", command=delete)
    sub.place(x=120, y=200)

def update_data(root,db):
	def UPDD():
		global root
		prn = E6.get()
		name = E7.get()
		email = E8.get()
		batch = E9.get()
		mobile = E10.get()
		if(len(prn)==0):
			tkMessageBox.showwarning("WARNING", "Enter a Valid PRN")
			return

		if db.students.count_documents({ 'PRN': prn }, limit = 1)==0:
			tkMessageBox.showwarning("ERROR", "STUDENT Does Not Exist")
			return
		if(len(name)!=0):
			db.students.update_one({"PRN":prn},{"$set": {'NAME' : name}})
		if(len(email)!=0):
			db.students.update_one({"PRN":prn},{"$set": {'EMAIL' : email}})
		if(len(batch)!=0):
			db.students.update_one({"PRN":prn},{"$set": {'BATCH' : batch}})
		if(len(mobile)!=0):
			db.students.update_one({"PRN":prn},{"$set": {'MOBILE' : mobile}})
            
		
		newwin.destroy()
		tkMessageBox.showinfo("Update Student", "Student Updated")

	newwin = Toplevel(root)
	newwin.geometry('400x400')
	newwin.title("Update STUDENTS")
	
	
	L6 = Label(newwin, text="PRN")
	L6.place(x=10,y=50)
	E6 = Entry(newwin, bd=7)
	E6.place(x=100,y=50)
	L7 = Label(newwin, text="NAME")
	L7.place(x=10,y=100)
	E7 = Entry(newwin, bd=7)
	E7.place(x=100,y=100)
	L8 = Label(newwin, text="EMAIL")
	L8.place(x=10,y=150)
	E8 = Entry(newwin, bd=7)
	E8.place(x=100,y=150)
	L9 = Label(newwin, text="BATCH")
	L9.place(x=10,y=200)
	E9 = Entry(newwin, bd=7)
	E9.place(x=100,y=200)
	L10 = Label(newwin, text="MOBILE")
	L10.place(x=10,y=250)
	E10 = Entry(newwin, bd=7)
	E10.place(x=100,y=250)
	sub=Button(newwin,text="Submit",command=UPDD)
	sub.place(x=120,y=350)


def display(root,db):
	newwin=Toplevel(root)
	newwin.geometry('400x400')
	newwin.title("STUDENT Details")
	L1=Label(newwin,text="PRN")
	L1.grid(row=0,column=0)
	L2 = Label(newwin, text="NAME")
	L2.grid(row=0, column=2)
	L3=Label(newwin,text="EMAIL")
	L3.grid(row=0,column=4)
	L4=Label(newwin,text="BATCH")
	L4.grid(row=0,column=6)
	L5=Label(newwin,text="MOBILE")
	L5.grid(row=0,column=8)
	i=1
	for x in db.students.find():
		y=len(x)
		# print(len(x))
		L1 = Label(newwin, text=x['PRN'])
		L1.grid(row=i, column=0)
		L2 = Label(newwin, text=x['NAME'])
		L2.grid(row=i, column=2)
		L3 = Label(newwin, text=x['EMAIL'])
		L3.grid(row=i, column=4)
		L4 = Label(newwin, text=x['BATCH'])
		L4.grid(row=i, column=6)
		if y==6:
			L5 = Label(newwin, text=x['MOBILE'])
			L5.grid(row=i, column=8)
		i+=1

add= Button(root,text='Add New STUDENTS',command=lambda:add_STUDENTS(root,db))
delete= Button(root,text='Delete STUDENTS Entry',command=lambda:del_data(root,db))
update= Button(root,text='Update STUDENTS Info',command=lambda:update_data(root,db))
show= Button(root,text='Show STUDENTS Details',command=lambda:display(root,db))
add.place(x=100,y=100)
delete.place(x=100,y=150)
update.place(x=100,y=200)
show.place(x=100,y=250)
root.mainloop()


