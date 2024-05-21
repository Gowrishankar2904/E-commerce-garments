#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python310/python.exe

print("content-type:text/html \r\n\r\n")

import pymysql
import cgi, cgitb
from datetime import date

today = date.today()
year = today.year

form = cgi.FieldStorage()

pid = form.getvalue("id")

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

</style>
    
    <script type="text/javascript">
     function calc(){
     var ch=loginform.mon.selectedIndex;
     if(ch==0)
        loginform.wdays.value="31";
        if(ch==1)
        loginform.wdays.value="28";
        if(ch==2)
        loginform.wdays.value="31";
        if(ch==3)
        loginform.wdays.value="30";
        if(ch==4)
        loginform.wdays.value="31";
        if(ch==5)
        loginform.wdays.value="30";
        if(ch==6)
        loginform.wdays.value="31";
        if(ch==7)
        loginform.wdays.value="31";
        if(ch==8)
        loginform.wdays.value="30";
        if(ch==9)
        loginform.wdays.value="31";
        if(ch==10)
        loginform.wdays.value="30";
        if(ch==11)
        loginform.wdays.value="31";
    }
    function remdays(){
    var wdays=parseInt(loginform.wdays.value);
    var ldays=parseInt(loginform.pleave_taken.value);
    var perdays=wdays-ldays;
    loginform.pdays.value=perdays;    
    }

    function gross(){
    var sal=parseInt(loginform.salary.value);
    var present=parseInt(loginform.pdays.value);
    var work=parseInt(loginform.wdays.value);
    var gross=Math.round((sal * present)/work);
    loginform.grosssalary.value=gross;    
    }
</script>
</head>

<body>
    <div class="container-fluid">
        <div class="row flex-nowrap">
            <div class="col-auto col-md-3 col-xl-2 px-sm-2 px-0 bg-dark na">
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
</body>

</html>
      """)

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="empdb")
cur = conn.cursor()

q = """select * from empdata where id="%s" """ % (pid)
cur.execute(q)
res = cur.fetchall()

for i in res:
    salary = i[13]
    Emp = i[1]
    name = i[2]

    print("""
<div style="margin-left:410px;width:700px;" class="na">
        <form style="margin-top:0px;" name="loginform" onsubmit="return login()">
<div>
            <div class="col-md-5 mar1">
                <span onclick="document.getElementById('more').style.display='none'">
                <center>
                <h4 class="text-center heading">Salary Details</h4>
                </center>
            </div>
        
        <!-- model -->
        <div class="col-md-5"></div>
        <div clss="col-md-4 mar" style="padding:5px;">
            <div class="input-container">
      <input class="form-control type="text" name="emp" value="%s" readonly maxlength="20" required><br>
      """ % (Emp))
    print("""
      <input class="form-control type="date" name="year" value="%s" readonly maxlength="20" required><br>
      """ % (year))
    print("""
        <select class="form-control" type="text" name="mon" maxlength="20" onchange="calc();remdays();gross();" required><br>
        <option value="select month">select month</option>
        <option value="Jan">Jan</option>
        <option value="Feb">Feb</option>
        <option value="March">March</option>
        <option value="April">April</option>
        <option value="May">May</option>
        <option value="June">June</option>
        <option value="July">July</option>
        <option value="Aug">Aug</option>
        <option value="Sep">Sep</option>
        <option value="Oct">Oct</option>
        <option value="Nov">Nov</option>
        <option value="Dec">Dec</option>
        </select><br>
    """)

    print("""
    <input class="form-control" type="text" value="%s" name="salary" readonly placeholder="Salary" maxlength="20" required><br>
    """ % (salary))
    print("""
    <input class="form-control" type="text" name="wdays"   placeholder="Working days" maxlength="20" required><br>
    <input class="form-control" type="text" name="pdays"  placeholder="Present days" maxlength="20" required><br>
    """)

    q1 = """select * from leave_data where emp_id="%s" """ % (Emp)
    cur.execute(q1)
    r = cur.fetchall()

    for i in r:
        print("""
            <input class="form-control" type="text" readonly name="pleave_taken" value="%s" placeholder="Leave taken" maxlength="20" required><br>
        """ % i[6])
        print("""
                <input class="form-control" type="text" name="grosssalary"  placeholder="Gross Salary" maxlength="20" required><br>
                <input class="form-control btn btn-info" type="Submit" name="login" value="submit"><br><br><br>
        </form>
        """)
        print("""
</table>
</div>
<body>
</html>
        """)

import pymysql
import cgi, cgitb

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", database="empdb")
cur = conn.cursor()

q1 = """select * from salary_data"""
cur.execute(q1)
r = cur.fetchall()

form = cgi.FieldStorage()

pemailid = form.getvalue("emp")
pyear = form.getvalue("year")
pmonth = form.getvalue("mon")
psalary = form.getvalue("salary")
pwdays = form.getvalue("wdays")
ppdays = form.getvalue("pdays")
pleave = form.getvalue("pleave_taken")
pgross_salary = form.getvalue("grosssalary")
psubmit = form.getvalue("login")
if psubmit != None:
    q = """insert into salary_data(emp_id,year,month,salary,wdays,pdays,leave_taken,gross_salary) 
    values('%s','%s','%s','%s','%s','%s','%s','%s')""" % (
    pemailid, pyear, pmonth, psalary, pwdays, ppdays, pleave, pgross_salary)
    cur.execute(q)
    print("""
        <script>
            alter("Data inserted successfully")
        </script>
    """)

conn.commit()
conn.close()
