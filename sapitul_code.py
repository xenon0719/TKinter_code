import tkinter

class Application(tkinter.Frame):

    def __init__(self,master):
        tkinter.Frame.__init__(self,master)
        self.pack()
        self.CreateWidgets()

    def CreateWidgets(self):
        self.textbox1=tkinter.Text()
        self.textbox1.pack()
        self.button1=tkinter.Button()
        self.button1["command"]=self.button1_click
        self.button1["text"]="click"
        self.button1.pack()
        self.quitbutton=tkinter.Button()
        self.quitbutton["text"]="Quit"
        self.quitbutton["command"]=self.quit
        self.quitbutton.pack()
    def button1_click(self):
        text=self.textbox1.get(0.0,tkinter.END)
        
        print(text.upper())
        print(text.lower())
        print(text.title())

        

root=tkinter.Tk()
app=Application(master=root)
app.mainloop()
root.destroy()
