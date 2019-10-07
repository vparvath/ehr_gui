# -*- coding: utf-8 -*-
"""
Created on Wed May  9 15:29:33 2018

@author: varun
"""

from tkinter import *
from Patient_screen import *
from test_patient_gui import *
class Patient_details:
	
	def myquit4(self):
		self.master.destroy()
		
#	def patient_details1(self):
#		root5=Toplevel(self.master)
#		mygui4=Patient_2(root5)
		#self.master.destroy()
	
	#def patient_view1(self):
	#	conn=pymysql.connect(host='local',user='root',password='Mysql@2611',db='ehr')

	#self.master.destroy()
	
	#def provider_view1(self):
		#self.master.destroy()
		
		
	def __init__(self,master):
		self.master=master
		self.master.geometry("518x376+378+199")
		self.master.title("New Toplevel")
		self.master.configure(background="#d9d9d9")
		
		self.Frame1 = Frame(top)
		self.Frame1.place(relx=0.12, rely=0.13, relheight=0.73, relwidth=0.78)
		self.Frame1.configure(relief=GROOVE)
		self.Frame1.configure(borderwidth="2")
		self.Frame1.configure(relief=GROOVE)
		self.Frame1.configure(background="#d9d9d9")
		self.Frame1.configure(width=405)
		
		self.encounter_button = Button(self.Frame1)
		self.encounter_button.place(relx=0.37, rely=0.18, height=34, width=107)
		self.encounter_button.configure(activebackground="#d9d9d9")
		self.encounter_button.configure(activeforeground="#000000")
		self.encounter_button.configure(background="#d9d9d9")
		self.encounter_button.configure(disabledforeground="#a3a3a3")
		self.encounter_button.configure(foreground="#000000")
		self.encounter_button.configure(highlightbackground="#d9d9d9")
		self.encounter_button.configure(highlightcolor="black")
		self.encounter_button.configure(pady="0")
		self.encounter_button.configure(text='''Encounter''')
		self.encounter_button.configure(width=107)
		
		self.Button1_1 = Button(self.Frame1)
		self.Button1_1.place(relx=0.37, rely=0.41, height=34, width=107)
		self.Button1_1.configure(activebackground="#d9d9d9")
		self.Button1_1.configure(activeforeground="#000000")
		self.Button1_1.configure(background="#d9d9d9")
		self.Button1_1.configure(disabledforeground="#a3a3a3")
		self.Button1_1.configure(foreground="#000000")
		self.Button1_1.configure(highlightbackground="#d9d9d9")
		self.Button1_1.configure(highlightcolor="black")
		self.Button1_1.configure(pady="0")
		self.Button1_1.configure(text='''Medication''')
		
		self.Button1_1_1 = Button(self.Frame1)
		self.Button1_1_1.place(relx=0.37, rely=0.63, height=34, width=107)
		self.Button1_1_1.configure(activebackground="#d9d9d9")
		self.Button1_1_1.configure(activeforeground="#000000")
		self.Button1_1_1.configure(background="#d9d9d9")
		self.Button1_1_1.configure(disabledforeground="#a3a3a3")
		self.Button1_1_1.configure(foreground="#000000")
		self.Button1_1_1.configure(highlightbackground="#d9d9d9")
		self.Button1_1_1.configure(highlightcolor="black")
		self.Button1_1_1.configure(pady="0")
		self.Button1_1_1.configure(text='''Lab Investigations''')
		
		self.Button2 = Button(self.Frame1)
		self.Button2.place(relx=0.46, rely=0.84, height=24, width=36)
		self.Button2.configure(activebackground="#d9d9d9")
		self.Button2.configure(activeforeground="#000000")
		self.Button2.configure(background="#d9d9d9")
		self.Button2.configure(disabledforeground="#a3a3a3")
		self.Button2.configure(foreground="#000000")
		self.Button2.configure(highlightbackground="#d9d9d9")
		self.Button2.configure(highlightcolor="black")
		self.Button2.configure(pady="0")
		self.Button2.configure(text='''back''')
		self.back_button.configure(command=self.myquit4)