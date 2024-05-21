#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python310/python.exe

print("content-type:text/html \r\n\r\n")

import pymysql,os
import cgi,cgitb

cgitb.enable()
conn=pymysql.connect(host="localhost",user="root",password="",database="empdb")
cur = conn.cursor()

form = cgi.FieldStorage()

pid=form.getvalue("id")

q="""select * from empdata where id="%s" """ % (pid)
cur.execute(q)
res=cur.fetchall()

for i in res:
    fn="storage/"+ i[14]

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

# form = cgi.FieldStorage()

pid = form.getvalue("id")

q = """select * from empdata where id="%s" """ % (pid)
cur.execute(q)
rec = cur.fetchall()

for i in rec:
    fn = "storage/" + i[14]

    print("""
        <center>
        <p>Welcome %s</p>
        <img src="%s" height=160 width=160><br><br>
        </center>
        """ % (i[2], fn))

    print("""
       <html>
<body>
<center>

</center>
    """)
for i in rec:
    print("""
    <center>
       <p>%s</p>
       <p>%s</p><br>
       <div class="col-md-5"></div>
        <form class="container col-md-2"  name="profile_img" method="post" enctype="multipart/form-data">
        <input class="form-control" type="file" name="imgs" placeholder="Update Profile" maxlenghth="20" required><br>
        <input class="form-control btn btn-info" type="Submit" name="Apply" value="update" maxlength="10"><br><br><br>
         </form>
       </center>
       """ % (i[1], i[2]))

print("""

</div>
</body>
</html>
""")

# form=cgi.FieldStorage()
psubmit = form.getvalue("Apply")

if psubmit!=None:

    if len(form) != 0:

        # print(pid)

        pimage = form['imgs']

        if pimage.filename:
            fs = os.path.basename(pimage.filename)
            open("storage/" + fs, "wb").write(pimage.file.read())
            q = """update empdata set image='%s' where id="%s" """ % (fs, pid)
            cur.execute(q)
            conn.commit()

            print("""
                    <script>
                       alert("Updated successfully");
                    </script>
                    """)
conn.close()