#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()

form = cgi.FieldStorage()
pid = form.getvalue("id")

print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Employee Leave Form</title>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
   <style>
    .leave-form {
      max-width: 400px;
      margin: 50px auto;
      padding: 30px;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    .btn-submit {
      background-color: #dc3545;
      color: #ffffff;
      transition: background-color 0.3s ease;
    }

    .btn-submit:hover {
      background-color: #bd2130;
    }
    .na{
       position:fixed;  
    }
    
    .main{
        margin-left:200px;
    }
   </style>
    <script>
        function calculateDays() {
            const startDate = new Date(document.getElementById('start-date').value);
            const endDate = new Date(document.getElementById('end-date').value);
            const resultTextBox = document.getElementById('result');

            if (startDate && endDate) {
                const difference = Math.abs(endDate - startDate);
                const daysDifference = Math.ceil(difference / (1000 * 60 * 60 * 24));
                resultTextBox.value = daysDifference;
            } else {
                resultTextBox.value = '';
            }
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
             """)
print("""
                            <a href="./empdashboard.py?id=%s" class="nav-link align-middle px-0">
                                <i class="fs-4 bi-house"></i> <span class="ms-1 d-none d-sm-inline">DASHBOARD</span>
                            </a>
             """% (pid))
print("""
                        </li>
                        <li>
                            <a href="#submenu2" data-bs-toggle="collapse" class="nav-link px-0 align-middle ">
                                <i class="fs-4 bi-bootstrap"></i> <span
                                    class="ms-1 d-none d-sm-inline">INVENTRY & ASSET</span></a>
                            <ul class="collapse nav flex-column ms-1" id="submenu2" data-bs-parent="#menu">
                                <li class="w-100">
             """)
print("""
                                    <a href="./empinventryform.py?id=%s" class="nav-link px-0"> <span class="d-none d-sm-inline">NEW</span>
             """% (pid))
print("""
                                        </a>
                                </li>
                                <li>
             """)
print("""
                                    <a href="./empinventrytableview.py?id=%s" class="nav-link px-0"> <span class="d-none d-sm-inline">VIEW</span>
             """% (pid))
print("""
                                        </a>
                                </li>
                            </ul>
                        </li>
                        <li>
                            <a href="#submenu3" data-bs-toggle="collapse" class="nav-link px-0 align-middle">
                                <i class="fs-4 bi-grid"></i> <span class="ms-1 d-none d-sm-inline">LEAVE REQUEST</span> </a>
                            <ul class="collapse nav flex-column ms-1" id="submenu3" data-bs-parent="#menu">
                                <li class="w-100">
             """)
print("""
                                    <a href="./empleaveform.py?id=%s" class="nav-link px-0"> <span class="d-none d-sm-inline">NEW</span>
             """% (pid))
print("""
                                        </a>
                                </li>
                                <li>
             """)
print("""
                                    <a href="./empleavedataview.py?id=%s" class="nav-link px-0"> <span class="d-none d-sm-inline">EXIST</span>
             """% (pid))
print("""
                                        </a>
                                </li>
                            </ul>
                        </li>
                        <li>
             """)
print("""
                            <a href="./empsalarytableview.py?id=%s" class="nav-link px-0 align-middle">
                                <i class="fs-4 bi-people"></i> <span class="ms-1 d-none d-sm-inline">SALARY </span>
             """% (pid))
print("""
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
             """)
print("""
                            <li><a class="dropdown-item" href="./empprofile.py?id=%s">Profile</a></li>
             """% (pid))
print("""
                            <li>
                                <hr class="dropdown-divider">
                            </li>
                            <li><a class="dropdown-item" href="./home.py?id=%s">Sign out</a></li>
             """% (pid))
print("""
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
""")

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="empdb")
cur = conn.cursor()

q = """select * from empdata where id="%s" """ % (pid)
cur.execute(q)
res = cur.fetchall()

for i in res:
    Emp = i[1]
    name = i[2]

print("""
    <div class="container">
      <div class="leave-form">
        <h2> Leave Request Form</h2>
        <form name="loginform" onsubmit="return login()" onchange="remdays();">
          <div class="form-group">
            <label for="employeeName">Employee id</label>
""")
print("""
            <input type="text" class="form-control" id="employeeName" name="empid" placeholder="Enter your id">
""")
print("""
          </div>

          <div class="form-group">
            <label for="employeeName">Employee Name</label>
            """)
print("""
            <input type="text" class="form-control" id="employeeid" name="ename" placeholder="Enter your name">
         """)
print("""
          </div>

          <div class="form-group">
            <label for="leaveType">Leave Type</label>
            <select class="form-control" id="leaveType" name="type">
              <option>select</option>
              <option>Vacation</option>
              <option>Sick Leave</option>
              <option>Personal Leave</option>
            </select>
          </div>

                <div class="form-group">
                    <label for="startDate">Start Date</label>
                    <input type="date" class="form-control" id="start-date" name="from" oninput="calculateDays()" >
                </div>

          <div class="form-group">
            <label for="endDate">End Date</label>
            <input type="date" class="form-control" id="end-date" name="to" oninput="calculateDays()">
          </div>

          <div class="form-group">
            <label for="reason">No.of.Days</label>
            <input type="text" class="form-control" id="result" rows="3" placeholder="No.of.Days" name="days"></textarea>
          </div>            
          <input type="submit" class="form-control btn btn-submit btn-block" name="login" value="APPLY" >
        </form>
      </div>
   </div>

</body>

</html>
""")

import pymysql
import cgi, cgitb

cgitb.enable()
conn = pymysql.connect(host="Localhost", user="root", password="", database="empdb")
cur = conn.cursor()

form = cgi.FieldStorage()
pempid = form.getvalue("empid")
pname = form.getvalue("ename")
pleave = form.getvalue("type")
pstart = form.getvalue("from")
pend = form.getvalue("to")
preas = form.getvalue("days")
psubmit = form.getvalue("login")

if psubmit != None:
    q = """insert into leave_data (emp_id,name,type,start_date,end_date,leave_taken)
        values('%s','%s','%s','%s','%s','%s')""" % (pempid, pname, pleave, pstart, pend, preas)
    cur.execute(q)
    conn.commit()
    print("""
           <script>
           alert("Data inserted successfully")
           </script>
           """)
conn.close()
