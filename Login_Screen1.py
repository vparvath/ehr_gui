# -*- coding: utf-8 -*-
"""
Created on Tue May  8 23:20:57 2018

@author: varun
"""
import sqlite3
from tkinter import *
from tkinter import messagebox
from Patient_Provider_screen import *
from Registration_screen import *

class Login_screen:
	def finish(self):
		self.master.destroy()
	
	def login1(self):
		db_name='cohr.db'
		#Establish Connection
		conn = sqlite3.connect('cohr.db')
		c = conn.cursor()
		find_user = 'Select * from login where username = ? and password = ?'
		c.execute(find_user,[(self.Entry1.get()),(self.Entry1_1.get())])
		result=c.fetchall()
		print(result)
		if len(result)==1:
			root2=Toplevel(self.master)
			mygui1=Screen_2(root2)
			
		else:
			messagebox.showerror('failed','User_name or Password is incorrect')
		conn.close()
#		with sqlite3.connect('db_name') as db:
#			c = db.cursor()
#			find_user = ('Select * from login where username = ? and password = ?')
#			c.execute(find_user,[(self.Entry1.get()),(self.Entry1_1.get())])
#			result = c.fetchall()
#			if result and self:
#				root2=Toplevel(self.master)
#				mygui1=Screen_2(root2)
#			else:
#				messagebox.showerror('User_name or Password is incorrect')
			
		 
	def register1(self):
		root3=Toplevel(self.master)
		mygui2=Register1(root3)
		
		
	
	def __init__(self,master):
		
		self.master=master
		self.master.geometry("600x450+629+230")
		self.master.title("Login")
		self.master.configure(background="#d9d9d9")
		
		self.Frame1=Frame(self.master)
		self.Frame1.place(relx=0.02, rely=0.09, relheight=0.78, relwidth=0.97)
		self.Frame1.configure(relief=GROOVE)
		self.Frame1.configure(borderwidth="2")
		self.Frame1.configure(relief=GROOVE)
		self.Frame1.configure(background="#d9d9d9")
		self.Frame1.configure(width=580)
		
		self.heading1=Label(self.Frame1)
		self.heading1.place(relx=0.19, rely=0.03, height=46, width=412)
		self.heading1.configure(background="#d9d9d9")
		self.heading1.configure(disabledforeground="#a3a3a3")
		self.heading1.configure(font=14)
		self.heading1.configure(foreground="#000000")
		self.heading1.configure(text='''Welcome to COHR''')
		self.heading1.configure(width=412)
		
		self.Frame2 = Frame(self.Frame1)
		self.Frame2.place(relx=0.19, rely=0.71, relheight=0.21, relwidth=0.66)
		self.Frame2.configure(relief=GROOVE)
		self.Frame2.configure(borderwidth="2")
		self.Frame2.configure(relief=GROOVE)
		self.Frame2.configure(background="#d9d9d9")
		self.Frame2.configure(width=385)
		
		self.cancel_bttn = Button(self.Frame2)
		self.cancel_bttn.place(relx=0.1, rely=0.27, height=33, width=76)
		self.cancel_bttn.configure(activebackground="#d9d9d9")
		self.cancel_bttn.configure(activeforeground="#000000")
		self.cancel_bttn.configure(background="#d9d9d9")
		self.cancel_bttn.configure(disabledforeground="#a3a3a3")
		self.cancel_bttn.configure(foreground="#000000")
		self.cancel_bttn.configure(highlightbackground="#d9d9d9")
		self.cancel_bttn.configure(highlightcolor="black")
		self.cancel_bttn.configure(pady="0")
		self.cancel_bttn.configure(text='Quit')
		self.cancel_bttn.configure(command=self.finish)
		self.cancel_bttn.configure(width=76)
		
		
		self.login_bttn = Button(self.Frame2)
		self.login_bttn.place(relx=0.73, rely=0.29, height=33, width=76)
		self.login_bttn.configure(activebackground="#d9d9d9")
		self.login_bttn.configure(activeforeground="#000000")
		self.login_bttn.configure(background="#d9d9d9")
		self.login_bttn.configure(disabledforeground="#a3a3a3")
		self.login_bttn.configure(foreground="#000000")
		self.login_bttn.configure(highlightbackground="#d9d9d9")
		self.login_bttn.configure(highlightcolor="black")
		self.login_bttn.configure(pady="0")
		self.login_bttn.configure(text='''Login''')
		self.login_bttn.configure(command=self.login1)
		
		self.register_bttn = Button(self.Frame2)
		self.register_bttn.place(relx=0.42, rely=0.29, height=33, width=76)
		self.register_bttn.configure(activebackground="#d9d9d9")
		self.register_bttn.configure(activeforeground="#000000")
		self.register_bttn.configure(background="#d9d9d9")
		self.register_bttn.configure(disabledforeground="#a3a3a3")
		self.register_bttn.configure(foreground="#000000")
		self.register_bttn.configure(highlightbackground="#d9d9d9")
		self.register_bttn.configure(highlightcolor="black")
		self.register_bttn.configure(pady="0")
		self.register_bttn.configure(text='''Register''')
		self.register_bttn.configure(command=self.register1)
		
		self.Frame3 = Frame(self.Frame1)
		self.Frame3.place(relx=0.09, rely=0.2, relheight=0.5, relwidth=0.84)
		self.Frame3.configure(relief=GROOVE)
		self.Frame3.configure(borderwidth="2")
		self.Frame3.configure(relief=GROOVE)
		self.Frame3.configure(background="#d9d9d9")
		self.Frame3.configure(width=485)
		
		self.label_user = Label(self.Frame3)
		self.label_user.place(relx=0.14, rely=0.4, height=26, width=76)
		self.label_user.configure(background="#d9d9d9")
		self.label_user.configure(disabledforeground="#a3a3a3")
		self.label_user.configure(foreground="#000000")
		self.label_user.configure(text='''User name''')
		
		self.label_passwrd = Label(self.Frame3)
		self.label_passwrd.place(relx=0.14, rely=0.64, height=26, width=76)
		self.label_passwrd.configure(activebackground="#f9f9f9")
		self.label_passwrd.configure(activeforeground="black")
		self.label_passwrd.configure(background="#d9d9d9")
		self.label_passwrd.configure(disabledforeground="#a3a3a3")
		self.label_passwrd.configure(foreground="#000000")
		self.label_passwrd.configure(highlightbackground="#d9d9d9")
		self.label_passwrd.configure(highlightcolor="black")
		self.label_passwrd.configure(text='''Password''')
		
		
		self.Entry1 = Entry(self.Frame3)
		self.Entry1.place(relx=0.35, rely=0.4,height=24, relwidth=0.42)
		self.Entry1.configure(background="white")
		self.Entry1.configure(disabledforeground="#a3a3a3")
		self.Entry1.configure(font="TkFixedFont")
		self.Entry1.configure(foreground="#000000")
		self.Entry1.configure(insertbackground="black")
		
		self.Entry1_1 = Entry(self.Frame3)
		self.Entry1_1.place(relx=0.35, rely=0.64,height=24, relwidth=0.42)
		self.Entry1_1.configure(background="white")
		self.Entry1_1.configure(disabledforeground="#a3a3a3")
		self.Entry1_1.configure(font="TkFixedFont")
		self.Entry1_1.configure(foreground="#000000")
		self.Entry1_1.configure(highlightbackground="#d9d9d9")
		self.Entry1_1.configure(highlightcolor="black")
		self.Entry1_1.configure(insertbackground="black")
		self.Entry1_1.configure(selectbackground="#c4c4c4")
		self.Entry1_1.configure(selectforeground="black")
		
		
		self.label_login = Label(self.Frame3)
		self.label_login.place(relx=0.39, rely=0.06, height=37, width=156)
		self.label_login.configure(background="#d9d9d9")
		self.label_login.configure(disabledforeground="#a3a3a3")
		self.label_login.configure(font=9)
		self.label_login.configure(foreground="#000000")
		self.label_login.configure(text='''Login/Register''')