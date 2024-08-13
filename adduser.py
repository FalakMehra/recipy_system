import tkinter
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect

class Main:
    def __init__(self):
        self.bgcolour = "#C1C3C1"
        self.root=tkinter.Tk()
        self.root.title('ADD USER')
        self.root.geometry('800x800')
        self.root.configure(bg=self.bgcolour)

        self.mainLabel=tkinter.Label(self.root,text='Add User',font=('',28,'bold'),bg="#6E726E",relief=tkinter.SUNKEN)
        self.mainLabel.pack(pady=20,ipadx=10,ipady=10)

        self.formFrame=tkinter.Frame(self.root,bg="#A1A5A1",width=self.root.winfo_screenwidth())
        self.formFrame.pack()
        self.font=('arial',14)

        self.lb1=tkinter.Label(self.formFrame,text='Enter name',font=self.font,bg='#A1A5A1')
        self.txt1=tkinter.Entry(self.formFrame,font=self.font)
        self.lb1.grid(row=0,column=0,padx=10,pady=10)
        self.txt1.grid(row=0,column=1,padx=10,pady=10,ipadx=10,ipady=10)

        self.lb2=tkinter.Label(self.formFrame, text='Enter email', font=self.font,bg='#A1A5A1')
        self.txt2=tkinter.Entry(self.formFrame, font=self.font)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2.grid(row=1, column=1, padx=10, pady=10,ipadx=10,ipady=10)

        self.lb3=tkinter.Label(self.formFrame, text='Enter mobile', font=self.font,bg='#A1A5A1')
        self.txt3=tkinter.Entry(self.formFrame, font=self.font)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3.grid(row=2, column=1, padx=10, pady=10,ipadx=10,ipady=10)

        self.lb4 = tkinter.Label(self.formFrame, text='Enter password', font=self.font,bg='#A1A5A1')
        self.txt4 = tkinter.Entry(self.formFrame, font=self.font)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4.grid(row=3, column=1, padx=10, pady=10,ipadx=10,ipady=10)

        self.lb5 = tkinter.Label(self.formFrame, text='Enter gender', font=self.font,bg='#A1A5A1')
        self.txt5 = ttk.Combobox(self.formFrame,values=['MALE','FEMALE'],state='readonly',font=self.font)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5.grid(row=4, column=1, padx=10, pady=10,ipadx=10,ipady=10)

        self.lb6=tkinter.Label(self.formFrame, text='Enter address', font=self.font,bg='#A1A5A1')
        self.txt6=tkinter.Entry(self.formFrame, font=self.font)
        self.lb6.grid(row=5, column=0, padx=10, pady=10)
        self.txt6.grid(row=5, column=1, padx=10, pady=10,ipadx=10,ipady=10)

        self.bt1=tkinter.Button(self.root,text='SUBMIT',width=20,font=self.font,command=self.insertUser,bg='#787D78',foreground='black',activebackground='black',activeforeground="white"
        ,relief=tkinter.SUNKEN)
        self.bt1.pack(pady=10)
        self.root.mainloop()

    def insertUser(self):
        name=self.txt1.get()
        email=self.txt2.get()
        mobile=self.txt3.get()
        password=self.txt4.get()
        gender=self.txt5.get()
        address=self.txt6.get()
        if name=='' or email=='' or mobile=='' or password=='' or gender=='' or address=='':
            msg.showwarning('WARNING','PLEASE FILL ALL THE DETAILS')
        else:
            conn = Connect()
            cr = conn.cursor()
            q = f"insert into user values(null,'{name}','{email}','{mobile}','{password}','{gender}','{address}')"
            cr.execute(q)
            conn.commit()
            msg.showinfo("SUCCESS", "USER HAS BEEN ADDED")

# obj=Main()

