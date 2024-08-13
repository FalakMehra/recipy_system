import tkinter
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect
import adminlogin
import userlogin

class Main:
    def __init__(self):
        self.bgcolour='#C1C3C1'
        self.root=tkinter.Tk()
        self.root.title('Add title')
        self.root.state('zoomed')
        self.root.configure(bg=self.bgcolour)

        self.mainLabel=tkinter.Label(self.root,text="Recipy_System",font=('arial',28,'bold'),bg='#6E726E',relief=tkinter.SUNKEN)
        self.mainLabel.pack(pady=20,ipadx=10,ipady=10)

        self.bt1 = tkinter.Button(self.root, text='Admin Login', font=('arial', 20, 'bold'), bg='#787D78',
                                  foreground='black', activebackground='black', activeforeground="white"
                                  , relief=tkinter.SUNKEN ,command=lambda: adminlogin.Main())
        self.bt1.pack(pady=10,anchor="w")

        self.bt2 = tkinter.Button(self.root, text='User Login', font=('arial', 20, 'bold'), bg='#787D78',
                                  foreground='black', activebackground='black', activeforeground="white"
                                  , relief=tkinter.SUNKEN ,command=lambda:userlogin.Main())
        self.bt2.pack(pady=10,anchor="w")

        self.root.mainloop()

obj=Main()
