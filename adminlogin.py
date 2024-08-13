import tkinter
import tkinter.messagebox as msg
import tkinter.ttk as ttk

import admindashboard
from connection import Connect

class Main:
    def __init__(self):
        self.bgcolour = "#C1C3C1"
        self.root=tkinter.Tk()
        self.root.title('LOGIN ADMIN')
        self.root.geometry('800x800')
        self.root.configure(bg=self.bgcolour)

        self.mainLabel=tkinter.Label(self.root,text='Login Admin',font=('',28,'bold'),bg="#6E726E",relief=tkinter.SUNKEN)
        self.mainLabel.pack(pady=20,ipadx=10,ipady=10)

        self.formFrame=tkinter.Frame(self.root,bg="#A1A5A1",width=self.root.winfo_screenwidth())
        self.formFrame.pack()
        self.font=('arial',14)

        self.lb1=tkinter.Label(self.formFrame, text='Enter email', font=self.font,bg='#A1A5A1')
        self.txt1=tkinter.Entry(self.formFrame, font=self.font)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1.grid(row=0, column=1, padx=10, pady=10,ipadx=10,ipady=10)

        self.lb2 = tkinter.Label(self.formFrame, text='Enter password', font=self.font,bg='#A1A5A1')
        self.txt2 = tkinter.Entry(self.formFrame, font=self.font,show='*')
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2.grid(row=1, column=1, padx=10, pady=10,ipadx=10,ipady=10)

        self.bt1=tkinter.Button(self.root,text='LOGIN',width=20,font=self.font,command=self.checkUser,bg='#787D78',foreground='black',activebackground='black',activeforeground="white"
        ,relief=tkinter.SUNKEN)
        self.bt1.pack(pady=10)
        self.root.mainloop()

    def checkUser(self):
        email=self.txt1.get()
        password=self.txt2.get()
        conn=Connect()
        cr=conn.cursor()
        q=f"select * from admin where email='{email}' and password='{password}'"
        cr.execute(q)
        result=cr.fetchall()
        if len(result)==0:
            msg.showwarning("",'INVALID EMAIL/PASSWORD')
        else:
            msg.showinfo("",'LOGIN SUCCESSFUL',parent=self.root)
        id=result[0][0]
        email=result[0][2]
        role=result[0][-1]
        name=result[0][1]
        admindashboard.Main(adminid=id,adminname=name,adminemail=email,adminrole=role)

# obj=Main()