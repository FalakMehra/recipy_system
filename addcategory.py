import tkinter
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect

class Main:
    def __init__(self):
        self.bgcolour = "#C1C3C1"
        self.root=tkinter.Tk()
        self.root.title('ADD CATEGORY')
        self.root.geometry('800x800')
        self.root.configure(bg=self.bgcolour)

        self.mainLabel=tkinter.Label(self.root,text='Add Category',font=('',28,'bold'),bg="#6E726E",relief=tkinter.SUNKEN)
        self.mainLabel.pack(pady=20,ipadx=10,ipady=10)

        self.formFrame=tkinter.Frame(self.root,bg="#A1A5A1",width=self.root.winfo_screenwidth())
        self.formFrame.pack()
        self.font=('arial',20)

        self.lb1=tkinter.Label(self.formFrame,text='Enter name',font=self.font,bg="#A1A5A1",foreground="black")
        self.txt1=tkinter.Entry(self.formFrame,font=self.font)
        self.lb1.grid(row=0,column=0,padx=10,pady=10)
        self.txt1.grid(row=0,column=1,padx=10,pady=10,ipadx=10,ipady=10)

        self.lb2=tkinter.Label(self.formFrame, text='Enter description', font=self.font,bg="#A1A5A1",foreground="black")
        self.txt2=tkinter.Entry(self.formFrame, font=self.font)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2.grid(row=1, column=1, padx=10, pady=10,ipadx=10,ipady=10)

        self.bt1=tkinter.Button(self.root,text='SUBMIT',width=20,font=('',18,'bold'),command=self.insertCategory,bg="#787D78",foreground="black",activebackground="black",activeforeground="white")
        self.bt1.pack(pady=10)
        self.root.mainloop()

    def insertCategory(self):
        name=self.txt1.get()
        description=self.txt2.get()

        if name=='' or description=='':
            msg.showwarning('WARNING','PLEASE FILL ALL THE DEATAILS')
        else:
            conn=Connect()
            cr=conn.cursor()
            q=f"insert into category values ('{name}','{description}')"
            cr.execute(q)
            conn.commit()
            msg.showinfo('SUCCESS','CATEGORY HAS BEEN ADDED')
# obj=Main()