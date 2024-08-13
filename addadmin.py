import tkinter
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect
class Main:
    def __init__(self):
        self.bgcolour='#C1C3C1'
        self.root=tkinter.Tk()
        self.root.title('Add title')
        self.root.geometry('600x600')
        self.root.configure(bg=self.bgcolour)

        self.mainLabel=tkinter.Label(self.root,text="Add Admin",font=('arial',28,'bold'),bg='#6E726E',relief=tkinter.SUNKEN)
        self.mainLabel.pack(pady=20,ipadx=10,ipady=10)
        self.formFrame=tkinter.Frame(self.root,bg='#A1A5A1',width=self.root.winfo_screenwidth())
        self.formFrame.pack()
        self.formFrame.pack_propagate(0)

        self.lb1=tkinter.Label(self.formFrame,text='Enter name',font=('arial',14),bg='#A1A5A1')
        self.txt1 = tkinter.Entry(self.formFrame,font=('arial',14))
        self.lb1.grid(row=0,column=0,pady=10,padx=10)
        self.txt1.grid(row=0,column=1,pady=10,padx=10,ipadx=10,ipady=10)

        self.lb2 = tkinter.Label(self.formFrame, text='Enter email', font=('arial', 14),bg='#A1A5A1')
        self.txt2 = tkinter.Entry(self.formFrame, font=('arial', 14))
        self.lb2.grid(row=1, column=0,pady=10,padx=10)
        self.txt2.grid(row=1, column=1,pady=10,padx=10,ipadx=10,ipady=10)

        self.lb3 = tkinter.Label(self.formFrame, text='Enter Mobile', font=('arial', 14),bg='#A1A5A1')
        self.txt3 = tkinter.Entry(self.formFrame, font=('arial', 14))
        self.lb3.grid(row=2, column=0,pady=10,padx=10)
        self.txt3.grid(row=2, column=1,pady=10,padx=10,ipadx=10,ipady=10)

        self.lb4 = tkinter.Label(self.formFrame, text='Enter Password', font=('arial', 14),bg='#A1A5A1')
        self.txt4 = tkinter.Entry(self.formFrame, font=('arial', 14))
        self.lb4.grid(row=3, column=0,pady=10,padx=10)
        self.txt4.grid(row=3, column=1,pady=10,padx=10,ipadx=10,ipady=10)

        self.lb5 = tkinter.Label(self.formFrame, text='Enter Role', font=('arial', 14),bg='#A1A5A1')
        self.txt5 = ttk.Combobox(self.formFrame,values=['Super admin','Admin'],state='readonly', font=('arial', 14))
        self.lb5.grid(row=4, column=0,pady=10,padx=10)
        self.txt5.grid(row=4, column=1,pady=10,padx=10,ipadx=10,ipady=10)

        self.bt1=tkinter.Button(self.root,text='Submit',font=('arial',20,'bold'),bg='#787D78',foreground='black',activebackground='black',activeforeground="white"
        ,relief=tkinter.SUNKEN,command=self.insertadmin)
        self.bt1.pack(pady=10)

        self.root.mainloop()
    def insertadmin(self):
        name = self.txt1.get()
        email = self.txt2.get()
        mobile = self.txt3.get()
        password= self.txt4.get()
        role = self.txt5.get()
        if name=='' or email=='' or mobile=='' or password=='' or role=='':
            msg.showwarning('WARNING','PLEASE FILL ALL THE DETAILS')



        else:
            conn=Connect()
            cr=conn.cursor()
            q=f"insert into admin values(null,'{name}','{email}','{mobile}','{password}','{role}')"
            cr.execute(q)
            conn.commit()
            msg.showinfo("SUCCESS","ADMIN HAS BEEN ADDED")

# obj=Main()