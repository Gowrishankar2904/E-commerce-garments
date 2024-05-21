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
    <script>
        var uname, pass;

        function validate() {
            uname = document.forms["login_form"]["uname"];
            pass = document.forms["login_form"]["pass"];

            if (uname.value == "") {
                alert("please enter your user name");
                uname.focus()
                return false;
            }

            if (pass.value == "") {
                alert("please enter your user password");
                pass.focus()
                return false;
            }

            if (uname.value == "abimanyu" && pass.value == "12345") {
                alert("login is success");
                return true;
            }
            else {
                alert("invalid data");
                return false;
            }
        }
    </script>
</head>

<body>
    <div class="modal-body">
        <form action="./admin dashboard.py" name="login_form" method="post" onsubmit=" return validate()">
            <div class="container">
                <img class="user" src="./image/WhatsApp Image 2023-12-07 at 11.22.08 AM.jpeg" alt="" height="70px"
                    width="70px">
                <div class="card">
                    <input type="text" placeholder="Username" name="uname" id="name"><br>
                    <input type="password" placeholder="Password" name="pass" id="name"><br>
                    <a href="#">Forget password</a><br>
                    <input type="submit" value="Submit" id="button">

                </div>
            </div>
        </form>
    <div>
        
</body>

</html>
      """)