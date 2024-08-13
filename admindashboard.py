from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import addcategory
import viewcategory
import addadmin
import viewadmin
import adminChangePassword



class Main:
    def __init__(self,adminid,adminname,adminemail,adminrole):
        self.bgcolour = "#C1C3C1"
        self.root = Tk()
        self.root.title('Admin Dashboard')
        self.root.state('zoomed')
        self.root.configure(bg=self.bgcolour)

        self.rootMenu = Menu(self.root)

        self.root.configure(menu=self.rootMenu)
        '''
        # File Menu
        self.fileMenu = Menu(self.rootMenu, tearoff=0) # Initializing File Menu
        # Creating an option(button) in rootMenu with name 'file' and linked fileMenu with it.
        self.rootMenu.add_cascade(label='File', menu=self.fileMenu)
        # Adding Buttons in the File Menu
        self.fileMenu.add_command(label="New Project")
        self.fileMenu.add_command(label="New")
        self.fileMenu.add_command(label="New Scratch File")
        '''

        self.mainLabel = Label(self.root, text=f"Welcome {adminname}", font=('', 28, 'bold'), bg="#141301",fg="white",
                                       relief=SUNKEN)
        self.mainLabel.pack(pady=20, ipadx=10, ipady=10)

        if adminrole=='SUPER ADMIN':
            self.catMenu = Menu(self.rootMenu, tearoff=0)
            self.catMenu.add_command(label='Add Admin', command=lambda: addadmin.Main())
            self.catMenu.add_command(label='View Admin', command=lambda: viewadmin.Main())
            self.rootMenu.add_cascade(label="Admin", menu=self.catMenu)

        self.catMenu = Menu(self.rootMenu, tearoff=0)
        self.catMenu.add_command(label='Add Category', command=lambda:addcategory.Main())
        self.catMenu.add_command(label='View Category', command=lambda:viewcategory.Main())
        self.rootMenu.add_cascade(label="Category", menu=self.catMenu)


        # self.catMenu = Menu(self.rootMenu, tearoff=0)
        # self.catMenu.add_command(label='Add Admin', command=lambda: addadmin.Main())
        # self.catMenu.add_command(label='View Admin', command=lambda: viewadmin.Main())
        # self.rootMenu.add_cascade(label="Admin", menu=self.catMenu)

        self.catMenu = Menu(self.rootMenu, tearoff=0)
        self.rootMenu.add_cascade(label="Profile", menu=self.catMenu)
        self.catMenu.add_command(label='Change password', command=lambda: adminChangePassword.Main(adminemail))
        self.catMenu.add_command(label='Logout',command=lambda:self.root.destroy())
        self.root.mainloop()



# obj = Main()