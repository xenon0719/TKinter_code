import tkinter
import tkinter.font

class Application(tkinter.Frame):

    def __init__(self,master):
        tkinter.Frame.__init__(self,master)
        self.config(bg="pink")
        self.pack()
        self.CreateWidgets()
        

    def CreateWidgets(self):
        self.label1=tkinter.Label(self)
        self.label1.config(text="Hello World")
        self.label1.config(bg="black")
        self.label1.config(fg="pink")
        self.myFont=tkinter.font.Font(family="Helvitica",size=26)
        self.label1.config(font=self.myFont)
        self.label1.pack()

    
        self.label1=tkinter.Label(self)
        self.label1.config(text="We are Gabriel and Ferdinand")
        self.label1.config(bg="black")
        self.label1.config(fg="pink")
        self.myFont=tkinter.font.Font(family="Helvitica",size=26)
        self.label1.config(font=self.myFont)
        self.label1.pack()
        
    
        self.label1=tkinter.Label(self)
        self.label1.config(text="Nice to meet you")
        self.label1.config(bg="black")
        self.label1.config(fg="pink")
        self.myFont=tkinter.font.Font(family="Helvitica",size=26)
        self.label1.config(font=self.myFont)
        self.label1.pack()

root=tkinter.Tk()
app=Application(master=root)
app.mainloop()
root.destroy()
