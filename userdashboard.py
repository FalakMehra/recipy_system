from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import addrecipy
import recipy_view
import user_rating
import viewrecipy
import adduser
import viewuser
import userChangePassword


class Main:
    def __init__(self,username,userid,useremail):
        self.bgcolour = "#C1C3C1"
        self.root = Tk()
        self.root.title('User Dashboard')
        self.root.state('zoomed')
        self.root.configure(bg=self.bgcolour)

        self.rootMenu = Menu(self.root)

        self.root.configure(menu=self.rootMenu)

        self.mainLabel = Label(self.root, text=f"Welcome {username}", font=('', 28, 'bold'), bg="#141301",
                               relief=SUNKEN,fg='white')
        self.mainLabel.pack(pady=20, ipadx=10, ipady=10)

        self.catMenu = Menu(self.rootMenu, tearoff=0)
        self.rootMenu.add_cascade(label='Recipy',menu=self.catMenu)
        self.catMenu.add_command(label='Add recipy', command=lambda: addrecipy.main(userid))
        self.catMenu.add_command(label='Recipy List', command=lambda: recipy_view.Main(userid,username))

        self.catMenu.add_command(label="View Recipy",command=lambda: viewrecipy.main(userid))
        self.catMenu.add_command(label="User_Rating", command=lambda: user_rating.main(userid))


        self.catMenu = Menu(self.rootMenu, tearoff=0)
        self.catMenu.add_command(label='Add User', command=lambda: adduser.Main())
        self.catMenu.add_command(label='View user', command=lambda: viewuser.Main())
        self.rootMenu.add_cascade(label="User", menu=self.catMenu)

        self.catMenu = Menu(self.rootMenu, tearoff=0)
        self.rootMenu.add_cascade(label="Profile", menu=self.catMenu)
        self.catMenu.add_command(label='Change password', command=lambda: userChangePassword.Main(useremail))
        self.catMenu.add_command(label='Logout',command=lambda:self.root.destroy())
        self.root.mainloop()



# if __name__=='__main__':
#     obj = Main()