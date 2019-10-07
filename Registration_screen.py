# -*- coding: utf-8 -*-
"""
Created on Tue May  8 23:31:51 2018

@author: varun
"""
from tkinter import *
class Register1:
	
	def myquit2(self):
		self.master.destroy()
		
	#def save_to_database(self):
		#add back feature also
	
	def __init__(self,master):
		self.master=master
		self.master.geometry("400x250+629+230")
		self.master.title("Select View")
		self.master.configure(background="#d9d9d9")
		
		self.Frame1 = Frame(master)
		self.Frame1.place(relx=0.02, rely=0.03, relheight=0.95, relwidth=0.95)
		self.Frame1.configure(relief=GROOVE)
		self.Frame1.configure(borderwidth="2")
		self.Frame1.configure(relief=GROOVE)
		self.Frame1.configure(background="#d9d9d9")
		self.Frame1.configure(width=475)
		
		self.Entry1 = Entry(self.Frame1)
		self.Entry1.place(relx=0.46, rely=0.21,height=24, relwidth=0.43)
		self.Entry1.configure(background="white")
		self.Entry1.configure(disabledforeground="#a3a3a3")
		self.Entry1.configure(font=10)
		self.Entry1.configure(foreground="#000000")
		self.Entry1.configure(insertbackground="black")
		
		
		self.Entry1_1 = Entry(self.Frame1)
		self.Entry1_1.place(relx=0.46, rely=0.39,height=24, relwidth=0.43)
		self.Entry1_1.configure(background="white")
		self.Entry1_1.configure(disabledforeground="#a3a3a3")
		self.Entry1_1.configure(font=10)
		self.Entry1_1.configure(foreground="#000000")
		self.Entry1_1.configure(highlightbackground="#d9d9d9")
		self.Entry1_1.configure(highlightcolor="black")
		self.Entry1_1.configure(insertbackground="black")
		self.Entry1_1.configure(selectbackground="#c4c4c4")
		self.Entry1_1.configure(selectforeground="black")
		
		self.Label1 = Label(self.Frame1)
		self.Label1.place(relx=0.17, rely=0.21, height=26, width=110)
		self.Label1.configure(background="#d9d9d9")
		self.Label1.configure(disabledforeground="#a3a3a3")
		self.Label1.configure(foreground="#000000")
		self.Label1.configure(text='''New user_name''')
		
		self.Label1_1_1 = Label(self.Frame1)
		self.Label1_1_1.place(relx=0.17, rely=0.39, height=26, width=110)
		self.Label1_1_1.configure(activebackground="#f9f9f9")
		self.Label1_1_1.configure(activeforeground="black")
		self.Label1_1_1.configure(background="#d9d9d9")
		self.Label1_1_1.configure(disabledforeground="#a3a3a3")
		self.Label1_1_1.configure(foreground="#000000")
		self.Label1_1_1.configure(highlightbackground="#d9d9d9")
		self.Label1_1_1.configure(highlightcolor="black")
		self.Label1_1_1.configure(text='''New Password''')
		
		self.Button1 = Button(self.Frame1)
		self.Button1.place(relx=0.17, rely=0.67, height=33, width=136)
		self.Button1.configure(activebackground="#d9d9d9")
		self.Button1.configure(activeforeground="#000000")
		self.Button1.configure(background="#d9d9d9")
		self.Button1.configure(disabledforeground="#a3a3a3")
		self.Button1.configure(foreground="#000000")
		self.Button1.configure(highlightbackground="#d9d9d9")
		self.Button1.configure(highlightcolor="black")
		self.Button1.configure(pady="0")
		self.Button1.configure(text='''Cancel''')
		self.Button1.configure(width=136)
		self.Button1.configure(command=self.myquit2)
		
		self.Button1_1 = Button(self.Frame1)
		self.Button1_1.place(relx=0.61, rely=0.66, height=33, width=136)
		self.Button1_1.configure(activebackground="#d9d9d9")
		self.Button1_1.configure(activeforeground="#000000")
		self.Button1_1.configure(background="#d9d9d9")
		self.Button1_1.configure(disabledforeground="#a3a3a3")
		self.Button1_1.configure(foreground="#000000")
		self.Button1_1.configure(highlightbackground="#d9d9d9")
		self.Button1_1.configure(highlightcolor="black")
		self.Button1_1.configure(pady="0")
		self.Button1_1.configure(text='''Confirm''')
		
		self.Entry1_2 = Entry(self.Frame1)
		self.Entry1_2.place(relx=0.46, rely=0.05,height=24, relwidth=0.43)
		self.Entry1_2.configure(background="white")
		self.Entry1_2.configure(disabledforeground="#a3a3a3")
		self.Entry1_2.configure(font=10)
		self.Entry1_2.configure(foreground="#000000")
		self.Entry1_2.configure(highlightbackground="#d9d9d9")
		self.Entry1_2.configure(highlightcolor="black")
		self.Entry1_2.configure(insertbackground="black")
		self.Entry1_2.configure(selectbackground="#c4c4c4")
		self.Entry1_2.configure(selectforeground="black")
		
		self.Label4 = Label(self.Frame1)
		self.Label4.place(relx=0.17, rely=0.05, height=26, width=110)
		self.Label4.configure(background="#d9d9d9")
		self.Label4.configure(disabledforeground="#a3a3a3")
		self.Label4.configure(foreground="#000000")
		self.Label4.configure(text='''Registration key''')