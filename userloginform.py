#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python310/python.exe
print("content-type:text/html \r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LOGIN FORM</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background-image: url(./assets/logbg2.jpg);
            background-size: cover;
        }

        .container {
            top: 50%;
            left: 50%;
            position: absolute;
            transform: translate(-50%, -50%);
        }

        .card {
            padding: 60px 40px 50px 40px;
            background-color: black;
            border-radius: 10px;
        }

        #name {
            border-radius: 20px;
            width: 200px;
            border: none;
            background: transparent;
            border-bottom: 1px solid white;
            padding: 6px;
            margin-bottom: 20px;
            color: aliceblue;
        }

        #button {
            margin-top: 30px;
            border: 20px;
            padding: 10px 20px;
            background-color: blue;
            color: white;
            margin-left: 50px;
            border-radius: 30px;
        }

        #button:hover {
            background-color: greenyellow;
            color: black;
            cursor: pointer;
        }

        a {
            font-size: 15px;

        }

        .user {
            border-radius: 50%;
            position: absolute;
            margin-left: 100px;
            margin-top: -40px;
        }
    </style>
</head>

<body>
    <div class="modal-body">
        <form action="" name="login_form" method="post" >
            <div class="container">
                <img class="user" src="./image/WhatsApp Image 2023-12-07 at 11.22.08 AM.jpeg" alt="" height="70px"
                    width="70px">
                <div class="card">
                    <input type="text" placeholder="Username" name="uname" id="name"><br>
                    <input type="password" placeholder="Password" name="pass" id="name"><br>
                    <a href="#">Forget password</a><br>
                    <input type="submit" value="Submit" name="submit" id="button">
                </div>
            </div>
        </form>
    </div>
    
</body>

</html>
      """)
import pymysql
import cgi,cgitb

cgitb.enable()
conn=pymysql.connect(host="localhost",user="root",password="",database="empdb")
cur=conn.cursor()

form=cgi.FieldStorage()
puname=form.getvalue("uname")
ppwd=form.getvalue("pass")
psubmit=form.getvalue("submit")

if psubmit!=None:

    q="""select id from user_data where uname='%s' and pass='%s'"""%(puname,ppwd)

    cur.execute(q)
    rec=cur.fetchone()
    conn.commit()

    if rec!=None:
        print("""
          <script>
           alert("login is successfull");
           location.href="userpage.py?id=%s";
        </script>
        """%rec[0])


    else:
        print("""
          <script>
            alert("Please enter a valid username and password");
        </script>
        """)

conn.close()