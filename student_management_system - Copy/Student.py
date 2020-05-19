from tkinter import *
import tkinter.messagebox
import student_database
class Student:
    def __init__(self,root):
         self.root=root
         self.root.title("Student Management system")
         self.root.geometry("900x500+0+0")
         self.root.config(bg="powderblue")

         id=StringVar()
         firstname = StringVar()
         surname = StringVar()
         age = StringVar()
         gender = StringVar()
         mobile = StringVar()
         department = StringVar()
         level = StringVar()
         agno = StringVar()
         scholarship_state = StringVar()
        #-----------------------------------------------------#
         def cancel():

             cancel=tkinter.messagebox.askyesno("Students database management systems","confirm if you want cancel")
             if cancel > 0:
              root.destroy()
             return
         def clearall():
              self.txtid.delete(0,END)# si on ecrit 0 sans end il efface lettre par lettre
              self.txtfname.delete(0,END)
              self.txtlname.delete(0,END)
              self.txtage.delete(0,END)
              self.txtgender.delete(0,END)
              self.txtmobile.delete(0,END)
              self.txtdepartment.delete(0, END)
              self.txtlevel.delete(0, END)
              self.txtagno.delete(0, END)
              self.txtscholarship.delete(0, END)
         def addstudent():
              if(len(id.get())!=0):
                   student_database.addStudent(id.get(),firstname.get(),surname.get(),age.get(),gender.get(),mobile.get(),department.get(),level.get(),agno.get(),scholarship_state.get())
                   studentlist.delete(0,END)
                   studentlist.insert(END,id.get(),firstname.get(),surname.get(),age.get(),gender.get(),mobile.get(),department.get(),level.get(),agno.get(),scholarship_state.get())
         def display():
              studentlist.delete(0,END)
              for row in student_database.showall():
                   studentlist.insert(END,row,str(" "))
         def studentregister(event):
              global t
              searchstudent=studentlist.curselection()[0]
              t=studentlist.set(searchstudent)
              self.txtid.delete(0,END)  # si on ecrit 0 sans end il efface lettre par lettre
              self.txtid.insert(END,t[1])
              self.txtfname.delete(0,END)
              self.txtfname.insert(END, t[2])
              self.txtlname.delete(0, END)
              self.txtlname.insert(END, t[3])
              self.txtage.delete(0, END)
              self.txtage.insert(END, t[4])
              self.txtgender.delete(0, END)
              self.txtgender.insert(END, t[5])
              self.txtmobile.delete(0, END)
              self.txtmobile.insert(END, t[6])
              self.txtdepartment.delete(0, END)
              self.txtdepartment.insert(END, t[7])
              self.txtlevel.delete(0, END)
              self.txtlevel.insert(END, t[8])
              self.txtagno.delete(0, END)
              self.txtagno.insert(END, t[9])
              self.txtscholarship.delete(0, END)
              self.txtscholarship.insert(END, t[10])


         def delete():
              if (len(id.get()) != 0):
                   student_database.deleteStudent(t[0])
                   clearall()
                   display()
         def searchdatabase():
              studentlist.delete(0,END)
              for row in student_database.search(id.get(),firstname.get(),surname.get(),age.get(),gender.get(),mobile.get(),department.get(),level.get(),agno.get(),scholarship_state.get()):
                   studentlist.insert(END, row, str(""))
         def update():
              if (len(id.get()) != 0):
                   student_database.deleteStudent(t[0])
              if (len(id.get()) != 0):
                   student_database.addStudent(id.get(),firstname.get(),surname.get(),age.get(),gender.get(),mobile.get(),department.get(),level.get(),agno.get(),scholarship_state.get())
                   studentlist.delete(0,END)
                   studentlist.insert(END,(id.get(),firstname.get(),surname.get(),age.get(),gender.get(),mobile.get(),department.get(),level.get(),agno.get(),scholarship_state.get()))











        #----------------pour les frames blanc----------------------#
         MainFrame = Frame(self.root, bg="powderblue")
         MainFrame.grid()
         #margin yukarda aşağida =pady
         #margin sağ sol=padx
         TitFrame = Frame(MainFrame, padx=220, pady=10, bg="powderblue",relief=RAISED)#, relief=RIDGE
         TitFrame.pack(side=TOP)
         self.lblTit=Label(TitFrame,font=('arial',20,'bold'),text="Student Management system",bg="powderblue")
         self.lblTit.grid()

         TitFrame1 = Frame(MainFrame,bd=2,width=700, height=70, padx=3, pady=3, bg="Ghost white",relief=RIDGE)  #
         TitFrame1.pack(side=BOTTOM)

         TitFrame11 = Frame(MainFrame, bd=1, width=700, height=400, padx=20, pady=20,relief=RIDGE, bg="powderblue")  # , relief=RIDGE
         TitFrame11.pack(side=BOTTOM)

         TitFrame2 = LabelFrame(TitFrame11,bd=1, width=500, height=300, padx=10, pady=10, bg="Ghost white",font=('arial',12,'bold'),text="Students",relief=RAISED)
         TitFrame2.pack(side=LEFT)

         TitFrame3 = LabelFrame(TitFrame11,bd=1,width=200, height=68, padx=10, pady=10, bg="Ghost white",font=('arial',12,'bold'),text="Students detail",relief=RAISED)
         TitFrame3.pack(side=RIGHT)

        #-----------------------pour labels et entree----------------------------#
         self.lblid = Label(TitFrame2, font=('arial', 10, 'bold'), text="Student id:",padx=2, pady=2, bg="Ghost white")
         self.lblid.grid(row=0,column=0,sticky=W)
         self.txtid = Entry(TitFrame2, font=('arial', 10, 'bold'),textvariable=id,width=39)
         self.txtid.grid(row=0, column=1, sticky=W)

         self.lblfname = Label(TitFrame2, font=('arial', 10, 'bold'), text="First name:", padx=2, pady=2, bg="Ghost white")
         self.lblfname.grid(row=1, column=0, sticky=W)
         self.txtfname = Entry(TitFrame2, font=('arial', 10, 'bold'), textvariable=firstname, width=39)
         self.txtfname.grid(row=1, column=1, sticky=W)

         self.lbllname = Label(TitFrame2, font=('arial', 10, 'bold'), text="surname:", padx=2, pady=2,bg="Ghost white")
         self.lbllname.grid(row=2, column=0, sticky=W)
         self.txtlname = Entry(TitFrame2, font=('arial', 10, 'bold'), textvariable=surname, width=39)
         self.txtlname.grid(row=2, column=1, sticky=W)

         self.lblage = Label(TitFrame2, font=('arial', 10, 'bold'), text="age:", padx=2, pady=2,bg="Ghost white")
         self.lblage.grid(row=3, column=0, sticky=W)
         self.txtage = Entry(TitFrame2, font=('arial', 10, 'bold'), textvariable=age, width=39)
         self.txtage.grid(row=3, column=1, sticky=W)

         self.lblgender = Label(TitFrame2, font=('arial', 10, 'bold'), text="gender:", padx=2, pady=2, bg="Ghost white")
         self.lblgender.grid(row=4, column=0, sticky=W)
         self.txtgender = Entry(TitFrame2, font=('arial', 10, 'bold'), textvariable=gender, width=39)
         self.txtgender.grid(row=4, column=1, sticky=W)

         self.lblmobile = Label(TitFrame2, font=('arial', 10, 'bold'), text="mobile:", padx=2, pady=2, bg="Ghost white")
         self.lblmobile.grid(row=5, column=0, sticky=W)
         self.txtmobile = Entry(TitFrame2, font=('arial', 10, 'bold'), textvariable=mobile, width=39)
         self.txtmobile.grid(row=5, column=1, sticky=W)

         self.lbldepartment = Label(TitFrame2, font=('arial', 10, 'bold'), text="department:", padx=2, pady=2,bg="Ghost white")
         self.lbldepartment.grid(row=6, column=0, sticky=W)
         self.txtdepartment = Entry(TitFrame2, font=('arial', 10, 'bold'), textvariable=department, width=39)
         self.txtdepartment.grid(row=6, column=1, sticky=W)

         self.lbllevel = Label(TitFrame2, font=('arial', 10, 'bold'), text="level:", padx=2, pady=2,bg="Ghost white")
         self.lbllevel.grid(row=7, column=0, sticky=W)
         self.txtlevel = Entry(TitFrame2, font=('arial', 10, 'bold'), textvariable=level, width=39)
         self.txtlevel.grid(row=7, column=1, sticky=W)

         self.lblagno = Label(TitFrame2, font=('arial', 10, 'bold'), text="agno:", padx=2, pady=2,bg="Ghost white")
         self.lblagno.grid(row=8, column=0, sticky=W)
         self.txtagno = Entry(TitFrame2, font=('arial', 10, 'bold'), textvariable=agno, width=39)
         self.txtagno.grid(row=8, column=1, sticky=W)

         self.lblscholarship = Label(TitFrame2, font=('arial', 10, 'bold'), text="scholarship state:", padx=2, pady=2,bg="Ghost white")
         self.lblscholarship.grid(row=9, column=0, sticky=W)
         self.txtscholarship = Entry(TitFrame2, font=('arial', 10, 'bold'), textvariable=scholarship_state, width=39)
         self.txtscholarship.grid(row=9, column=1, sticky=W)
        #-------------------list-------------------------#
         scrollbar=Scrollbar(TitFrame3)
         scrollbar.grid(row=0, column=1, sticky='ns')
         studentlist=Listbox(TitFrame3,width=40,height=13,font=('arial', 10, 'bold'),yscrollcommand=scrollbar.set)
         studentlist.bind('<<ListboxSelect>>',studentregister)
         studentlist.grid(row=0, column=0, padx=6,pady=6)
         scrollbar.config(command=studentlist.yview)
        #----------------------------------------------------#
         self.btnadd=Button(TitFrame1,text="Add student",font=('arial', 10, 'bold'),height=1,width=10,bd=1,command=addstudent)
         self.btnadd.grid(row=0, column=1)

         self.btnadd = Button(TitFrame1, text="Update", font=('arial', 10, 'bold'), height=1, width=10, bd=1,command=update)
         self.btnadd.grid(row=0, column=2)

         self.btnadd = Button(TitFrame1, text="Search", font=('arial', 10, 'bold'), height=1, width=10, bd=1)
         self.btnadd.grid(row=0, column=3)

         self.btnadd = Button(TitFrame1, text="Clear", font=('arial', 10, 'bold'), height=1, width=10, bd=1,command=clearall)
         self.btnadd.grid(row=0, column=4)

         self.btnadd = Button(TitFrame1, text="Display", font=('arial', 10, 'bold'), height=1, width=10, bd=1)
         self.btnadd.grid(row=0, column=5)

         self.btnadd = Button(TitFrame1, text="delete", font=('arial', 10, 'bold'), height=1, width=10, bd=1,command=delete)
         self.btnadd.grid(row=0, column=6)

         self.btnadd = Button(TitFrame1, text="Cancel", font=('arial', 10, 'bold'), height=1, width=10, bd=1,command=cancel)
         self.btnadd.grid(row=0, column=7)


        #-----------------------------------------------------#
if __name__=='__main__':
    root=Tk()
    application=Student(root)
    root.mainloop()

