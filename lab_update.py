# -*- coding: utf-8 -*-
"""
Created on Thu May 10 23:43:06 2018

@author: varun
"""

class Lab_update:
def __init__(self, top=None):
	'''This class configures and populates the toplevel window.
	   top is the toplevel containing window.'''
	_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
	_fgcolor = '#000000'  # X11 color: 'black'
	_compcolor = '#d9d9d9' # X11 color: 'gray85'
	_ana1color = '#d9d9d9' # X11 color: 'gray85' 
	_ana2color = '#d9d9d9' # X11 color: 'gray85' 
	font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
		" roman -underline 0 -overstrike 0"
	font13 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
		"roman -underline 0 -overstrike 0"

	top.geometry("600x442+361+222")
	top.title("New Toplevel")
	top.configure(background="#d9d9d9")



	self.Entry1 = Entry(top)
	self.Entry1.place(relx=0.53, rely=0.07,height=20, relwidth=0.27)
	self.Entry1.configure(background="white")
	self.Entry1.configure(disabledforeground="#a3a3a3")
	self.Entry1.configure(font=font10)
	self.Entry1.configure(foreground="#000000")
	self.Entry1.configure(insertbackground="black")

	self.Entry1_1 = Entry(top)
	self.Entry1_1.place(relx=0.53, rely=0.16,height=20, relwidth=0.27)
	self.Entry1_1.configure(background="white")
	self.Entry1_1.configure(disabledforeground="#a3a3a3")
	self.Entry1_1.configure(font=font10)
	self.Entry1_1.configure(foreground="#000000")
	self.Entry1_1.configure(highlightbackground="#d9d9d9")
	self.Entry1_1.configure(highlightcolor="black")
	self.Entry1_1.configure(insertbackground="black")
	self.Entry1_1.configure(selectbackground="#c4c4c4")
	self.Entry1_1.configure(selectforeground="black")

	self.Entry1_1_1 = Entry(top)
	self.Entry1_1_1.place(relx=0.53, rely=0.25,height=20, relwidth=0.27)
	self.Entry1_1_1.configure(background="white")
	self.Entry1_1_1.configure(disabledforeground="#a3a3a3")
	self.Entry1_1_1.configure(font=font10)
	self.Entry1_1_1.configure(foreground="#000000")
	self.Entry1_1_1.configure(highlightbackground="#d9d9d9")
	self.Entry1_1_1.configure(highlightcolor="black")
	self.Entry1_1_1.configure(insertbackground="black")
	self.Entry1_1_1.configure(selectbackground="#c4c4c4")
	self.Entry1_1_1.configure(selectforeground="black")

	self.Entry1_1_1_1 = Entry(top)
	self.Entry1_1_1_1.place(relx=0.53, rely=0.34,height=20, relwidth=0.27)
	self.Entry1_1_1_1.configure(background="white")
	self.Entry1_1_1_1.configure(disabledforeground="#a3a3a3")
	self.Entry1_1_1_1.configure(font=font10)
	self.Entry1_1_1_1.configure(foreground="#000000")
	self.Entry1_1_1_1.configure(highlightbackground="#d9d9d9")
	self.Entry1_1_1_1.configure(highlightcolor="black")
	self.Entry1_1_1_1.configure(insertbackground="black")
	self.Entry1_1_1_1.configure(selectbackground="#c4c4c4")
	self.Entry1_1_1_1.configure(selectforeground="black")

	self.Entry1_1_1_1_1 = Entry(top)
	self.Entry1_1_1_1_1.place(relx=0.53, rely=0.43, height=20, relwidth=0.27)

	self.Entry1_1_1_1_1.configure(background="white")
	self.Entry1_1_1_1_1.configure(disabledforeground="#a3a3a3")
	self.Entry1_1_1_1_1.configure(font=font10)
	self.Entry1_1_1_1_1.configure(foreground="#000000")
	self.Entry1_1_1_1_1.configure(highlightbackground="#d9d9d9")
	self.Entry1_1_1_1_1.configure(highlightcolor="black")
	self.Entry1_1_1_1_1.configure(insertbackground="black")
	self.Entry1_1_1_1_1.configure(selectbackground="#c4c4c4")
	self.Entry1_1_1_1_1.configure(selectforeground="black")

	self.Entry1_1_1_1_1_1 = Entry(top)
	self.Entry1_1_1_1_1_1.place(relx=0.53, rely=0.52, height=20
			, relwidth=0.27)
	self.Entry1_1_1_1_1_1.configure(background="white")
	self.Entry1_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
	self.Entry1_1_1_1_1_1.configure(font=font10)
	self.Entry1_1_1_1_1_1.configure(foreground="#000000")
	self.Entry1_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
	self.Entry1_1_1_1_1_1.configure(highlightcolor="black")
	self.Entry1_1_1_1_1_1.configure(insertbackground="black")
	self.Entry1_1_1_1_1_1.configure(selectbackground="#c4c4c4")
	self.Entry1_1_1_1_1_1.configure(selectforeground="black")

	self.Entry1_1_1_1_1_1_1 = Entry(top)
	self.Entry1_1_1_1_1_1_1.place(relx=0.53, rely=0.61, height=20
			, relwidth=0.27)
	self.Entry1_1_1_1_1_1_1.configure(background="white")
	self.Entry1_1_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
	self.Entry1_1_1_1_1_1_1.configure(font=font10)
	self.Entry1_1_1_1_1_1_1.configure(foreground="#000000")
	self.Entry1_1_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
	self.Entry1_1_1_1_1_1_1.configure(highlightcolor="black")
	self.Entry1_1_1_1_1_1_1.configure(insertbackground="black")
	self.Entry1_1_1_1_1_1_1.configure(selectbackground="#c4c4c4")
	self.Entry1_1_1_1_1_1_1.configure(selectforeground="black")

	self.Label1 = Label(top)
	self.Label1.place(relx=0.35, rely=0.07, height=21, width=75)
	self.Label1.configure(background="#d9d9d9")
	self.Label1.configure(disabledforeground="#a3a3a3")
	self.Label1.configure(foreground="#000000")
	self.Label1.configure(text='''encounter_id''')

	self.Label1_1 = Label(top)
	self.Label1_1.place(relx=0.37, rely=0.16, height=21, width=64)
	self.Label1_1.configure(activebackground="#f9f9f9")
	self.Label1_1.configure(activeforeground="black")
	self.Label1_1.configure(background="#d9d9d9")
	self.Label1_1.configure(disabledforeground="#a3a3a3")
	self.Label1_1.configure(foreground="#000000")
	self.Label1_1.configure(highlightbackground="#d9d9d9")
	self.Label1_1.configure(highlightcolor="black")
	self.Label1_1.configure(text='''description''')
	self.Label1_1.configure(width=64)

	self.Label1_1_1 = Label(top)
	self.Label1_1_1.place(relx=0.38, rely=0.25, height=21, width=34)
	self.Label1_1_1.configure(activebackground="#f9f9f9")
	self.Label1_1_1.configure(activeforeground="black")
	self.Label1_1_1.configure(background="#d9d9d9")
	self.Label1_1_1.configure(disabledforeground="#a3a3a3")
	self.Label1_1_1.configure(foreground="#000000")
	self.Label1_1_1.configure(highlightbackground="#d9d9d9")
	self.Label1_1_1.configure(highlightcolor="black")
	self.Label1_1_1.configure(text='''loinc''')

	self.Label1_1_1_1 = Label(top)
	self.Label1_1_1_1.place(relx=0.37, rely=0.43, height=21, width=64)
	self.Label1_1_1_1.configure(activebackground="#f9f9f9")
	self.Label1_1_1_1.configure(activeforeground="black")
	self.Label1_1_1_1.configure(background="#d9d9d9")
	self.Label1_1_1_1.configure(disabledforeground="#a3a3a3")
	self.Label1_1_1_1.configure(foreground="#000000")
	self.Label1_1_1_1.configure(highlightbackground="#d9d9d9")
	self.Label1_1_1_1.configure(highlightcolor="black")
	self.Label1_1_1_1.configure(text='''labresult''')
	self.Label1_1_1_1.configure(width=64)

	self.Label1_1_1_1_1 = Label(top)
	self.Label1_1_1_1_1.place(relx=0.38, rely=0.52, height=21, width=34)
	self.Label1_1_1_1_1.configure(activebackground="#f9f9f9")
	self.Label1_1_1_1_1.configure(activeforeground="black")
	self.Label1_1_1_1_1.configure(background="#d9d9d9")
	self.Label1_1_1_1_1.configure(disabledforeground="#a3a3a3")
	self.Label1_1_1_1_1.configure(foreground="#000000")
	self.Label1_1_1_1_1.configure(highlightbackground="#d9d9d9")
	self.Label1_1_1_1_1.configure(highlightcolor="black")
	self.Label1_1_1_1_1.configure(text='''labcost''')

	self.Label1_1_1_1_1_1 = Label(top)
	self.Label1_1_1_1_1_1.place(relx=0.37, rely=0.61, height=21, width=64)
	self.Label1_1_1_1_1_1.configure(activebackground="#f9f9f9")
	self.Label1_1_1_1_1_1.configure(activeforeground="black")
	self.Label1_1_1_1_1_1.configure(background="#d9d9d9")
	self.Label1_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
	self.Label1_1_1_1_1_1.configure(foreground="#000000")
	self.Label1_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
	self.Label1_1_1_1_1_1.configure(highlightcolor="black")
	self.Label1_1_1_1_1_1.configure(text='''labdate''')
	self.Label1_1_1_1_1_1.configure(width=64)

	self.Label1_1_1_1_1_1_1 = Label(top)
	self.Label1_1_1_1_1_1_1.place(relx=0.38, rely=0.34, height=21, width=34)
	self.Label1_1_1_1_1_1_1.configure(activebackground="#f9f9f9")
	self.Label1_1_1_1_1_1_1.configure(activeforeground="black")
	self.Label1_1_1_1_1_1_1.configure(background="#d9d9d9")
	self.Label1_1_1_1_1_1_1.configure(disabledforeground="#a3a3a3")
	self.Label1_1_1_1_1_1_1.configure(foreground="#000000")
	self.Label1_1_1_1_1_1_1.configure(highlightbackground="#d9d9d9")
	self.Label1_1_1_1_1_1_1.configure(highlightcolor="black")
	self.Label1_1_1_1_1_1_1.configure(text='''npi''')

	self.Button1 = Button(top)
	self.Button1.place(relx=0.23, rely=0.77, height=34, width=117)
	self.Button1.configure(activebackground="#d9d9d9")
	self.Button1.configure(activeforeground="#000000")
	self.Button1.configure(background="#d9d9d9")
	self.Button1.configure(disabledforeground="#a3a3a3")
	self.Button1.configure(foreground="#000000")
	self.Button1.configure(highlightbackground="#d9d9d9")
	self.Button1.configure(highlightcolor="black")
	self.Button1.configure(pady="0")
	self.Button1.configure(text='''Cancel''')
	self.Button1.configure(width=117)

	self.Button1_1 = Button(top)
	self.Button1_1.place(relx=0.62, rely=0.77, height=34, width=117)
	self.Button1_1.configure(activebackground="#d9d9d9")
	self.Button1_1.configure(activeforeground="#000000")
	self.Button1_1.configure(background="#d9d9d9")
	self.Button1_1.configure(disabledforeground="#a3a3a3")
	self.Button1_1.configure(foreground="#000000")
	self.Button1_1.configure(highlightbackground="#d9d9d9")
	self.Button1_1.configure(highlightcolor="black")
	self.Button1_1.configure(pady="0")
	self.Button1_1.configure(text='''Save Changes''')

	self.Label2 = Label(top)
	self.Label2.place(relx=0.03, rely=0.0, height=31, width=194)
	self.Label2.configure(background="#d9d9d9")
	self.Label2.configure(disabledforeground="#a3a3a3")
	self.Label2.configure(font=font13)
	self.Label2.configure(foreground="#000000")
	self.Label2.configure(text='''update Lab Details''')
	self.Label2.configure(width=194)