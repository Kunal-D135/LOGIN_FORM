from django.shortcuts import render, HttpResponse
import mysql.connector as c

# Create your views here.
def student(req):
    return render(req,"student.html")

def indata(req):
    rollno=req.GET['rollno'];   
    name=req.GET['name'];
    clas=req.GET['clas'];  
    mob=req.GET['mob'];  
    address=req.GET['address'];  
    conn=c.connect(host="localhost",user="root", passwd="12345",database='db')
    cur=conn.cursor()
    query="insert into student1(rollno,name,clas,mob,address)values({},'{}','{}','{}','{}')".format(rollno,name,clas,mob,address)   
    cur.execute(query)
    conn.commit()
    return HttpResponse("SUCESSFULLY DATA SAVED IN DATABASE")
    
def view(req):
    conn=c.connect(host="localhost",user="root", passwd="12345",database='db')
    cur=conn.cursor()
    query="select * from student1";
    cur.execute(query)
    res=cur.fetchall()
    return render(req,"show.html",{'data':res})