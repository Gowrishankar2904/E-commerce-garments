#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python310/python.exe

print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()

form=cgi.FieldStorage()
pid=form.getvalue("id")


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
        .image {
            padding-right: 100px;
            padding-top: 30px;
        }
        body {
            background-color: #f8f9fa;
        }

        .leave-form {
            max-width: 500px;
            margin: 50px auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
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

print("""           
            <div class="col p-4">
                <div class="main col p-4">
                    <center>
                        <h2
                            style="font-family:Georgia, 'Times New Roman', Times, serif; color: #230124;margin-left:20px;">
                            Employee
                            Inventry Request</h2>
                    </center><br>
                    <div class="col-md-4"></div>
                    <form action="" class="container col-md-5" name="image" method="post" enctype="multipart/form-data">
                        <!-- <input type="text"> -->
     """)
print("""
                        <input class="form-control"  type="text" required name="Assetid" placeholder="asset_id"><br>
                """)
print("""
                        <input class="form-control"  type="text" required name="empid" placeholder="emp_id"><br>
                """)
print("""
                        <input class="form-control" type="text" name="name" placeholder="Name of the Asset"
                            maxlength="20" required><br>
                        <select class="form-control dropdown" type="text" name="assetcat" maxlength="20" required>
                            <option value="" disabled selected>Asset Category</option>
                            <option value="computer">Computer</option>
                            <option value="Mouse">Mouse</option>
                            <option value="Keyboard">Keyboard</option>
                        </select><br>
                        <input class="form-control" type="text" name="description" placeholder="Description of Asset"
                            maxlength="20" required><br>
                        <input class="form-control" type="text" name="brand" placeholder="Brand" maxlength="20"
                            required><br>
                        <input class="form-control" type="text" name="model" placeholder="Model" maxlength="20"
                            required><br>
                        <input class="form-control" type="number" name="purchase" placeholder="Quantity Purchased"
                            maxlength="20" required><br>
                        <input class="form-control" type="number" name="price" placeholder="Price" maxlength="20"
                            required><br>
                      <center>
                        <input class="form-cmnmybnjontrol btn btn-info" type="Submit" name="login" value="Submit">
                      </center>
                    </form>
                </div>
            </div>
        </div>
    </div>
</body>

</html>
""")

import pymysql
import cgi, cgitb, os
import smtplib

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="empdb")
cur = conn.cursor()


aid = form.getvalue("Assetid")
eid = form.getvalue("empid")
aname = form.getvalue("name")
acat = form.getvalue("assetcat")
ades = form.getvalue("description")
abrnd = form.getvalue("brand")
amod = form.getvalue("model")
apur = form.getvalue("purchase")
aprce = form.getvalue("price")
sub = form.getvalue("login")

if sub!=None:

        q = """insert into inventry (assid,empid,aname,acategory,adescription,brand,model,qty,price) 
           values('%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (aid, eid, aname, acat, ades, abrnd, amod, apur, aprce)
        cur.execute(q)
        conn.commit()
        print("""
                    <script>
                    alert("Data inserted successfully")
                    </script>
                        """)
conn.close()