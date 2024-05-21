#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html \r\n\r\n")
import os
import smtplib
import pymysql
import cgi,cgitb

cgitb.enable()
conn=pymysql.connect(host="localhost",user="root",database="empdb")
cur=conn.cursor()

q1="""select max(id) from empdata"""
cur.execute(q1)
r=cur.fetchone()

#print(r)
if r[0]!=None:
    n=r[0]
else:
    n=0

#print(n)

z=""
if n<9:
    z="000"
elif n>=10 and n<=99:
    z="00"
elif n>=100 and n<=999:
    z="0"

form=cgi.FieldStorage()

employee_id="EMP"+z+str(n+1)

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
        crossorigin="anonymous"></script>
<style>
    .na{
       position:fixed;  
    }
    
    .main{
        margin-left:200px;
    }
    
    .side{
    background-color: rgb(45, 41, 46);
    }

</style>
</head>

<body>
    <div class="container-fluid ">
        <div class="row flex-nowrap">
            <div class="col-auto col-md-3 col-xl-2 px-sm-2 px-0 side na">
                <div class="d-flex flex-column align-items-center align-items-sm-start px-3 pt-2 text-white min-vh-100">
                    <a href="/"
                        class="d-flex align-items-center pb-3 mb-md-0 me-md-auto text-white text-decoration-none">
                        <span class="fs-5 d-none d-sm-inline"></span>
                    </a>
                    <ul class="nav nav-pills flex-column mb-sm-auto mb-0 align-items-center align-items-sm-start"
                        id="menu">
                        <li class="nav-item">
                            <a href="./admin dashboard.py" class="nav-link align-middle px-0">
                                <i class="fs-4 bi-house"></i> <span class="ms-1 d-none d-sm-inline">DASHBOARD</span>
                            </a>
                        </li>
                        <li>
                            <a href="#submenu2" data-bs-toggle="collapse" class="nav-link px-0 align-middle ">
                                <i class="fs-4 bi-bootstrap"></i> <span
                                    class="ms-1 d-none d-sm-inline">EMPLOYEE DETAILS </span></a>
                            <ul class="collapse nav flex-column ms-1" id="submenu2" data-bs-parent="#menu">
                                <li class="w-100">
                                    <a href="./adminempaddform.py" class="nav-link px-0"> <span class="d-none d-sm-inline">NEW</span>
                                        </a>
                                </li>
                                <li>
                                    <a href="./adminempdataview.py" class="nav-link px-0"> <span class="d-none d-sm-inline">VIEW</span>
                                        </a>
                                </li>
                            </ul>
                        </li>
                        <li>
                            <a href="./admininventrystatus.py" class="nav-link px-0 align-middle">
                                <i class="fs-4 bi-table"></i> <span class="ms-1 d-none d-sm-inline">INVENTRY & ASSET</span></a>
                        </li>
                        <li>
                            <a href="#submenu3" data-bs-toggle="collapse" class="nav-link px-0 align-middle">
                                <i class="fs-4 bi-grid"></i> <span class="ms-1 d-none d-sm-inline">LEAVE REQUEST</span> </a>
                            <ul class="collapse nav flex-column ms-1" id="submenu3" data-bs-parent="#menu">
                                <li class="w-100">
                                    <a href="./adminleavedataview.py" class="nav-link px-0"> <span class="d-none d-sm-inline">NEW</span>
                                        </a>
                                </li>
                                <li>
                                    <a href="./adminleavedatatable.py" class="nav-link px-0"> <span class="d-none d-sm-inline">EXIST</span>
                                        </a>
                                </li>
                            </ul>
                        </li>
                        <li>
                            <a href="./salary.py" class="nav-link px-0 align-middle">
                                <i class="fs-4 bi-people"></i> <span class="ms-1 d-none d-sm-inline">SALARY CALCULATION</span>
                            </a>
                        </li>
                    </ul>
                    <hr>
                    <div class="dropdown pb-4">
                        <a href="#" class="d-flex align-items-center text-white text-decoration-none dropdown-toggle"
                            id="dropdownUser1" data-bs-toggle="dropdown" aria-expanded="false">
                            <img src="./image/WhatsApp Image 2023-12-07 at 11.22.08 AM.jpeg" alt="hugenerd" width="30" height="30"
                                class="rounded-circle">
                            <span class="d-none d-sm-inline mx-1">MORE</span>
                        </a>
                        <ul class="dropdown-menu dropdown-menu-dark text-small shadow">

                            <li>
                                <hr class="dropdown-divider">
                            </li>
                            <li><a class="dropdown-item" href="./home.py">Sign out</a></li>
                        </ul>
                    </div>
                </div>
            </div>
""")
print("""
 <div class="col py-3">
    <div class="main">
        <center>
            <h2 style="font-family:Georgia, 'Times New Roman', Times, serif; color: #230124;margin-left:20px;">Employee
                registration form</h2>
        </center><br>
        <div class="col-md-4"></div>
        <form action="" class="container col-md-5" name="image" method="post" enctype="multipart/form-data">
            <!-- <input type="text"> -->
            """)
print("""    
            <input class="form-control type="text" readonly value="%s" required name="emp"><br>
          """ %employee_id)
print("""
            <input class="form-control" type="text" name="name" placeholder="Name" maxlength="20" required><br>
            <input class="form-control" type="date" name="dob" placeholder="Dob" maxlength="20" required><br>
            <input class="form-control" type="text" name="role" placeholder="Role" maxlength="20" required><br>
            <input class="form-control" type="text" name="phone" placeholder="contact no" maxlength="20" required><br>
            <input class="form-control" type="mail" name="mail" placeholder="Email_id" maxlength="300" required><br>
            <input class="form-control" type="text" name="address" placeholder="Address" maxlength="100"><br>
            <select class="form-control" type="text" name="city" maxlength="20" required>
                <option value="" disabled selected>Select city</option>
                <option value="coimbatore">Coimbatore</option>
                <option value="kochin">Kochin</option>
                <select>
                    <br>
                    <select class="form-control" type="text" name="state" maxlength="20" required>
                        <option value="" disabled selected>Select state</option>
                        <option value="Tamilnadu">Tamilnadu</option>
                        <option value="kerala">Kerala</option>
                        <select>
                            <br>
                            <select class="form-control" type="text" name="type" maxlength="20" required>
                                <option value="" disabled selected>Select Employeement type</option>
                                <option value="fulltime">Fulltime</option>
                                <option value="parttime">Parttime</option>
                                <select>
                                    <br>
                                    <input class="form-control" type="text" name="uname" placeholder="Username"
                                        maxlength="20" required><br>
                                    <input class="form-control" type="text" name="pwd" placeholder="Password"
                                        maxlength="20" required><br>
                                    <input class="form-control" type="number" name="num" placeholder="Salary"
                                        maxlength="20" required><br>
                                    <input class="form-control" type="file" name="image"
                                        placeholder="Upload Profile Picture" maxlength="20" required>
                                    <br>
                                    <input class="form-cmnmybnjontrol btn btn-info" type="Submit" name="login"
                                        value="login"><br><br><br>
                               </select>
                            </select>
                        </select>
                    </select>
                </select>
            </select>                                
        </form>
 </div>
</body>

</html>
""")


pname = form.getvalue("name")
pdob=form.getvalue("dob")
prole=form.getvalue("role")
pcontact=form.getvalue("phone")
pemail_id=form.getvalue("mail")
paddr=form.getvalue("address")
pcity=form.getvalue("city")
pstate=form.getvalue("state")
pemployee_type=form.getvalue("type")
puserna = form.getvalue("uname")
ppass = form.getvalue("pwd")
psalary=form.getvalue("num")
pemployee_id= form.getvalue("emp")

if len(form) != 0:
    pimage = form['image']
    if pimage.filename:
        fn = os.path.basename(pimage.filename)
        open("storage/" + fn, "wb").write(pimage.file.read())
        q = """insert into empdata (emp_id,name,dob,role,contact,emailid,address,city,state,type,username,password,salary,image)
         values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (pemployee_id,pname,pdob,prole,pcontact,pemail_id,paddr,pcity,pstate,pemployee_type,puserna,ppass,psalary,fn)
        cur.execute(q)
        conn.commit()
        print("""
            <script>
            alert("Data inserted successfully")
            </script>
            """)

        fromaddr="abimanyuravichandran07@gmail.com"
        password="zpnsziumpfacvvoz"
        toaddr= pemail_id
        subject='Hi,welcome'
        body=""" Username: '%s' \nPassword: '%s' """%(puserna,ppass)
        msg=""" Subject:{} \n\n {}""".format(subject,body)
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login(fromaddr,password)
        server.sendmail(fromaddr,toaddr,msg)
        server.quit()

conn.close()
