#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python310/python.exe

print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb

form = cgi.FieldStorage()

pid = form.getvalue("id")

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="//netdna.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//netdna.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
<script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
<!------ Include the above in your HEAD tag ---------->


<link href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">

<link rel="icon" type="image/x-icon" href="./media/logoonly.png">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>

    <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet" type="text/css">


<style>

.mar{
    margin-top:-150px;

    margin-left:550px;
}
body {
  margin: 0px;
  padding: 0px;
}
.main {
  margin-left: 300px; /* Same as the width of the sidenav */
  font-size: 20px; /* Increased text to enable scrolling */
  padding: 0px 10px;
}
</style>
</head>
<body>

</body>
      </html>
      """)

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="empdb")
cur = conn.cursor()

q = """select*from empdata where id="%s" """ % (pid)
cur.execute(q)
rec = cur.fetchall()
for i in rec:
    empid = i[1]
    name = i[2]
    date = i[3]
    role = i[4]
    contact = i[5]
    mailid = i[6]
    address = i[7]
    city = i[8]
    state = i[9]
    type = i[10]
    uname = i[11]
    pwd = i[12]

    print("""
    <div>
    <form  style="margin-top:30px;"name="loginform"
        onsubmit="return login()">

        <!-- Modal content-->

        <div >
            <div  class="col-md-4>
                <span onclick="document.getElementById('more').style.display='none'" data-dismiss="modal"
                    </span>
                <h4 class="modal-title text-center heading">
                    Employee Details</h4>
            </div>
            <!-- model -->
            <div class="col-md-4"></div>
            <div  class="col-md-4" style="padding: 50px;" >
                <div class="input-container">

               <input class="form-control" type="text" readonly value="%s" required name="empid"><br>

                <input class="form-control" type="text" name="name"value="%s" placeholder="Name" maxlength="20" required><br>
                <input class="form-control" type="text" name="dob" value="%s" placeholder="Dob" maxlength="20" required><br>
               <input class="form-control" type="text" name="role" value="%s" placeholder="Role" maxlength="20" required><br>
               <input class="form-control" type="text" name="phone" value="%s" placeholder="contact no" maxlength="20" required><br>
               <input class="form-control" type="text" name="mail" value="%s" placeholder="Email_id" maxlength="20" required><br>
                <input class="form-control" type="text" name="address" value="%s" placeholder="Address" maxlength="100"><br>
                <input class="form-control" type="text"  name="city" value="%s" maxlength="20"  required>
                  <br>
                <input class="form-control" type="text" value="%s" name="state" maxlength="20"  required>
                  <br>
                <input class="form-control" type="text" value="%s" name="type" maxlength="20"  required>
                   <br>
                 <input class="form-control" type="text" name="uname"value="%s" placeholder="Username" maxlength="20" required><br>
                <input class="form-control" type="text" name="pwd" value="%s" placeholder="Password" maxlength="20" required><br>
                <br>
                <input class="form-control btn btn-info" type="Submit" name="login" value="update"><br><br><br>
            </form>
            """ % (empid, name, date, role, contact, mailid, address, city, state, type, uname, pwd))
print("""
</table>
</div>
</body>
</html>
""")
import pymysql
import cgi, cgitb

cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="empdb")
cur = conn.cursor()

# form = cgi.FieldStorage()

psubmit = form.getvalue("login")
if psubmit != None:
    empid = form.getvalue("empid")
    name = form.getvalue("name")
    date = form.getvalue("dob")
    role = form.getvalue("role")
    contact = form.getvalue("phone")
    mailid = form.getvalue("mail")
    address = form.getvalue("address")
    city = form.getvalue("city")
    state = form.getvalue("state")
    type = form.getvalue("type")
    uname = form.getvalue("uname")
    pwd = form.getvalue("pwd")
    q = """update empdata set name='%s', dob='%s' ,role='%s' ,contact='%s', emailid='%s', address='%s' ,city='%s' ,state='%s' ,type='%s', username='%s', password='%s' where emp_id='%s' """ % (name, date, role, contact, mailid, address, city, state, type, uname, pwd, empid)
    cur.execute(q)
    conn.commit()
    if (q):
        print("""
        <script>
           alert("Updated successfully");
           location.href="./adminempdataview.py";
        </script>
        """)
    else:
        print("""
                <script>
                   alert("Not Updated successfully");
                   location.href="./adminempedit.py?id=%s";
                </script>
                """ % (pid))

conn.close()