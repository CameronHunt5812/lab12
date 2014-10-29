####################################################
#
#              70pt - Add a new Button 
#                  called "Goodbye"
#
####################################################

from Tkinter import *

class MyApp:
	def __init__(self, parent):
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1["text"]= "Hello"
		self.button1["background"] = "red"
		self.button1.pack(side=LEFT)	### (1)


		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="World!")  
		self.button2.configure(background="green")               
		self.button2.pack(side=LEFT)	 ### (2)
		

		self.button3 = Button(self.myContainer1)
		self.button3.configure(text="Test?", background="cyan")  
		self.button3.pack(side=LEFT)	  ### (3)
		
		self.button4 = Button(self.myContainer1)
		self.button4.configure(text="Goodbye", background="orange")  
		self.button4.pack(side=LEFT)	  ### (4)
	
		
root = Tk()
myapp = MyApp(root)
root.mainloop()