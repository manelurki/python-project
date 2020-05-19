import sqlite3

def StudentData():

    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY,id text,firstname text,surname text,age text,gender text,mobile text,department text,level text,agno text,scholarship_state text)")
    con.commit()
    con.close()
def addStudent(id,firstname,surname,age,gender,mobile,department,level,agno,scholarship_state):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (Null,?,?,?,?,?,?,?,?,?)",(id,firstname,surname,age,gender,department,level,agno,scholarship_state))
    con.commit()
    con.close()
def showall():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    row=cur.fetchall()
    con.close()
    return row
def deleteStudent(id):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE * FROM student")
    row = cur.fetchall()
    con.close()
    #-----------------------#

def search(id="",firstname="",surname="",age="",gender="",mobile="",department="",level="",agno="",scholarship_state=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE id=? OR firstname=? OR surname=? OR age=? OR gender=? OR mobile=? OR department=? OR level=? OR agno=? OR scholarship_state=?",(id,firstname,surname,age,gender,mobile,department,level,agno,scholarship_state))
    row = cur.fetchall()
    con.close()
    return row
def update(id1,id="",firstname="",surname="",age="",gender="",mobile="",department="",level="",agno="",scholarship_state=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET id=?,firstname=?,surname=?,age=?,gender=?,mobile=?,department=?,level=?,agno=?,scholarship_state=?,WHERE id1=?",(id,firstname,surname,age,gender,mobile,department,level,agno,scholarship_state,id1))
    con.commit()
    con.close()

StudentData()