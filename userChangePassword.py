import  tkinter
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect
class Main:
    def __init__(self,useremail):
        self.bgcolour = "#C1C3C1"
        self.root=tkinter.Tk()
        self.root.title('Add title')
        self.root.geometry('600x600')
        self.root.configure(bg=self.bgcolour)

        self.mainLabel=tkinter.Label(self.root,text="Change Password",font=('arial',28,'bold'),bg="#6E726E",fg='white',relief=tkinter.SUNKEN)
        self.mainLabel.pack(pady=20,ipadx=10,ipady=10)

        self.formFrame=tkinter.Frame(self.root,bg="#A1A5A1",width=self.root.winfo_screenwidth())
        self.formFrame.pack()

        self.lb1 = tkinter.Label(self.formFrame, text='Enter Email', font=('arial', 14),bg='#A1A5A1')
        self.txt1 = tkinter.Entry(self.formFrame, font=('arial', 14))
        self.lb1.grid(row=0, column=0, pady=10, padx=10)
        self.txt1.grid(row=0, column=1, pady=10, padx=10,ipadx=10,ipady=10)
        self.txt1.insert(0, useremail)
        self.txt1.configure(state='readonly')

        self.lb2=tkinter.Label(self.formFrame,text='Enter old password',font=('arial',14),bg='#A1A5A1')
        self.txt2 = tkinter.Entry(self.formFrame,font=('arial',14))
        self.lb2.grid(row=1,column=0,pady=10,padx=10)
        self.txt2.grid(row=1,column=1,pady=10,padx=10,ipadx=10,ipady=10)

        self.lb3 = tkinter.Label(self.formFrame, text='Enter new password', font=('arial', 14),bg='#A1A5A1')
        self.txt3 = tkinter.Entry(self.formFrame, font=('arial', 14))
        self.lb3.grid(row=2, column=0, pady=10, padx=10)
        self.txt3.grid(row=2, column=1, pady=10, padx=10,ipadx=10,ipady=10)

        self.bt1=tkinter.Button(self.root,text='Submit',font=('arial',14),command=self.insertuser,bg='#787D78',foreground='black',activebackground='black',activeforeground="white"
        ,relief=tkinter.SUNKEN)
        self.bt1.pack(pady=10)

        self.root.mainloop()
    def insertuser(self):
        email = self.txt1.get()
        password = self.txt2.get()
        newpassword = self.txt3.get()
        conn = Connect()
        cr = conn.cursor()
        q = f"select * from user where email='{email}' and password='{password}'"
        cr.execute(q)
        result = cr.fetchall()
        if len(result) == 0:
            msg.showwarning("", 'INVALID EMAIL/PASSWORD')
        else:
            q = f"update user set password='{newpassword}'where email='{email}'"
            cr.execute(q)
            conn.commit()
            msg.showinfo('', 'User Password has been Updated', parent=self.root)
            self.root.destroy()


# obj=Main()