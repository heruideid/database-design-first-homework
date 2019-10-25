import pyodbc
from flask import Flask, request, redirect, url_for
from flask import render_template
from flask_bootstrap import Bootstrap


cnxn, crsr= None, None

def run(s):
    crsr.execute(s)
    crsr.commit()


def init():
    global cnxn, crsr 
    cnxn = pyodbc.connect('DSN=mysql64; DRIVER={MySQL ODBC 8.0 Unicode Driver}; SERVER=localhost; DATABASE=; UID=root; PWD=;')
    crsr = cnxn.cursor()
    run("create table  if not exists student(sno text,sname text,sex text,sage text,sdept text)")
    run("create table if not exists  course (cno text,cname text,cpno text,ccredit text)")
    run("create table if not exists sc (sno text,cno text,grade int)")

#Cont一个列表，包含新增的各属性的值
def insert(tableName,Cont):
    sql=None
    if tableName=="student":
        sql="insert into student values (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")"%(Cont[0],Cont[1],Cont[2],Cont[3],Cont[4])
        run(sql)
        return render_template('index.html')
    elif tableName=="course":
        sql="insert into course values (\"%s\",\"%s\",\"%s\",\"%s\")"%(Cont[0],Cont[1],Cont[2],Cont[3])
        run(sql)
        return render_template('index.html')

def delete(tableName,id):
    sql=None
    if tableName=="student":
        sql="delete from student where sno="+id
        run(sql)
        return render_template('index.html')
    elif tableName=="course":
        sql="delete from course where cno="+id
        run(sql)
        return render_template('index.html')

#dic包含要修改的属性与修改值的键值对
#id 是修改那一行的sno或cno
def update(tableName,dic,id):
    prime_key,sql_1=None,""
    for key,value in dic.items():
        if sql_1=="":
            sql_1=sql_1+key+"=\""+value+"\""
        else:
            sql_1=sql_1+","+key+"=\""+value+"\""
    if(tableName=="student"):
        prime_key="sno"
    else:
        prime_key="cno"
    sql="update %s set %s where %s=%s"%(tableName,sql_1,prime_key,id)
    #update student set sdept=
    run(sql)
    return render_template('index.html')

def query(tableName,id):
    prime_key,sql=None,None
    if(tableName=="student"):
        prime_key="sno"
    else:
        prime_key="cno"
    sql="select * from %s where %s=%s"%(tableName,prime_key,id)
    crsr.execute(sql)
    u=crsr.fetchall()
    return render_template('query_%s.html'%(tableName),u=u)

def showall():
    sql_1="select * from student"
    sql_2="select * from course"
    crsr.execute(sql_1)
    u=crsr.fetchall()
    crsr.execute(sql_2)
    v=crsr.fetchall()
    return render_template('showall.html',u=u,v=v)

def close():
    crsr.close();
    cnxn.close();

def end():
    close()
    cnxn, crsr = None, None