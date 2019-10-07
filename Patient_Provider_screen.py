# -*- coding: utf-8 -*-
"""
Created on Tue May  8 23:29:23 2018

@author: varun
"""
from tkinter import *
from Patient_screen import *
from test_patient_gui import *


class Screen_2:
	
	def myquit1(self):
		self.master.destroy()
		
	def Patient1(self):
		root4=Toplevel(self.master)
		mygui3=Patient_1(root4)
		#self.master.destroy()
	
	#def patient_view1(self):
	#	conn=pymysql.connect(host='local',user='root',password='Mysql@2611',db='ehr')

	#self.master.destroy()
	
	#def provider_view1(self):
		#self.master.destroy()
		
		
	def __init__(self,master):
		self.master=master
		self.master.geometry("600x450+629+230")
		self.master.title("Select a View")
		self.master.configure(background="#d9d9d9")
		
		
		self.Frame1 = Frame(master)
		self.Frame1.place(relx=0.12, rely=0.09, relheight=0.81, relwidth=0.78)
		self.Frame1.configure(relief=GROOVE)
		self.Frame1.configure(borderwidth="2")
		self.Frame1.configure(relief=GROOVE)
		self.Frame1.configure(background="#d9d9d9")
		self.Frame1.configure(width=465)
		
		
		self.Patient_button = Button(self.Frame1)
		self.Patient_button.place(relx=0.28, rely=0.19, height=73, width=206)
		self.Patient_button.configure(activebackground="#c0e6f1")
		self.Patient_button.configure(activeforeground="#000000")
		self.Patient_button.configure(background="#bff0f2")
		self.Patient_button.configure(disabledforeground="#a3a3a3")
		self.Patient_button.configure(foreground="#000000")
		self.Patient_button.configure(highlightbackground="#d9d9d9")
		self.Patient_button.configure(highlightcolor="black")
		self.Patient_button.configure(pady="0")
		self.Patient_button.configure(text='''Patient View''')
		self.Patient_button.configure(width=206)
		self.Patient_button.configure(command=self.Patient1)
		
		
		self.Provider_button = Button(self.Frame1)
		self.Provider_button.place(relx=0.28, rely=0.58, height=73, width=206)
		self.Provider_button.configure(activebackground="#c0e6f1")
		self.Provider_button.configure(activeforeground="#000000")
		self.Provider_button.configure(background="#bff0f2")
		self.Provider_button.configure(disabledforeground="#a3a3a3")
		self.Provider_button.configure(foreground="#000000")
		self.Provider_button.configure(highlightbackground="#d9d9d9")
		self.Provider_button.configure(highlightcolor="black")
		self.Provider_button.configure(pady="0")
		self.Provider_button.configure(text='''Provider View''')
		
		
		
		self.back_button = Button(self.Frame1)
		self.back_button.place(relx=0.45, rely=0.92, height=23, width=50)
		self.back_button.configure(activebackground="#c0e6f1")
		self.back_button.configure(activeforeground="#000000")
		self.back_button.configure(background="#d9d9d9")
		self.back_button.configure(disabledforeground="#a3a3a3")
		self.back_button.configure(foreground="#000000")
		self.back_button.configure(highlightbackground="#d9d9d9")
		self.back_button.configure(highlightcolor="black")
		self.back_button.configure(pady="0")
		self.back_button.configure(text='''back''')
		self.back_button.configure(command=self.myquit1)