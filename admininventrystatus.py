#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python310/python.exe


print("content-type:text/html \r\n\r\n")
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
        </div>
""")

import pymysql
import cgi, cgitb

cgitb.enable()
conn = pymysql.connect(host="Localhost", user="root", password="", database="empdb")
cur = conn.cursor()

q1 = """select * from inventry where status=" " """
cur.execute(q1)
res = cur.fetchall()

print("""
<html>
<bodY>
<div class="col-md-4"></div>
<div class="col-md-6">
<center>
</center><br>
<table border="4" cellpadding="5" cellspacing="15" style="margin-left:300px;">
<tr>
<th>id</th>
<th>assetid</th>
<th>name</th>
<th>category</th>
<th>description</th>
<th>brand</th>
<th>model</th>
<th>qty</th>
<th>price</th>
<th>status</th>
</tr>""")
for i in res:
    print("""
    <tr>
    <form method="post">
        <td><input type="text" name="leave" value="%s" readonly style='width:100px; border:none;'></td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>
        <input class="btn btn-success" type="submit" name="accept" value="accept"><br><br>
        <input class="btn btn-success" type="submit" name="decline" value="decline">
        </td>
    </form>
    </tr>""" % (i[0], i[1], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))
print("""
</table>
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

paccept = form.getvalue("accept")
pdecline = form.getvalue("decline")
pleave = form.getvalue("leave")
pid = form.getvalue("id")
if paccept != None:
    q = """update inventry set status='Approved' where id='%s'""" % (pleave)
    cur.execute(q)
    conn.commit()

    print("""
    <script>
        alert("update successfully ");
    </script>
    """)
if pdecline != None:
    q = """update inventry set status='Rejected' where id='%s'""" % (pleave)
    cur.execute(q)
    conn.commit()

    print("""
        <script>
            alert("update successfully ");
        </script>
        """)

conn.close()