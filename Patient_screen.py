# -*- coding: utf-8 -*-
"""
Created on Wed May  9 00:22:22 2018

@author: varun
"""
from tkinter import *
import sqlite3
class Patient_1:
	db_name='C:\\A\\sem 4\\intro to python\\final_project\\EHR\\EHR.db'
	def __init__(self,master):
		self.master=master
		self.master.geometry("300x100+629+230")
		self.master.title("Patient View")
		self.master.configure(background="#d9d9d9")
		
#		self.Frame1 = Frame(master)
#		self.Frame1.place(relx=0.03, rely=0.22, relheight=0.62, relwidth=0.94)
#		self.Frame1.configure(relief=GROOVE)
#		self.Frame1.configure(borderwidth="2")
#		self.Frame1.configure(relief=GROOVE)
#		self.Frame1.configure(background="#d9d9d9")
#		self.Frame1.configure(width=565)
#		


		
	
		self.Button1 = Button(self.master)
		self.Button1.place(relx=0.10, rely=0.25, height=33, width=76)
		self.Button1.configure(activebackground="#d9d9d9")
		self.Button1.configure(activeforeground="#000000")
		self.Button1.configure(background="#d9d9d9")
		self.Button1.configure(disabledforeground="#a3a3a3")
		self.Button1.configure(foreground="#000000")
		self.Button1.configure(highlightbackground="#d9d9d9")
		self.Button1.configure(highlightcolor="black")
		self.Button1.configure(pady="0")
		self.Button1.configure(text='''Add''')
		self.Button1.configure(width=76)
		
		
		self.tv=ttk.Treeview(self.master,height=30)
		self.tv['columns'] = ('fname', 'lname')
		 #Age', 'NPI', 'pcp', 'parentclinic', 'address', 'Phone')
		#self.tv=ttk.Treeview(height=30,columns=3)
		self.tv.heading("#0", text='Patient_id', anchor='w')
		self.tv.column("#0", stretch=NO, width=70, anchor="w")
		self.tv.heading('fname', text='First_name')
		self.tv.column('fname', anchor='center', width=70)
		#self.tv.heading('fname', text='First_name')
		#self.tv.column('fname', anchor='center', width=70)
		self.tv.heading('lname', text='Last_name')
		self.tv.column('lname', anchor='center', width=70)
		
		#self.tree.place(relx=0.86, rely=0.59, height=33, width=76)
		#self.tree=ttk.Treeview(height=30,columns=2)
		#self.tv.grid(row=4,column=0,columnspan=2)
		#self.tv.heading('#0', text='Patient_id',anchor=W)
		#self.tv.heading('#0', text='Patient_id',anchor=W)	
		#self.tv.heading('#1', text='First_name',anchor=W)	
		#self.tv.heading('lname', text='Last_name',anchor=W)
		#self.tv.heading('#2', text='Age',anchor=W)
#		self.tv.heading(10, text='NPI',anchor=W)
#		self.tv.heading(12, text='pcp',anchor=W)
#		self.tv.heading(14, text='parentclinic',anchor=W)
#		self.tv.heading(16, text='address',anchor=W)
#		self.tv.heading(18, text='Phone',anchor=W)
		self.tv.pack()
		
		self.Button1_1 = Button(self.master)
		self.Button1_1.place(relx=0.40, rely=0.25, height=33, width=76)
		self.Button1_1.configure(activebackground="#d9d9d9")
		self.Button1_1.configure(activeforeground="#000000")
		self.Button1_1.configure(background="#d9d9d9")
		self.Button1_1.configure(disabledforeground="#a3a3a3")
		self.Button1_1.configure(foreground="#000000")
		self.Button1_1.configure(highlightbackground="#d9d9d9")
		self.Button1_1.configure(highlightcolor="black")
		self.Button1_1.configure(pady="0")
		self.Button1_1.configure(text='''Update''')
		
		self.Button1_1_1 = Button(self.master)
		self.Button1_1_1.place(relx=0.7, rely=0.25, height=33, width=76)
		self.Button1_1_1.configure(activebackground="#d9d9d9")
		self.Button1_1_1.configure(activeforeground="#000000")
		self.Button1_1_1.configure(background="#d9d9d9")
		self.Button1_1_1.configure(disabledforeground="#a3a3a3")
		self.Button1_1_1.configure(foreground="#000000")
		self.Button1_1_1.configure(highlightbackground="#d9d9d9")
		self.Button1_1_1.configure(highlightcolor="black")
		self.Button1_1_1.configure(pady="0")
		self.Button1_1_1.configure(text='''Patient details''')
#		self.master=master
#		self.master.geometry("600x450+629+230")
#		self.master.title('Patient View')
#		self.master.configure(background="#d9d9d9")
#		
#		Frame1 =  LabelFrame(self.master,text='Add a patient')
#		Frame1.grid(row=0,column=1)
		
		#Frame.grid(row=0,coloumn=2)
		
#		self.add_button = Button(self.Frame1)
#		self.add_button.place(relx=0.28, rely=0.19, height=73, width=206)
#		self.add_button.configure(activebackground="#c0e6f1")
#		self.add_button.configure(activeforeground="#000000")
#		self.add_button.configure(background="#bff0f2")
#		self.add_button.configure(disabledforeground="#a3a3a3")
#		self.add_button.configure(foreground="#000000")
#		self.add_button.configure(highlightbackground="#d9d9d9")
#		self.add_button.configure(highlightcolor="black")
#		self.add_button.configure(pady="0")
#		self.add_button.configure(text='''Add patient''')
#		self.add_button.configure(width=206)
			
		
#		self.tree=ttk.Treeview(height=20,columns=2)
#		self.tree.grid(row=4,column=0,columnspan=2)
#		self.tree.heading('#0', text='First_name',anchor=W)	
#		self.tree.heading(2, text='Last_name',anchor=W)	
#		
		self.viewing_records()
		
	def run_query1(self,query,parameters=()):
		with 	sqlite3.connect(self.db_name) as conn:
			cursor=conn.cursor()
			query_result=cursor.execute(query,parameters)
			conn.commit()
		return query_result

	def viewing_records(self):
		records=self.tv.get_children()
		for element in records:
			self.tv.delete(element)
		query='SELECT patient_id,fname,lname FROM PATIENT'
		db_rows=self.run_query1(query)
		for row in db_rows:
			self.tv.insert('',0,text=row[0],values=row[1])
	