<?php 
    $email = $_POST['inputEmail'];
    $password = $_POST['inputPassword'];
    $error = "";
    $forgotPass = "";

    //checking to see if the login info is valid
    if (isset($_POST['submit'])) { //if the submit button is clicked
        //user login
        if ($email == "user@email.com") { //CHECK DATABASE FOR MATCHING USER EMAIL HERE
            if ($password == "password") { //CHECK DATABASE FOR MATCHING PASSWORD HERE
                header("Location: userprofile.php"); //redirects to user profile
            }
            else {
                $error = "Oops! That's the wrong password!";
            }
        }
        //admin login
        elseif ($email == "admin@email.com") { //CHECK DATABASE FOR MATCHING ADMIN EMAIL HERE
            if ($password == "password") { //CHECK DATABASE FOR MATCHING PASSWORD HERE
                header("Location: adminprofile.php"); //redirects to admin profile
            }
            else {
                $error = "Oops! That's the wrong password!";
            }
        }
        else {
            $error = "Oops! That email is not linked to an existing account.";
        }
    }
?>


<!doctype html>

<head>
    <meta charset="utf-8">
    <title>Sign in</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
        crossorigin="anonymous">
    <link rel="stylesheet" href="css/styles.css">
    <link rel="icon" type="image/png" sizes="32x32" href="css/favicon.png">
</head>

<body>
    <div class="main-content" style="margin: 15%;">
        <h1>Sign in</h1>
        <p class="error"><?php echo $error; ?></p>
        <form method="POST">

            <div class="form-row">
                <div class="form-group col-md-6">
                    <label for="inputEmail">Email (required)</label>
                    <input type="email" class="form-control" name="inputEmail" id="inputEmail" placeholder="example@email.com" required>
                </div>
                <div class="form-group col-md-6">
                    <label for="inputPassword">Password (required)</label>
                    <input type="password" class="form-control" name="inputPassword" id="inputPassword" placeholder="Example1234" required>
                </div>
            </div>

            <button name="submit" type="submit" class="btn btn-outline-dark" style="float:right;">Sign in</button>

            <button type="button" class="btn btn-outline-dark" onclick="history.go(-1)">Go Back</button>
        </form>
        <br>
        <button name="forgotPass" class="btn btn-outline-dark" onclick="window.location.href = 'forgotpass.php';">Forgot Password?</button>
    </div>
</body>

<footer>
    <p>Copyright © 2020 | Our Bookstore | All rights reserved.</p>
</footer>

</html>