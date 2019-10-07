# -*- coding: utf-8 -*-
"""
Created on Tue May  8 23:20:30 2018

@author: varun
"""
from Intermiediate_screen import *
from tkinter import *
from Login_Screen1 import *
from Patient_Provider_screen import *
from Registration_screen	import *
from pymysql import *
from test_patient_gui import *
from Intermiediate_screen import *

def main():
		root=Tk()
		login_screen1=Login_screen(root)
		root.mainloop()

if __name__=='__main__':
	main()
	

